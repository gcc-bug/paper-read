# 0918 案例解释与验证方向

2026-10-12 — 配套 slides 的详细案例笔记。诊断复用 recorded audit；解释为 Codex interpretation，可能原因为未验证假设。

[主笔记](notes.md) · [完整 PDF](0918-calibration-zh.pdf) · [案例索引](coverage.md)

所有 47 个案例的 reference selection 与既有版本一致；reference 表示相对清晰，不构成 calibration certification。不同 cases 通常不是 controlled pairs。

<a id="case-t1-001"></a>
## T1 Visibility / 001

**Baseline 改变时，lifetime 是否稳定？**

[对照图](figures/t1-001.pdf) · [Target CSV](data/t1-001.csv) · [Reference / 002](data/t1-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Contrast fit: $R^2=0.972$; free / zero offset $\tau=55.94/77.48\,\mu s$。

**Codex interpretation — 观察**：Free-offset / zero-offset fit：55.94 / 77.48 us；检查 baseline 依赖。

> [!hypothesis]
> Suggested by Codex; not yet verified. Baseline 未稳定、晚时刻 contrast 未归零，或 exponential model 的假设不满足。

**验证方向**：延长 delay；交错测量 no-pi reference；比较 baseline 稳定性与不同 fit window。

**读图条件**：准备顺序为推断；拟合对象是两路布居差。

图显示两路 recorded P1；diagnostic 拟合的是 preparation-channel contrast。触及 fit bound 不构成该上界 lifetime 的测量。

<a id="case-t1-004"></a>
## T1 Visibility / 004

**Flat trace 不能确定一个很长的 T1**

[对照图](figures/t1-004.pdf) · [Target CSV](data/t1-004.csv) · [Reference / 002](data/t1-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Contrast fit: $R^2=0.008$; lifetime reaches $10000\,\mu s$ fit bound; lifetime unresolved。

**Codex interpretation — 观察**：Nominal with-pi P1：0.956 → 0.950（0–100 us）；几乎没有 resolved decay。

> [!hypothesis]
> Suggested by Codex; not yet verified. Lifetime 超出窗口；delay 未实际改变；readout 前重激发；channel 或 acquisition 有误。

**验证方向**：核对 executed sequence 与 time units；重复 preparation reference，再扩大 delay window。

**读图条件**：准备顺序为推断；拟合对象是两路布居差。

图显示两路 recorded P1；diagnostic 拟合的是 preparation-channel contrast。触及 fit bound 不构成该上界 lifetime 的测量。

<a id="case-t1-005"></a>
## T1 Visibility / 005

**Baseline 改变时，lifetime 是否稳定？**

[对照图](figures/t1-005.pdf) · [Target CSV](data/t1-005.csv) · [Reference / 002](data/t1-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Contrast fit: $R^2=0.909$; free / zero offset $\tau=33.01/44.48\,\mu s$。

**Codex interpretation — 观察**：Free-offset / zero-offset fit：33.01 / 44.48 us；检查 baseline 依赖。 Residual 还存在相邻关联。

> [!hypothesis]
> Suggested by Codex; not yet verified. Baseline 未稳定、晚时刻 contrast 未归零，或 exponential model 的假设不满足。

**验证方向**：延长 delay；交错测量 no-pi reference；比较 baseline 稳定性与不同 fit window。

**读图条件**：准备顺序为推断；拟合对象是两路布居差。

图显示两路 recorded P1；diagnostic 拟合的是 preparation-channel contrast。触及 fit bound 不构成该上界 lifetime 的测量。

<a id="case-ramsey-001"></a>
## T2 Ramsey / 001

**一个 exponential envelope 能否描述全部 delay？**

[对照图](figures/ramsey-001.pdf) · [Target CSV](data/ramsey-001.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.769$; candidate $T_2^*=36.11\,\mu s$; residual correlation $0.10$。

**Codex interpretation — 观察**：Single-frequency exponential fit：R2=0.769；residual correlation=0.10。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-002"></a>
## T2 Ramsey / 002

**较清晰 oscillation 也可能留下 correlated residual**

[对照图](figures/ramsey-002.pdf) · [Target CSV](data/ramsey-002.csv) · [Reference / 006](data/ramsey-006.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.878$; candidate $T_2^*=36.51\,\mu s$; residual correlation $0.32$。

**Codex interpretation — 观察**：可见 decaying oscillation，R2=0.878；residual correlation=0.32，仍需检查。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-003"></a>
## T2 Ramsey / 003

**一个 exponential envelope 能否描述全部 delay？**

[对照图](figures/ramsey-003.pdf) · [Target CSV](data/ramsey-003.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.700$; candidate $T_2^*=7.81\,\mu s$; residual correlation $0.48$。

**Codex interpretation — 观察**：Single-frequency exponential fit：R2=0.700；residual correlation=0.48。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-004"></a>
## T2 Ramsey / 004

**一个 exponential envelope 能否描述全部 delay？**

[对照图](figures/ramsey-004.pdf) · [Target CSV](data/ramsey-004.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.580$; candidate $T_2^*=20.56\,\mu s$; residual correlation $0.22$。

**Codex interpretation — 观察**：Single-frequency exponential fit：R2=0.580；residual correlation=0.22。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-005"></a>
## T2 Ramsey / 005

**一个 exponential envelope 能否描述全部 delay？**

[对照图](figures/ramsey-005.pdf) · [Target CSV](data/ramsey-005.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.642$; candidate $T_2^*=4.65\,\mu s$; residual correlation $0.17$。

**Codex interpretation — 观察**：Single-frequency exponential fit：R2=0.642；residual correlation=0.17。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-006"></a>
## T2 Ramsey / 006

**较清晰 oscillation 也可能留下 correlated residual**

[对照图](figures/ramsey-006.pdf) · [Target CSV](data/ramsey-006.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.878$; candidate $T_2^*=36.74\,\mu s$; residual correlation $0.37$。

**Codex interpretation — 观察**：可见 decaying oscillation，R2=0.878；residual correlation=0.37，仍需检查。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-007"></a>
## T2 Ramsey / 007

**一个 exponential envelope 能否描述全部 delay？**

[对照图](figures/ramsey-007.pdf) · [Target CSV](data/ramsey-007.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.563$; candidate $T_2^*=17.65\,\mu s$; residual correlation $0.37$。

**Codex interpretation — 观察**：Single-frequency exponential fit：R2=0.563；residual correlation=0.37。

> [!hypothesis]
> Suggested by Codex; not yet verified. Frequency / baseline drift、非 exponential dephasing 或 measurement noise；尚无唯一机制。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-ramsey-008"></a>
## T2 Ramsey / 008

**Envelope 结构超出单一 exponential model**

[对照图](figures/ramsey-008.pdf) · [Target CSV](data/ramsey-008.csv) · [Reference / 002](data/ramsey-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Recorded Ramsey fit: $R^2=0.328$; candidate $T_2^*=21.78\,\mu s$; residual correlation $0.38$。

**Codex interpretation — 观察**：Dense oscillation trace 在约 40–50 us 重新变宽；single-envelope fit 不能覆盖全部结构。

> [!hypothesis]
> Suggested by Codex; not yet verified. Multiple frequencies / beating、drift 或 readout / noise 变化；不能仅凭图确认 low-frequency noise。

**验证方向**：检查 cycle-resolved trace 与 residual；重复 acquisition；比较 fit window、envelope 与 echo。

**读图条件**：对照也有复查项；虚线仅表示包络，不是完整振荡预测。

Reference 002 或 006 也有 recorded flags；不作为无缺陷的 normal standard。模型条件、不同 runs 的 T1/T2 比较限制见主笔记。

<a id="case-rabi-001"></a>
## Rabi Oscillation / 001

**Noise-like trace 中，fitter 仍然会返回 period**

[对照图](figures/rabi-001.pdf) · [Target CSV](data/rabi-001.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.160$; coverage $10.10$ cycles; $5.9$ samples/cycle。

**Codex interpretation — 观察**：没有清晰完整 cycle；R2=0.160；每个 fitted cycle 仅 5.94 个 samples。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive / readout contrast 不足、frequency 不准或 pulse path 问题；candidate 高频也可能是 noise fitting。

**验证方向**：先验证 spectroscopy 与 readout，再重复 sweep；不能直接采用 fitted half-period 作为 pi amplitude。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-003"></a>
## Rabi Oscillation / 003

**Noise-like trace 中，fitter 仍然会返回 period**

[对照图](figures/rabi-003.pdf) · [Target CSV](data/rabi-003.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.130$; coverage $25.44$ cycles; $2.4$ samples/cycle。

**Codex interpretation — 观察**：没有清晰完整 cycle；R2=0.130；每个 fitted cycle 仅 2.36 个 samples。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive / readout contrast 不足、frequency 不准或 pulse path 问题；candidate 高频也可能是 noise fitting。

**验证方向**：先验证 spectroscopy 与 readout，再重复 sweep；不能直接采用 fitted half-period 作为 pi amplitude。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-004"></a>
## Rabi Oscillation / 004

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-004.pdf) · [Target CSV](data/rabi-004.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.967$; coverage $1.08$ cycles; $55.8$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.967；相邻 residual correlation=0.64。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-005"></a>
## Rabi Oscillation / 005

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-005.pdf) · [Target CSV](data/rabi-005.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.798$; coverage $1.06$ cycles; $56.7$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.798；相邻 residual correlation=0.24。 Orthogonal IQ variance fraction=0.13。

> [!hypothesis]
> Suggested by Codex; not yet verified. Noise、readout response 变化或额外 state contribution；IQ 几何本身不能证明 leakage。

**验证方向**：检查完整 IQ trajectory 与重复 scan；独立验证 readout，必要时增加 leakage-sensitive measurement。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-006"></a>
## Rabi Oscillation / 006

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-006.pdf) · [Target CSV](data/rabi-006.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.689$; coverage $1.69$ cycles; $35.4$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.689；相邻 residual correlation=0.52。 Orthogonal IQ variance fraction=0.11。

> [!hypothesis]
> Suggested by Codex; not yet verified. Noise、readout response 变化或额外 state contribution；IQ 几何本身不能证明 leakage。

**验证方向**：检查完整 IQ trajectory 与重复 scan；独立验证 readout，必要时增加 leakage-sensitive measurement。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-007"></a>
## Rabi Oscillation / 007

**高 fit score 不保证 period 已被测到**

[对照图](figures/rabi-007.pdf) · [Target CSV](data/rabi-007.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.959$; coverage $0.22$ cycles; $159.7$ samples/cycle。

**Codex interpretation — 观察**：Scan 仅覆盖 candidate cycle 的 0.22；period 很大部分来自 extrapolation。

> [!hypothesis]
> Suggested by Codex; not yet verified. Amplitude window 太短；局部 response 被误当作完整 sinusoid；模型可辨识性不足。

**验证方向**：在合适的控制范围内扩大 amplitude scan；观察 turning point 与 return；验证 pi endpoint。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-008"></a>
## Rabi Oscillation / 008

**高 fit score 不保证 period 已被测到**

[对照图](figures/rabi-008.pdf) · [Target CSV](data/rabi-008.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.996$; coverage $0.50$ cycles; $93.7$ samples/cycle。

**Codex interpretation — 观察**：Scan 仅覆盖 candidate cycle 的 0.50；period 很大部分来自 extrapolation。

> [!hypothesis]
> Suggested by Codex; not yet verified. Amplitude window 太短；局部 response 被误当作完整 sinusoid；模型可辨识性不足。

**验证方向**：在合适的控制范围内扩大 amplitude scan；观察 turning point 与 return；验证 pi endpoint。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-009"></a>
## Rabi Oscillation / 009

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-009.pdf) · [Target CSV](data/rabi-009.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.824$; coverage $1.66$ cycles; $36.1$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.824；相邻 residual correlation=0.95。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-010"></a>
## Rabi Oscillation / 010

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-010.pdf) · [Target CSV](data/rabi-010.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.480$; coverage $2.76$ cycles; $21.8$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.480；相邻 residual correlation=0.94。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-011"></a>
## Rabi Oscillation / 011

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-011.pdf) · [Target CSV](data/rabi-011.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.664$; coverage $3.00$ cycles; $20.0$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.664；相邻 residual correlation=0.94。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-012"></a>
## Rabi Oscillation / 012

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-012.pdf) · [Target CSV](data/rabi-012.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.512$; coverage $4.70$ cycles; $10.4$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.512；相邻 residual correlation=0.81。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-013"></a>
## Rabi Oscillation / 013

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-013.pdf) · [Target CSV](data/rabi-013.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.432$; coverage $2.88$ cycles; $20.9$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.432；相邻 residual correlation=0.95。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-014"></a>
## Rabi Oscillation / 014

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-014.pdf) · [Target CSV](data/rabi-014.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.594$; coverage $2.27$ cycles; $26.4$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.594；相邻 residual correlation=0.96。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-015"></a>
## Rabi Oscillation / 015

**Scan 未覆盖完整 cycle，period 缺乏约束**

[对照图](figures/rabi-015.pdf) · [Target CSV](data/rabi-015.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.586$; coverage $0.10$ cycles; $599.9$ samples/cycle。

**Codex interpretation — 观察**：Scan 仅覆盖 candidate cycle 的 0.10；period 很大部分来自 extrapolation。

> [!hypothesis]
> Suggested by Codex; not yet verified. Amplitude window 太短；局部 response 被误当作完整 sinusoid；模型可辨识性不足。

**验证方向**：在合适的控制范围内扩大 amplitude scan；观察 turning point 与 return；验证 pi endpoint。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-rabi-016"></a>
## Rabi Oscillation / 016

**Sinusoid 是否足以描述这个 amplitude scan？**

[对照图](figures/rabi-016.pdf) · [Target CSV](data/rabi-016.csv) · [Reference / 002](data/rabi-002.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ-projection fit: $R^2=0.894$; coverage $1.83$ cycles; $24.1$ samples/cycle。

**Codex interpretation — 观察**：IQ-projection sinusoid：R2=0.894；相邻 residual correlation=0.69。

> [!hypothesis]
> Suggested by Codex; not yet verified. Drive nonlinearity、detuning、drift 或 readout model 不适用；仅凭 residual 无法确定机制。

**验证方向**：重复同一 scan；核对 drive frequency；比较不同 amplitude window 与 pulse envelope。

**读图条件**：IQ 投影独立标准化，符号与大小不可跨案例比较。

Candidate frequency 来自 recorded audit；绘图只重建该频率下的 linear coefficients。IQ 几何异常不能单独证明 leakage。

<a id="case-spectroscopy-002"></a>
## Qubit Spectroscopy / 002

**Background 中的 fitted line 不足以确定 f10**

[对照图](figures/spectroscopy-002.pdf) · [Target CSV](data/spectroscopy-002.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.016$; step $1.00$ MHz; FWHM $1.08$ MHz。

**Codex interpretation — 观察**：Whole-scan IQ fit 的 R2=0.016；缺少清晰可复现的 single feature 证据。

> [!hypothesis]
> Suggested by Codex; not yet verified. Transition 不在窗口、drive 或 readout contrast 太弱；也可能存在很窄但尚未验证的 feature。

**验证方向**：验证 probe 与 drive path；调整 scan window；重复局部 candidate frequency，检查 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-004"></a>
## Qubit Spectroscopy / 004

**存在 feature，不等于 single-line model 已可靠**

[对照图](figures/spectroscopy-004.pdf) · [Target CSV](data/spectroscopy-004.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.682$; step $1.00$ MHz; FWHM $7.55$ MHz。

**Codex interpretation — 观察**：Single-Lorentzian IQ fit：R2=0.682；candidate FWHM=7.55 MHz。

> [!hypothesis]
> Suggested by Codex; not yet verified. Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。

**验证方向**：重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-005"></a>
## Qubit Spectroscopy / 005

**Fit score 不能补足 frequency resolution**

[对照图](figures/spectroscopy-005.pdf) · [Target CSV](data/spectroscopy-005.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.965$; step $1.00$ MHz; FWHM $0.50$ MHz。

**Codex interpretation — 观察**：Frequency step=1.00 MHz，candidate FWHM=0.50 MHz；采样不足。

> [!hypothesis]
> Suggested by Codex; not yet verified. 实际窄 resonance 或 isolated outlier；现有 grid 无法可靠区分，也不支持过高 linewidth precision。

**验证方向**：在 feature 附近使用更小 frequency step，并重复采样；比较 peak / dip 的宽度与 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-006"></a>
## Qubit Spectroscopy / 006

**存在 feature，不等于 single-line model 已可靠**

[对照图](figures/spectroscopy-006.pdf) · [Target CSV](data/spectroscopy-006.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.545$; step $1.00$ MHz; FWHM $116.37$ MHz。

**Codex interpretation — 观察**：Single-Lorentzian IQ fit：R2=0.545；candidate FWHM=116.37 MHz。

> [!hypothesis]
> Suggested by Codex; not yet verified. Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。

**验证方向**：重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-007"></a>
## Qubit Spectroscopy / 007

**Fit score 不能补足 frequency resolution**

[对照图](figures/spectroscopy-007.pdf) · [Target CSV](data/spectroscopy-007.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.265$; step $1.00$ MHz; FWHM $1.57$ MHz。

**Codex interpretation — 观察**：Frequency step=1.00 MHz，candidate FWHM=1.57 MHz；采样不足。

> [!hypothesis]
> Suggested by Codex; not yet verified. 实际窄 resonance 或 isolated outlier；现有 grid 无法可靠区分，也不支持过高 linewidth precision。

**验证方向**：在 feature 附近使用更小 frequency step，并重复采样；比较 peak / dip 的宽度与 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-008"></a>
## Qubit Spectroscopy / 008

**Scan boundary 限制了 resonance center 的判断**

[对照图](figures/spectroscopy-008.pdf) · [Target CSV](data/spectroscopy-008.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.312$; step $1.00$ MHz; FWHM $13.30$ MHz。

**Codex interpretation — 观察**：Candidate center=4.300 GHz 位于 scan 边界；不能完整观察两侧 response。

> [!hypothesis]
> Suggested by Codex; not yet verified. Feature 延伸到窗口外、多个 transitions 或 baseline 变化；边界值不是已测定的 center。

**验证方向**：扩大 frequency window 观察两侧；检查 candidate feature 的复现性与 drive-strength dependence。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-009"></a>
## Qubit Spectroscopy / 009

**Fit score 不能补足 frequency resolution**

[对照图](figures/spectroscopy-009.pdf) · [Target CSV](data/spectroscopy-009.csv) · [Reference / 010](data/spectroscopy-010.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.948$; step $1.00$ MHz; FWHM $1.85$ MHz。

**Codex interpretation — 观察**：Frequency step=1.00 MHz，candidate FWHM=1.85 MHz；采样不足。

> [!hypothesis]
> Suggested by Codex; not yet verified. 实际窄 resonance 或 isolated outlier；现有 grid 无法可靠区分，也不支持过高 linewidth precision。

**验证方向**：在 feature 附近使用更小 frequency step，并重复采样；比较 peak / dip 的宽度与 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-011"></a>
## Qubit Spectroscopy / 011

**Background 中的 fitted line 不足以确定 f10**

[对照图](figures/spectroscopy-011.pdf) · [Target CSV](data/spectroscopy-011.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.044$; step $1.00$ MHz; FWHM $2.11$ MHz。

**Codex interpretation — 观察**：Whole-scan IQ fit 的 R2=0.044；缺少清晰可复现的 single feature 证据。

> [!hypothesis]
> Suggested by Codex; not yet verified. Transition 不在窗口、drive 或 readout contrast 太弱；也可能存在很窄但尚未验证的 feature。

**验证方向**：验证 probe 与 drive path；调整 scan window；重复局部 candidate frequency，检查 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-012"></a>
## Qubit Spectroscopy / 012

**Scan boundary 限制了 resonance center 的判断**

[对照图](figures/spectroscopy-012.pdf) · [Target CSV](data/spectroscopy-012.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.065$; step $1.00$ MHz; FWHM $782.41$ MHz。

**Codex interpretation — 观察**：Candidate center=4.400 GHz 位于 scan 边界；不能完整观察两侧 response。

> [!hypothesis]
> Suggested by Codex; not yet verified. Feature 延伸到窗口外、多个 transitions 或 baseline 变化；边界值不是已测定的 center。

**验证方向**：扩大 frequency window 观察两侧；检查 candidate feature 的复现性与 drive-strength dependence。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-013"></a>
## Qubit Spectroscopy / 013

**存在 feature，不等于 single-line model 已可靠**

[对照图](figures/spectroscopy-013.pdf) · [Target CSV](data/spectroscopy-013.csv) · [Reference / 010](data/spectroscopy-010.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.618$; step $1.00$ MHz; FWHM $8.93$ MHz。

**Codex interpretation — 观察**：Single-Lorentzian IQ fit：R2=0.618；candidate FWHM=8.93 MHz。

> [!hypothesis]
> Suggested by Codex; not yet verified. Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。

**验证方向**：重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-014"></a>
## Qubit Spectroscopy / 014

**Background 中的 fitted line 不足以确定 f10**

[对照图](figures/spectroscopy-014.pdf) · [Target CSV](data/spectroscopy-014.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.033$; step $1.00$ MHz; FWHM $1.01$ MHz。

**Codex interpretation — 观察**：Whole-scan IQ fit 的 R2=0.033；缺少清晰可复现的 single feature 证据。

> [!hypothesis]
> Suggested by Codex; not yet verified. Transition 不在窗口、drive 或 readout contrast 太弱；也可能存在很窄但尚未验证的 feature。

**验证方向**：验证 probe 与 drive path；调整 scan window；重复局部 candidate frequency，检查 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-015"></a>
## Qubit Spectroscopy / 015

**Background 中的 fitted line 不足以确定 f10**

[对照图](figures/spectroscopy-015.pdf) · [Target CSV](data/spectroscopy-015.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.054$; step $1.00$ MHz; FWHM $2.01$ MHz。

**Codex interpretation — 观察**：Whole-scan IQ fit 的 R2=0.054；缺少清晰可复现的 single feature 证据。

> [!hypothesis]
> Suggested by Codex; not yet verified. Transition 不在窗口、drive 或 readout contrast 太弱；也可能存在很窄但尚未验证的 feature。

**验证方向**：验证 probe 与 drive path；调整 scan window；重复局部 candidate frequency，检查 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-016"></a>
## Qubit Spectroscopy / 016

**存在 feature，不等于 single-line model 已可靠**

[对照图](figures/spectroscopy-016.pdf) · [Target CSV](data/spectroscopy-016.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.392$; step $1.00$ MHz; FWHM $54.00$ MHz。

**Codex interpretation — 观察**：Single-Lorentzian IQ fit：R2=0.392；candidate FWHM=54.00 MHz。

> [!hypothesis]
> Suggested by Codex; not yet verified. Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。

**验证方向**：重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-017"></a>
## Qubit Spectroscopy / 017

**存在 feature，不等于 single-line model 已可靠**

[对照图](figures/spectroscopy-017.pdf) · [Target CSV](data/spectroscopy-017.csv) · [Reference / 001](data/spectroscopy-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.619$; step $1.00$ MHz; FWHM $30.87$ MHz。

**Codex interpretation — 观察**：Single-Lorentzian IQ fit：R2=0.619；candidate FWHM=30.87 MHz。

> [!hypothesis]
> Suggested by Codex; not yet verified. Background、drive-induced broadening、多个 response 或 drift；线形不匹配不能唯一归因。

**验证方向**：重复并局部细扫；比较 drive strength；保留 IQ 和 phase，检查两侧 background。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-spectroscopy-018"></a>
## Qubit Spectroscopy / 018

**Fit score 不能补足 frequency resolution**

[对照图](figures/spectroscopy-018.pdf) · [Target CSV](data/spectroscopy-018.csv) · [Reference / 010](data/spectroscopy-010.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；IQ single-line diagnostic: $R^2=0.929$; step $1.00$ MHz; FWHM $1.05$ MHz。

**Codex interpretation — 观察**：Frequency step=1.00 MHz，candidate FWHM=1.05 MHz；采样不足。

> [!hypothesis]
> Suggested by Codex; not yet verified. 实际窄 resonance 或 isolated outlier；现有 grid 无法可靠区分，也不支持过高 linewidth precision。

**验证方向**：在 feature 附近使用更小 frequency step，并重复采样；比较 peak / dip 的宽度与 reproducibility。

**读图条件**：图示幅度；指标来自 IQ 投影的单洛伦兹线形拟合。

低 whole-window fit score 不排除真实窄 feature；高 fit score 不能补足采样分辨率。图的 magnitude 与指标拟合的 IQ projection 是不同 observable。

<a id="case-readout-002"></a>
## GMM Readout Clusters / 002

**Preparation label 不等于可可靠区分的 state**

[对照图](figures/readout-002.pdf) · [Target CSV](data/readout-002.csv) · [Reference / 009](data/readout-009.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Held-out linear classifier: balanced accuracy $62.12\%$; not original GMM fidelity。

**Codex interpretation — 观察**：Held-out linear balanced accuracy = 62.12%；nominal preparation groups 重叠。

> [!hypothesis]
> Suggested by Codex; not yet verified. Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。

**验证方向**：先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。

**读图条件**：预测准备标签；包含状态准备与弛豫的影响。

这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。

<a id="case-readout-003"></a>
## GMM Readout Clusters / 003

**Preparation label 不等于可可靠区分的 state**

[对照图](figures/readout-003.pdf) · [Target CSV](data/readout-003.csv) · [Reference / 009](data/readout-009.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Held-out linear classifier: balanced accuracy $59.67\%$; not original GMM fidelity。

**Codex interpretation — 观察**：Held-out linear balanced accuracy = 59.67%；nominal preparation groups 重叠。

> [!hypothesis]
> Suggested by Codex; not yet verified. Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。

**验证方向**：先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。

**读图条件**：预测准备标签；包含状态准备与弛豫的影响。

这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。

<a id="case-readout-004"></a>
## GMM Readout Clusters / 004

**Preparation label 不等于可可靠区分的 state**

[对照图](figures/readout-004.pdf) · [Target CSV](data/readout-004.csv) · [Reference / 009](data/readout-009.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Held-out linear classifier: balanced accuracy $70.73\%$; not original GMM fidelity。

**Codex interpretation — 观察**：Held-out linear balanced accuracy = 70.73%；nominal preparation groups 重叠。

> [!hypothesis]
> Suggested by Codex; not yet verified. Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。

**验证方向**：先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。

**读图条件**：预测准备标签；包含状态准备与弛豫的影响。

这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。

<a id="case-readout-005"></a>
## GMM Readout Clusters / 005

**接近 screen threshold：需要检查，但不宜二分判错**

[对照图](figures/readout-005.pdf) · [Target CSV](data/readout-005.csv) · [Reference / 009](data/readout-009.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Held-out linear classifier: balanced accuracy $74.48\%$; not original GMM fidelity。

**Codex interpretation — 观察**：Balanced accuracy = 74.48%，略低于本地 75% screen threshold；threshold 不是物理定律。

> [!hypothesis]
> Suggested by Codex; not yet verified. Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。

**验证方向**：先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。

**读图条件**：预测准备标签；包含状态准备与弛豫的影响。

这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。

<a id="case-readout-008"></a>
## GMM Readout Clusters / 008

**Preparation label 不等于可可靠区分的 state**

[对照图](figures/readout-008.pdf) · [Target CSV](data/readout-008.csv) · [Reference / 007](data/readout-007.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Held-out linear classifier: balanced accuracy $61.70\%$; not original GMM fidelity。

**Codex interpretation — 观察**：Held-out linear balanced accuracy = 61.70%；nominal preparation groups 重叠。

> [!hypothesis]
> Suggested by Codex; not yet verified. Preparation pulse 不准；probe setting 不合适；measurement 期间 relaxation；measurement chain noise。

**验证方向**：先验证 preparation / Rabi，再检查 probe frequency、integration window 和 demodulated time trace。

**读图条件**：预测准备标签；包含状态准备与弛豫的影响。

这里的 accuracy 来自 held-out linear classifier，不是原始 GMM fidelity。相同 qubit 仍不保证所有 settings 匹配。

<a id="case-resonator-006"></a>
## Resonator Spectroscopy / 006

**First-point spike 是 resonance 还是 acquisition transient？**

[对照图](figures/resonator-006.pdf) · [Target CSV](data/resonator-006.csv) · [Reference / 001](data/resonator-001.csv)

**来源与诊断**：0918 packaged CSV 与 recorded audit；Descriptive screen only: window 6.000--6.130 GHz; no validated transfer-function fit。

**Codex interpretation — 观察**：Scaled magnitude 首点约 1728，次点约 66，后续 median 约 41；窗口内无 resolved interior resonance。

> [!hypothesis]
> Suggested by Codex; not yet verified. Settling / acquisition discontinuity、edge / out-of-window resonance，或 useful signal 不足。

**验证方向**：加入 settling 后重测首点；反向 sweep；扩大窗口并同时检查 phase / IQ。

**读图条件**：此处为曲线观察，尚无经过验证的传输函数拟合。

原 scaled magnitude 首点约 1728、次点约 66、后续 median 约 41；图显示除以 1000 后的相同数据。不同 case 的 scale / settings 独立；多个 features 本身不构成错误。
