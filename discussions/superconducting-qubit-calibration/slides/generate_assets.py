#!/usr/bin/env python3
"""Package recorded evidence; reconstruct Rabi curves at recorded frequencies.

No acquisition or nonlinear physical-parameter fitting is performed.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
DEFAULT_SOURCE = HERE.parents[3] / 'agent_control'
FONT_ROOT = HERE.parents[2] / 'skills/write-slides/assets/company-beamer/fonts'
for font in FONT_ROOT.glob('OpenSans-*.ttf'):
    font_manager.fontManager.addfont(font)
plt.rcParams.update({'font.family':'Open Sans', 'font.weight':'semibold',
    'axes.labelweight':'semibold', 'axes.labelsize':14,
    'xtick.labelsize':14, 'ytick.labelsize':14, 'pdf.fonttype':42})
SLUG = {'T1 Visibility':'t1','T2 Ramsey':'ramsey','Rabi Oscillation':'rabi',
        'Qubit Spectroscopy':'spectroscopy','GMM Readout Clusters':'readout','Resonator Spectroscopy':'resonator'}
ORDER = list(SLUG)
MAIN = [('Resonator Spectroscopy','006'),
        ('Qubit Spectroscopy','008'),('Qubit Spectroscopy','005'),
        ('Rabi Oscillation','003'),('Rabi Oscillation','007'),
        ('T1 Visibility','004'),('T2 Ramsey','008'),
        ('GMM Readout Clusters','008')]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def esc(s):
    return str(s).replace('\\',r'\textbackslash{}').replace('_',r'\_').replace('%',r'\%').replace('&',r'\&').replace('#',r'\#').replace('–','--').replace('→',r'$\to$')

def explanation(fam, case, r):
    m=r['metrics']; flags=r['review_flags']
    if fam=='T1 Visibility':
        title='Baseline 改变时，lifetime 是否稳定？'
        obs=f"Free-offset / zero-offset fit：{m['contrast_tau_us']:.2f} / {m['zero_offset_tau_us']:.2f} us；检查 baseline 依赖。"
        cause='Baseline 未稳定、晚时刻 contrast 未归零，或 exponential model 的假设不满足。'
        check='延长 delay；交错测量 no-pi reference；比较 baseline 稳定性与不同 fit window。'
        if case=='004':
            title='Flat trace 不能确定一个很长的 T1'
            obs='Nominal with-pi P1：0.956 → 0.950（0–100 us）；几乎没有 resolved decay。'
            cause='Lifetime 超出窗口；delay 未实际改变；readout 前重激发；channel 或 acquisition 有误。'
            check='核对 executed sequence 与 time units；重复 preparation reference，再扩大 delay window。'
        elif case=='005':
            obs+=' Residual 还存在相邻关联。'
        metric=rf"Contrast fit: $R^2={m['r2']:.3f}$; free / zero offset $\tau={m['contrast_tau_us']:.2f}/{m['zero_offset_tau_us']:.2f}\,\mu s$"
        if case=='004':metric=rf"Contrast fit: $R^2={m['r2']:.3f}$; lifetime reaches $10000\,\mu s$ fit bound; lifetime unresolved"
    elif fam=='GMM Readout Clusters':
        title='Preparation label 不等于可可靠区分的 state'
        obs=f"Held-out linear balanced accuracy = {100*m['heldout_balanced_accuracy']:.2f}%；nominal preparation groups 重叠。"
        cause='Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。'
        check='先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。'
        if case=='005':
            title='接近 screen threshold：需要检查，但不宜二分判错'
            obs=f"Balanced accuracy = {100*m['heldout_balanced_accuracy']:.2f}%，略低于本地 75% screen threshold；threshold 不是物理定律。"
        metric=rf"Held-out linear classifier: balanced accuracy ${100*m['heldout_balanced_accuracy']:.2f}\%$; not original GMM fidelity"
    elif fam=='Rabi Oscillation':
        title='Sinusoid 是否足以描述这个 amplitude scan？'
        obs=f"IQ-projection sinusoid：R2={m['r2']:.3f}；相邻 residual correlation={m['residual_lag1']:.2f}。"
        cause='Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。'
        check='重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。'
        if 'LIMITED_OSCILLATION_COVERAGE' in flags:
            title=('高 fit score 不保证 period 已被测到' if m['r2']>=.9
                   else 'Scan 未覆盖完整 cycle，period 缺乏约束')
            obs=f"Scan 仅覆盖 candidate cycle 的 {m['cycles_in_scan']:.2f}；period 很大部分来自 extrapolation。"
            cause='Amplitude window 太短；局部 response 被误当作完整 sinusoid；模型可辨识性不足。'
            check='在合适的控制范围内扩大 amplitude scan；观察 turning point 与 return；验证 pi endpoint。'
        if case in ('001','003'):
            title='Noise-like trace 中，fitter 仍然会返回 period'
            obs=f"没有清晰完整 cycle；R2={m['r2']:.3f}；每个 fitted cycle 仅 {m['samples_per_cycle']:.2f} 个 samples。"
            cause='Drive / readout contrast 不足、frequency 不准或 pulse path 问题；candidate 高频也可能是 noise fitting。'
            check='先验证 spectroscopy 与 readout，再重复 sweep；不能直接采用 fitted half-period 作为 pi amplitude。'
        elif 'IQ_NOT_WELL_APPROXIMATED_BY_FIXED_TWO_STATE_LINE' in flags:
            obs+=f" Orthogonal IQ variance fraction={m['orthogonal_iq_variance_fraction']:.2f}。"
            cause='Noise、readout response 变化或额外 state contribution；IQ 几何本身不能证明 leakage。'
            check='检查完整 IQ trajectory 与重复 scan；独立验证 readout，必要时增加 leakage-sensitive measurement。'
        metric=rf"IQ-projection fit: $R^2={m['r2']:.3f}$; coverage ${m['cycles_in_scan']:.2f}$ cycles; ${m['samples_per_cycle']:.1f}$ samples/cycle"
    elif fam=='Qubit Spectroscopy':
        title='存在 feature，不等于 single-line model 已可靠'
        obs=f"Single-Lorentzian IQ fit：R2={m['r2']:.3f}；candidate FWHM={1000*m['candidate_fwhm_GHz']:.2f} MHz。"
        cause='Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。'
        check='重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。'
        if case in ('002','011','014','015'):
            title='Background 中的 fitted line 不足以确定 f10'
            obs=f"Whole-scan IQ fit 的 R2={m['r2']:.3f}；缺少清晰可复现的 single feature 证据。"
            cause='Transition 不在窗口、drive 或 readout contrast 太弱；也可能存在很窄但尚未验证的 feature。'
            check='验证 probe 与 drive path；调整 scan window；重复局部 candidate frequency，检查 reproducibility。'
        elif 'FEATURE_NEAR_SCAN_EDGE' in flags:
            title='Scan boundary 限制了 resonance center 的判断'
            obs=f"Candidate center={m['candidate_center_GHz']:.3f} GHz 位于 scan 边界；不能完整观察两侧 response。"
            cause='Feature 延伸到窗口外、多个 transitions 或 baseline 变化；边界值不是已测定的 center。'
            check='扩大 frequency window 观察两侧；检查 candidate feature 的复现性与 drive-strength dependence。'
        elif 'FEATURE_WIDTH_POORLY_SAMPLED' in flags:
            title='Fit score 不能补足 frequency resolution'
            obs=f"Frequency step={1000*m['step']:.2f} MHz，candidate FWHM={1000*m['candidate_fwhm_GHz']:.2f} MHz；采样不足。"
            cause='实际窄 resonance 或 isolated outlier；现有 grid 无法可靠区分，也不支持过高 linewidth precision。'
            check='在 feature 附近使用更小 frequency step，并重复采样；比较 peak / dip 的宽度与 reproducibility。'
        metric=rf"IQ single-line diagnostic: $R^2={m['r2']:.3f}$; step ${1000*m['step']:.2f}$ MHz; FWHM ${1000*m['candidate_fwhm_GHz']:.2f}$ MHz"
    elif fam=='T2 Ramsey':
        title='一个 exponential envelope 能否描述全部 delay？'
        obs=f"Single-frequency exponential fit：R2={m['r2']:.3f}；residual correlation={m['residual_lag1']:.2f}。"
        cause='Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。'
        check='检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。'
        if case=='008':
            title='Envelope 结构超出单一 exponential model'
            obs='Dense oscillation trace 在约 40–50 us 重新变宽；single-envelope fit 不能覆盖全部结构。'
            cause='Multiple frequencies / beating、drift 或 readout / noise 变化；不能仅凭图确认 low-frequency noise。'
        elif case in ('002','006'):
            title='较清晰 oscillation 也可能留下 correlated residual'
            obs=f"可见 decaying oscillation，R2={m['r2']:.3f}；residual correlation={m['residual_lag1']:.2f}，仍需检查。"
        metric=rf"Recorded Ramsey fit: $R^2={m['r2']:.3f}$; candidate $T_2^*={m['tau_us']:.2f}\,\mu s$; residual correlation ${m['residual_lag1']:.2f}$"
    else:
        title='First-point spike 是 resonance 还是 acquisition transient？'
        obs='Scaled magnitude 首点约 1728，次点约 66，后续 median 约 41；窗口内无 resolved interior resonance。'
        cause='Settling / acquisition discontinuity、edge / out-of-window resonance，或 useful signal 不足。'
        check='加入 settling 后重测首点；反向 sweep；扩大窗口并同时检查 phase / IQ。'
        metric=r"Descriptive screen only: window 6.000--6.130 GHz; no validated transfer-function fit"
    return dict(title=title,observation=obs,cause=cause,check=check,metric=metric)

def reference(fam,case):
    if fam=='GMM Readout Clusters': return '007' if case=='008' else '009'
    if fam=='T2 Ramsey':return '006' if case=='002' else '002'
    if fam=='Qubit Spectroscopy' and case in ('009','013','018'):return '010'
    return {'T1 Visibility':'002','Rabi Oscillation':'002','Qubit Spectroscopy':'001','Resonator Spectroscopy':'001'}[fam]

def projection(a):
    iq=a[:,4:6]-a[:,4:6].mean(0)
    _,_,vt=np.linalg.svd(iq,full_matrices=False)
    y=iq@vt[0]
    return y/max(y.std(),1e-12)

def panel(ax,fam,case,record,a,is_reference):
    m=record['metrics']
    qubit=re.search(r' - (q\d+)',record['source'])
    ax.set_title(('Reference' if is_reference else 'Needs review')+f' / {case}'+(f' / {qubit[1]}' if qubit else ''),loc='left',fontsize=16,fontweight='bold')
    ax.grid(alpha=.14)
    ax.tick_params(labelsize=14)
    if fam=='GMM Readout Clusters':
        ax.scatter(a[:,1],a[:,2],s=2.2,alpha=.28,color='#1d6a9c',rasterized=True,label='Without pi')
        ax.scatter(a[:,3],a[:,4],s=2.2,alpha=.28,color='#cf6a38',rasterized=True,label='With pi')
        ax.set(xlabel='I (a.u.)',ylabel='Q (a.u.)')
        ax.legend(loc='upper right',fontsize=14,markerscale=3)
    elif fam=='T1 Visibility':
        ax.plot(a[:,0],a[:,2],'.-',ms=3,lw=.7,color='#1d6a9c',label='Nominal with pi')
        ax.plot(a[:,0],a[:,4],'.-',ms=3,lw=.7,color='#cf6a38',label='Nominal no pi')
        ax.set(xlabel='Delay (us)',ylabel='Recorded P1',ylim=(-.03,1.03))
        ax.legend(loc='best',fontsize=14)
    elif fam=='T2 Ramsey':
        ax.plot(a[:,0],a[:,2],'.',ms=1.3,color='#1d6a9c',alpha=.7,rasterized=True)
        t=np.linspace(a[0,0],a[-1,0],600)
        envelope=m['oscillation_amplitude']*np.exp(-t/m['tau_us'])
        ax.plot(t,m['offset']+envelope,'--',lw=1,color='#c25c38',label='Recorded-fit envelope')
        ax.plot(t,m['offset']-envelope,'--',lw=1,color='#c25c38')
        ax.set(xlabel='Delay (us)',ylabel='Recorded P1',ylim=(0,1))
        ax.legend(loc='upper right',fontsize=14)
    elif fam=='Rabi Oscillation':
        y=projection(a);x=a[:,0];f=m['frequency_per_amplitude']
        design=np.column_stack([np.ones(len(x)),np.cos(2*np.pi*f*x),np.sin(2*np.pi*f*x)])
        coef=np.linalg.lstsq(design,y,rcond=None)[0]
        r2=1-np.sum((y-design@coef)**2)/np.sum((y-y.mean())**2)
        assert abs(r2-m['r2'])<1e-6
        ax.plot(x,y,'.',ms=3,color='#1d6a9c',label='IQ projection')
        t=np.linspace(x[0],x[-1],1500)
        ax.plot(t,np.column_stack([np.ones(len(t)),np.cos(2*np.pi*f*t),np.sin(2*np.pi*f*t)])@coef,lw=1,color='#c25c38',label='Fit (recorded frequency)')
        ax.set(xlabel='Drive amplitude (setting)',ylabel='IQ projection\n(standardized)')
        ax.legend(loc='best',fontsize=14)
    else:
        x=a[:,0]; y=a[:,3]/1000
        if fam=='Qubit Spectroscopy' and case=='005' and not is_reference:
            k=np.argmax(y); sl=slice(max(0,k-6),min(len(x),k+7));x=x[sl];y=y[sl]
            ax.set_title(f'Review / {case} (local zoom)',loc='left',fontsize=16,fontweight='bold')
        ax.plot(x,y,'.-',ms=2.7,lw=.6,color='#1d6a9c')
        ax.set(xlabel=('Drive' if fam=='Qubit Spectroscopy' else 'Probe')+' frequency (GHz)',ylabel='Scaled magnitude\n/ 1000 (a.u.)')
        ax.ticklabel_format(axis='x',style='plain',useOffset=False)
    for spine in ax.spines.values(): spine.set_color('#49433f')
    # Shared, readable legend below both panels; keep the curves unobscured.
    legend=ax.get_legend()
    if legend is not None: legend.remove()

def make_figure(fam,case,records,out):
    ref=reference(fam,case)
    fig,axs=plt.subplots(1,2,figsize=(8.1,2.9))
    for ax,c,is_ref in zip(axs,[ref,case],[True,False]):
        a=np.loadtxt(HERE/'data'/f'{SLUG[fam]}-{c}.csv',delimiter=',')
        panel(ax,fam,c,records[fam,c],a,is_ref)
    handles,labels=axs[0].get_legend_handles_labels()
    fig.tight_layout(pad=.6,w_pad=1.4,rect=(0,.17 if handles else 0,1,1))
    if handles:
        fig.legend(handles,labels,loc='lower center',ncol=2,fontsize=14,
                   frameon=False,markerscale=2,handlelength=1.4,columnspacing=1.2)
    fig.savefig(out,metadata={'Title':f'{fam} {ref} versus {case}','Author':'0918 calibration study'})
    plt.close(fig)

def slide_content(fam,case,record):
    """Select visible evidence; retain complete interpretation in case-notes.md."""
    m=record['metrics'];flags=record['review_flags']
    if fam=='T1 Visibility':
        title='基线的选择影响衰减时间'
        metric=rf"两路布居差拟合： $\tau_{{free}}={m['contrast_tau_us']:.2f}$ / $\tau_0={m['zero_offset_tau_us']:.2f}\,\mu s$"
        if case=='004':
            title='平坦曲线无法确定 T1'
            metric=r"0--100 $\mu s$ 内 $P_1$ 从 0.956 变为 0.950；拟合触及 10000 $\mu s$ 上界"
        caveat='准备顺序为推断；拟合对象是两路布居差。'
    elif fam=='GMM Readout Clusters':
        title='两组准备条件的区分仍需验证'
        if case=='008':title='两组准备条件的 IQ 分布明显重叠'
        if case=='005':title='接近筛查阈值仍需结合数据判断'
        metric=rf"线性分类器的留出评估平衡准确率： ${100*m['heldout_balanced_accuracy']:.2f}\%$"
        caveat='预测准备标签；包含状态准备与弛豫的影响。'
    elif fam=='Rabi Oscillation':
        title='单一正弦模型仍有未解释的结构'
        if 'LIMITED_OSCILLATION_COVERAGE' in flags:title='局部曲线不足以约束周期'
        if case in ('001','003'):title='噪声状曲线也会返回拟合周期'
        elif 'IQ_NOT_WELL_APPROXIMATED_BY_FIXED_TWO_STATE_LINE' in flags:title='IQ 分布偏离固定两态连线'
        metric=rf"IQ 投影拟合： $R^2={m['r2']:.3f}$；扫描覆盖 ${m['cycles_in_scan']:.2f}$ 个周期"
        if case in ('001','003'):metric+=rf"；每周期 ${m['samples_per_cycle']:.2f}$ 个采样点"
        caveat='IQ 投影独立标准化，符号与大小不可跨案例比较。'
    elif fam=='Qubit Spectroscopy':
        title='可见响应仍需检查线形模型'
        if case in ('002','011','014','015'):title='背景中的候选响应仍需验证'
        elif 'FEATURE_NEAR_SCAN_EDGE' in flags:title='扫描边界限制了中心频率的判断'
        elif 'FEATURE_WIDTH_POORLY_SAMPLED' in flags:title='频率步长不能分辨拟合线宽'
        metric=rf"IQ 投影诊断： $R^2={m['r2']:.3f}$；步长 {1000*m['step']:.2f} / 半高全宽 {1000*m['candidate_fwhm_GHz']:.2f} MHz"
        caveat='图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。'
    elif fam=='T2 Ramsey':
        title='单一包络仍有未解释的结构'
        if case=='008':title='振荡结构超出单一包络模型'
        if case in ('002','006'):title='较清晰振荡也留下相关残差'
        metric=rf"已有拟合： $R^2={m['r2']:.3f}$；相邻残差相关系数 ${m['residual_lag1']:.2f}$"
        caveat='对照也有复查项；虚线仅表示包络，不是完整振荡预测。'
    else:
        title='首点尖峰的来源仍未确定'
        metric=r"扫描范围 6.000--6.130 GHz；窗口内部未分辨出共振"
        caveat='此处为曲线观察，尚无经过验证的传输函数拟合。'
    return title,metric,caveat

def frame(fam,case,record):
    slug=SLUG[fam];title,metric,caveat=slide_content(fam,case,record)
    return '\n'.join([
        rf'\begin{{frame}}[t,label=case-{slug}-{case}]{{{title}}}{{{fam} / {case}}}',
        r'\setlength{\parskip}{0pt}',
        r'\begingroup',
        r'\setlength{\topsep}{0pt}\setlength{\partopsep}{0pt}',
        r'\begin{figure}',
        r'\centering',
        rf'\includegraphics[width=\linewidth,height=43mm,keepaspectratio]{{figures/{slug}-{case}.pdf}}',
        rf'\caption{{案例 {case} 与对照 {reference(fam,case)}。{metric}。{caveat}}}',
        rf'\label{{fig-{slug}-{case}}}',
        r'\end{figure}',
        r'\endgroup',
        r'\end{frame}',
    ])

def case_note(fam,case,record):
    d=explanation(fam,case,record);ref=reference(fam,case);slug=SLUG[fam]
    metric=d['metric']
    lines=[f'<a id="case-{slug}-{case}"></a>',f'## {fam} / {case}','',
        f'**{d["title"]}**','',
        f'[对照图](figures/{slug}-{case}.pdf) · [Target CSV](data/{slug}-{case}.csv) · [Reference / {ref}](data/{slug}-{ref}.csv)','',
        f'**来源与诊断**：0918 packaged CSV 与 recorded audit；{metric}。','',
        f'**Codex interpretation — 观察**：{d["observation"]}','',
        '> [!hypothesis]',
        f'> Suggested by Codex; not yet verified. {d["cause"]}','',
        f'**验证方向**：{d["check"]}','',
        f'**读图条件**：{slide_content(fam,case,record)[2]}']
    if fam=='Rabi Oscillation':
        lines+=['','Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。']
    elif fam=='Qubit Spectroscopy':
        lines+=['','低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。']
    elif fam=='GMM Readout Clusters':
        lines+=['','这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。']
    elif fam=='T1 Visibility':
        lines+=['','图显示两路 recorded P1；diagnostic 拟合的是 preparation-channel contrast。触及 fit bound 不构成该上界 lifetime 的测量。']
    elif fam=='T2 Ramsey':
        lines+=['','Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。']
    else:
        lines+=['','原 scaled magnitude 首点约 1728、次点约 66、后续 median 约 41；图显示除以 1000 后的相同数据。不同 case 的 scale / settings 独立；多个 features 本身不构成错误。']
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,help='agent_control checkout; import verified recorded data instead of using packaged snapshots')
    args=ap.parse_args()
    for directory in ['data','figures','generated']:(HERE/directory).mkdir(exist_ok=True)
    evidence=HERE/'evidence.json'
    if args.source or not evidence.exists():
        source=(args.source or DEFAULT_SOURCE).resolve();out=source/'output/review_0918'
        status=json.loads((out/'status.json').read_text());manifest=json.loads((out/'manifest.json').read_text())
        assert status['status']=='complete'
        for f,k in [('manifest.json','manifest_sha256'),('summary.md','summary_sha256')]:assert sha(out/f)==status[k]
        for f,h in manifest['input_sha256'].items():assert sha(Path(f))==h,f
        review=json.loads((out/'raw_physics/results.json').read_text())
        assert sha(source/'scripts/audit_raw_physics.py')==review['manifest']['script_sha256']
        packaged=[]
        for r in review['cases']:
            p=Path(r['source']);assert sha(p)==r['sha256']
            slug=SLUG[r['family']];dest=HERE/'data'/f'{slug}-{r["case"]}.csv'
            shutil.copyfile(p,dest)
            q=dict(r);q['source']=p.relative_to(source).as_posix();q['packaged_source']=dest.relative_to(HERE).as_posix();packaged.append(q)
        evidence.write_text(json.dumps({'scope':'Reused completed recorded audit; no new physics fit or acquisition.',
            'prepared_date':'2026-10-10','review_status':status,'review_generated_utc':manifest['generated_utc'],
            'raw_results_sha256':sha(out/'raw_physics/results.json'),'audit_script_sha256':review['manifest']['script_sha256'],
            'policy':review['policy'],'runtime':review['manifest'],'cases':packaged},ensure_ascii=False,indent=2)+'\n')
    package=json.loads(evidence.read_text());records={(r['family'],r['case']):r for r in package['cases']}
    for r in package['cases']:assert sha(HERE/r['packaged_source'])==r['sha256']
    targets=[(fam,r['case']) for fam in ORDER for r in package['cases'] if r['family']==fam and r['review_flags']]
    targets.append(('Resonator Spectroscopy','006'))
    assert len(targets)==47 and len(set(targets))==47
    assert set(MAIN)<=set(targets)
    appendix=[k for k in targets if k not in MAIN]
    for fam,case in targets:make_figure(fam,case,records,HERE/'figures'/f'{SLUG[fam]}-{case}.pdf')
    for name,items in [('main-cases',MAIN),('appendix-cases',appendix)]:
        (HERE/'generated'/f'{name}.tex').write_text('\n\n'.join(frame(f,c,records[f,c]) for f,c in items)+'\n')
    index=[]
    for label,title,families in [('case-index','完整案例：时间与脉冲',ORDER[:3]),
                                  ('case-index-other','完整案例：频谱与读出',ORDER[3:])]:
        index += [rf'\begin{{frame}}[label={label}]{{{title}}}',
                  r'\setlength{\parskip}{.6mm}\small',
                  r'* 表示正文中的代表案例；点击编号跳转。\par\vspace{2mm}']
        for fam in families:
            keys=[k for k in targets if k[0]==fam]
            links=[rf'\hyperlink{{case-{SLUG[fam]}-{c}}}{{\beamerbutton{{{c+("*" if (fam,c) in MAIN else "")}}}}}' for _,c in keys]
            rows=[ ' '.join(links[i:i+8]) for i in range(0,len(links),8)]
            index.append(rf'\textbf{{{fam}}} ({len(keys)})\par '+r'\par\vspace{1mm}'.join(rows)+r'\par\vspace{2mm}')
        other='case-index-other' if label=='case-index' else 'case-index'
        index += [rf'\vfill\hyperlink{{{other}}}{{\beamerbutton{{另一页导航}}}}',r'\end{frame}']
    (HERE/'generated'/'case-index.tex').write_text('\n'.join(index)+'\n',encoding='utf-8')
    note_header=['# 0918 案例解释与验证方向','',
        '2026-10-12 — 配套 slides 的详细案例笔记。诊断复用 recorded audit；解释为 Codex interpretation，可能原因为未验证假设。','',
        '[主笔记](notes.md) · [完整 PDF](0918-calibration-zh.pdf) · [案例索引](coverage.md)','',
        '所有 47 个案例的 reference selection 与既有版本一致；reference 表示相对清晰，不构成 calibration certification。不同 cases 通常不是 controlled pairs。','']
    (HERE/'case-notes.md').write_text('\n'.join(note_header)+'\n'+ '\n\n'.join(case_note(f,c,records[f,c]) for f,c in targets)+'\n',encoding='utf-8')
    listing=['# Case coverage','', '* marks a main-deck case; all others appear in the appendix.','', '| Family | Target and explanation | Reference | Location |','| --- | --- | --- | --- |']
    for fam,c in targets:listing.append(f'| {fam} | [{c}](case-notes.md#case-{SLUG[fam]}-{c}) | {reference(fam,c)} | '+('Main*' if (fam,c) in MAIN else 'Appendix')+' |')
    (HERE/'coverage.md').write_text('\n'.join(listing)+'\n')
    (HERE/'generated'/'coverage.json').write_text(json.dumps({'main':MAIN,'appendix':appendix,'total':47},indent=2)+'\n')
    print(f'Verified {len(records)} packaged CSVs; generated 47 paired figures, 8 main frames, 39 appendix frames.')

if __name__=='__main__':main()
