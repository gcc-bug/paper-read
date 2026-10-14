# 量子控制软件的早期工作：配套解释

Prepared on 2026-10-13; explanatory background expanded on 2026-10-14. [完整 PDF](early-control-work-zh.pdf) · [Beamer source](early-control-work.tex) · [现有校准报告](0918-calibration-zh.pdf) · [校准报告笔记](notes.md)。本笔记供读者自己理解、备讲和回顾，保留比 slides 更详细的背景。报告的主题、字体、导航与构建说明放在后面的制作记录中。

这是供报告使用的草稿。个人职责来自读者本轮确认；代码行为来自选定的 QuantaCS commits 与实现；组织主线和机制解释为 Codex interpretation。未声称重新执行软件测试、采集物理数据或测量控制改善。

## 读者确认的工作范围

以下是读者明确确认的意思，保留为职责依据：

- QuantaCS 的目标是补偿 waveform generator 到 chip 的信号传输失真。读者只构建 compilation pipeline 中的功能；响应参数由同事提供，读者不负责其测量或拟合。
- sion 与 sion-exper 的工作同时包括电极电压序列计算和 ARTIQ 输出控制代码。
- 离子输运工作的角色是软件开发，读者没有进行物理实验。
- 本稿与现有校准 slides 一起用于报告。读者认可把控制软件工作与测量指标溯源作为相互连接的报告内容。

## 正文 1–3 页：范围与问题

第 1 页封面，第 2 页目录，第 3 页并列两类项目。共同点是将物理控制要求转成可执行的电信号；差别是 QuantaCS 接收既有响应参数进行补偿，而离子项目计算电极电压序列并组织输出。这个共同点是报告组织上的解释，不表示两个平台采用相同控制模型。

当前版本（2026-10-14）正文共 7 页：封面、目录、工作概览、预失真原理、编译集成、离子输运、接续校准报告。第 8 页为补偿模型附录。提交记录与函数细节保留在本笔记，不用于正式介绍。

## 理解背景 — 2026-10-14

以下是 **Codex interpretation**，用于解释已确认的软件职责。预失真部分沿用此前核对的代码模型；离子部分是一般电势与控制背景，不表示已经读取项目算法或证明输运性能。

### 为什么生成器的波形不等于芯片收到的波形？

生成器只控制信号链的输入。电缆、滤波器、电子学和低温线路具有带宽与暂态响应，信号经过这些元件后，可能出现边沿变缓、延迟、过冲或拖尾。目标应是器件端所需的电信号；若直接在生成器播放同形波形，器件端不一定得到目标。

预失真的思路是先根据线路模型调整输入，让线路作用后的输出更接近目标。因此补偿后的输入可能故意出现额外过冲或尾部。“输入看起来更不理想”与“模型中的输出更接近目标”并不矛盾；原有阶跃示意就是这个关系的例子。

### 线性时不变和传输函数是什么意思？

线性指输入叠加和缩放时，模型输出也按相同方式叠加和缩放。时不变指把输入延后一段时间，输出只相应延后，模型关系本身不变。这些是假设，不是每条真实线路在任意幅度、频率和时间下都严格满足的性质。

在这种模型下，输出为输入与冲激响应的卷积：

$$
y(t)=\int h(\tau)u(t-\tau)\,d\tau.
$$

$h(t)$ 描述线路对理想短冲激的响应；转到频域后，卷积变成乘法 $Y(\omega)=H(\omega)U(\omega)$。传输函数 $H$ 同时描述各频率分量的幅度和相位变化。阶跃响应是对持续阶跃输入的响应，冲激响应与阶跃响应有联系，但两者不是同一个量。

逆补偿 $U_{\mathrm{pre}}=Y_{\mathrm{target}}/H$ 是模型内的解。如果某些频率上 $H$ 很小，输入便需要很大的对应分量，可能放大噪声或超过输出幅度；有限带宽也可能让目标无法精确实现。实际还需考虑采样、窗口、模型误差和硬件约束。因此代数上写出逆，并不保证任何目标波形都可回放。

### 为什么要在编译流程中处理连续波形和边界？

有记忆的线路会把一个脉冲的影响延续到脉冲结束以后。如果每个脉冲都单独截断处理，其尾部可能被遗漏，紧随其后的等待或下一脉冲也可能受到影响。先组合一段连续的端口波形，可以在同一时间轴上表达这些响应，再生成设备执行指令。

保护采样、尾部和等待区间因而是有物理意义的边界处理，并非单纯文件格式转换。保护采样通常为有限窗口留出响应空间；它是否足够，仍取决于模型和窗口选择。读者的贡献是把这些波形计算及参数接入编译流水线；参数测量、辨识和硬件改善验证不属于已确认的职责。

### 电极电压为什么能移动离子？

带电离子受到电场力。一般离子阱利用射频场与静态电势形成束缚；具体几何和场配置随平台不同。改变分段电极电压，可以改变沿输运方向的势能形状及其最低点，让束缚位置随时间移动。这里讲的是位置控制；不能把“离子移动”与“内部量子比特态旋转”混为一谈。

在固定几何、线性静电模型下，可以先计算每个电极单位电压产生的势函数 $\phi_k(\mathbf r)$，然后叠加：

$$
\Phi_{\mathrm{DC}}(\mathbf r,t)=\sum_k V_k(t)\phi_k(\mathbf r),\qquad
U(\mathbf r,t)=q\Phi_{\mathrm{DC}}(\mathbf r,t)+U_{\mathrm{RF,eff}}(\mathbf r).
$$

$V_k$ 是第 $k$ 个电极的电压，$q$ 是离子电荷，$U_{\mathrm{RF,eff}}$ 是在相应近似下的射频有效束缚势。该式解释电压序列计算的常见物理基础，不声称 sion 或 sion-exper 使用了这一具体求解方法。

输运不仅要把最低点从 A 移到 B，还可能需要保持束缚强度、避免突然改变电势，并满足电压与更新速率限制。快速或不平滑的移动可能激发离子的运动；是否满足这些目标，需要具体算法与验证记录，当前不能写成读者已经完成的物理结果。

### 电压序列计算和 ARTIQ 控制分别完成什么？

电压计算回答“各时刻各电极应使用什么电压”；输出控制回答“怎样按指定顺序与时序把这些设置交给设备”。ARTIQ 提供实验控制程序与实时执行机制，但不能据此推断项目的 DAC 型号、通信接口或更新速率。

读者确认两类软件工作都有参与，没有参与物理实验。因此介绍可以清楚说“我参与计算电极电压序列，并编写 ARTIQ 输出控制代码”，而不声称“我在实验中降低了输运加热”。代码数值检查、执行时序检查和真实离子输运测量分别回答不同问题。

### 从这些工作转到校准报告，连接在哪里？

控制侧把物理目标转成可执行信号，测量侧把信号作用后的响应转成记录与指标。两边都需要解释软件输出与物理含义之间的关系。这个连接可以自然引出后续报告：有一个输出波形或一个拟合数字，还需要检查它是否对应预期的物理操作或参数。

备讲时应能回答：谁提供响应参数？为什么需要补偿？为什么不能只处理孤立脉冲？电压改变的是势阱的什么？软件验证与硬件实验有何不同？本笔记已经解释一般原理，项目特定的离子求解方法仍待代码材料核对。

## 背景补充：信号传输模型（对应第 4、8 页）

Codex interpretation：在线性时不变（LTI）模型中，输出频谱满足 $Y(\omega)=H(\omega)U(\omega)$。为了得到目标输出，可计算 $U_{\mathrm{pre}}=Y_{\mathrm{target}}/H$，再通过 inverse FFT 转回输入采样。这里的目标是电信号波形，不是直接求解量子态控制。

代码实现使用 supplied multi-exponential response parameters，并支持可选的 AWG response。读者的贡献是把计算及其参数接入编译流程。参数辨识、原始模型来源和硬件测量不归入已确认的个人贡献。

这个公式描述模型内的补偿关系。真实硬件还涉及模型误差、有限带宽、幅度限制、采样以及漂移，不能从公式直接宣称 gate fidelity 或芯片端波形误差改善。

## 第 4 页：示意曲线的准确含义

本页是可编辑的 PGFPlots 图，完全是说明性模型，不来自测量或执行 QuantaCS 软件。使用一个指数项、无 AWG 响应：

$$H(s)=1+\frac{ps}{s+1/\tau},\qquad p=-0.25.$$

对于从 $t=0$ 开始的单位阶跃，未补偿输出为 $1+p e^{-t/\tau}$，图中从 0.75 接近 1。解析预失真输入为

$$u_{\mathrm{pre}}(t)=1-\frac{p}{1+p}e^{-t/[(1+p)\tau]}
=1+\frac13 e^{-t/(0.75\tau)}.$$

在这个精确连续时间模型下，补偿后的输出等于目标阶跃，因此未再画与 target 重叠的第四条线。图只显示 $t\geq0$，不显示阶跃之前的零值。它与代码的单指数传输函数一致，但不是有限 FFT 窗口的回放模拟，也不是实际有限时长脉冲。其目的只是解释“为什么生成器输入反而要偏离目标”。

## 第 5 页：端口波形与编译流程

Inspected `port_wave_composer.py` 按 function 与 port 提取 pulse/wait instructions，组合采样波形，在启用 predistortion 的端口调用 `calibrate_sample_wave`，再将结果拆成非零 playback segments 和 zero wait segments。图省略配置校验、负时间 instruction 分支、可选 AWG 参数，以及不需要补偿的端口。

Codex interpretation：先处理一段连续控制序列，才能在波形层表达传输响应的时间延展。Pulse tail、guard samples 与 wait intervals 因而是集成时需要处理的边界。这里只描述 inspected code 路径，不宣称任意 control flow、跨函数状态或所有 timing constraints 已获证明。

## 调研依据：具体个人贡献

从 author `gcc-bug` 的个人提交中，提炼 waveform calculation、parameter mapping、compilation integration 和 boundary/tests 四层。未把 merge、repository-wide formatting 或导入代码全部算作个人开发。

存在测试代码可以支持“添加了测试”；本次没有执行 QuantaCS 测试，不写“所有测试通过”。软件测试与模型内 forward/inverse consistency 也不能替代独立硬件验证。

## 第 6 页：离子输运软件

本页只使用读者确认的职责：电极电压序列计算与 ARTIQ 输出代码。图表示功能关系，不声称新 transport optimizer、特定 trap geometry、DAC 型号、update rate 或 heating 改善。

当前未能读取 requested remotes：`git@gitee.com:arclight_quantum/sion.git` 与 `git@gitee.com:jelly_orange/sion-exper.git`。SSH 访问遇到 host-key verification failure；HTTPS 的 sion-exper 查询需要不可用的 credentials。没有更改 SSH trust 或 credentials。

本地 `/Users/coldcat/Coldcat/Go/code/Sion` 是带有上游 surface-ion 内容的一次 initial import，且无 remote。它不建立与 requested projects 的对应，不能据 initial commit 将其所有模拟功能归为读者贡献。未修改该 checkout 的已有删除状态。

后续可补充：电场/势阱模型、电压求解流程、复用与新增模块、ARTIQ interface、软件验证例子。无需等这些资料才介绍已确认的职责；算法细节需核对后再扩充。

## 背景补充：控制与测量的共同软件问题

Codex interpretation：控制侧把 physical target 转成 waveform/voltage 和 instructions；测量侧把 IQ records 转成 assignments 和 metrics。两侧均需要知道输入、参数、单位、变换与版本，才能说明输出含义。

这是有依据的结构比较，依赖读者确认的控制职责及现有 [readout provenance question](../../../questions/0918-readout-estimator-provenance.md)。它没有建立 QuantaCS、离子项目与校准数据来自同一次设备实验的关系。尤其不能写“我用 QuantaCS 预失真提高了这组 readout fidelity”。

> [!hypothesis]
> Suggested by Codex; not yet verified. A future integrated workflow could retain control-program versions, response parameters, acquisition settings and estimator versions in one provenance chain. Whether this can diagnose a particular error would need matched control/measurement records and independent checks; the current separate project records do not establish such a workflow.

该未来设想留在笔记，不作为现有贡献放入正文。

## 第 7 页：接续校准报告

本页接入 [《从硬件到校准判断》](0918-calibration-zh.pdf)。正文仅讲 measurement pipeline 的问题，避免重复另一份 deck 的 hardware background 与病例。

现有 [IQ readout note](../../../concepts/iq-readout-and-assignment.md) 中，显示值 $F_0=0.9634$、$F_1=0.9169$ 的平均为 0.94015，rounding 后为显示的 $F=0.9402$；visibility 对应 $F_0+F_1-1=0.8803$。这些是记录中已核对的算术关系，不恢复原始 estimator。

原始 panel coloring、IQ transform、fitter、threshold、SNR、stateErr 和 sepErr 定义仍待恢复；本次检查现有记录，没有重新做 dataset audit。局部审计的 held-out linear classifier 也不等于原始 GMM estimator。准备标签和真实逐 shot 状态应继续区分。

建议口头转场：

> 前面的工作说明，我如何把控制要求转成可执行的信号。接下来转到测量侧：这些信号作用于器件后，记录到的 IQ 如何经过软件处理变成校准指标？我们需要分清数据直接支持什么、模型诊断了什么，以及哪些原因还需验证。

这是 Codex 提供的讲述草稿，不是历史上的读者发言。

## 调研依据：QuantaCS 实现记录与第 8 页模型

Consulted on 2026-10-13；local checkout `/Users/coldcat/Coldcat/Go/code/QuantaCS`，HEAD `5a1b6e74ad867d1729ca88d6c86afa5994c70eb7`，remote `git@gitee.com:hpcl_quanta/QuantaCS.git`。检查本地 history，没有 fetch 或修改项目。Selected source coverage:

- `src/quanta_cs/execution/step_response.py`：`StepResponseSystem`、FFT inverse/forward model、`calibrate_sample_wave`、optional second-order AWG response。
- `src/quanta_cs/compilation/quiets/pyqisgen/quanta_cs/port_wave_composer.py`：guard samples、wave segmentation、composition/calibration 与生成 instructions 的路径。
- `src/quanta_cs/data_structure/device_parameter/{edge,transmon_element}.py`：predistortion 配置类型与端口转换函数；选定提交。
- `tests/pulse_calibration/{test_pulse,test_port_info,test_compose_qi_program_to_waves}.py`：测试目录、测试名称与部分选定代码；未运行。

| Commit | Date recorded in Git | Selected contribution evidence |
| --- | --- | --- |
| `14cfc4c345feb94ba7dd12620149565be97e718c` | 2025-07-17 | SampleWave calibration interface and tests |
| `30d8bb11cc64f40af346ba9f008bb0af626a63ca` | 2025-07-17 | Qubit/edge mapping and coupler predistortion parameters |
| `dae71df41ef4b6fc35faeff7078056967ff675d9` | 2025-07-18 | Port waveform composition utilities and tests |
| `8de115478cc52159b18ac0dec89f515fabd4f8ed` | 2025-07-21 | Calibrated-wave instruction integration |
| `9d7dfb4e` / `056a47f5` | 2025-11-25 | Guard / tail handling updates |
| `9e499528dd6c50cb0da661b00dbf384465b721fc` | 2026-06-02 | Optional AWG transfer function, parameter propagation and tests |

这些 selected commits 不构成所有贡献的穷举。只将 inspected change 归给对应 author，不从 commit count 推断贡献量。

当前 code 采用 $H_{\mathrm{cryo}}=1+j\omega\sum_i p_i/(j\omega+1/\tau_i)$；在同时提供 $f_n,\zeta$ 时乘上 second-order AWG response。FFT 采用 real FFT / inverse real FFT。Exact-zero transfer values 加一个 epsilon，并不构成对所有近零响应的稳定正则化保证。有限采样、窗口边界、硬件幅度与高频噪声放大均不能从代数可逆性自动保证。

第 8 页频域公式中的 $U_{\mathrm{pre}}$ 为 spectrum，执行 inverse FFT 后得到回放 samples。January 2026 history 的 polynomial terms 后来在 June update 被修改，不把旧实现与当前可选 AWG 模型同时表述为现用功能。

## 准备阶段的待核对事项（不在 slides 中展示）

补齐 ion project 的代码可把职责介绍进一步细化为具体流程与实现例子。首先需要确定 voltage calculation 的方法来源与个人修改，再检查硬件接口与验证范围。本笔记保留当前未决信息，不向听众暗示这些算法或性能已经验证。

## Build

在本目录执行 `bash compile.sh`，同时编译本报告与现有校准报告。使用相同的 repository-relative theme、logo 与 bundled fonts。分别输出完整 `early-control-work-zh.pdf` 与 `0918-calibration-zh.pdf`，各自包含正文与附录；早期工作报告的中间文件在 ignored `build/early-control-work/`。

### Delivery checks — 2026-10-13

XeLaTeX 编译成功，共 14 页；最终 log 无 overfull/underfull boxes、missing-character 或 undefined-reference warnings。保留由 repository-relative theme lookup 产生的 package-name warning。全稿已渲染并目视检查；最后修改的图例和表格另行重渲染检查。代表流程页在 854 × 480、降低对比度并轻微模糊的模拟预览中检查，非真实投影设备测量。

核对了 notes/README 的相对文件链接、PDF 页数与非空文本、正文及附录的 navigation link annotations、可见文本没有私有数据 filing label。附录处切换为独立 section navigation；正文 11 页和附录 3 页与笔记对应。这些是交付检查，不是控制软件或物理模型的性能验证。

### Native figure captions — 2026-10-13

按读者反馈，将五个 figures 的说明移入环境内的 `\caption{...}`，使用 shared theme 的统一编号和格式；核心结论继续放在正文。阶跃图的 caption 明确保留单指数模型、$p=-0.25$、精确模型下补偿输出与目标重合，以及曲线非实测的条件。职责范围与依据不变。

重新编译并渲染检查全部 14 页，图注无裁切或重叠，最终 log 无 overfull/underfull、missing-character 或 undefined-reference warnings。页码与正文/附录划分不变；此次检查不新增控制软件或物理实验的性能证据。

## 叙述压缩 — 2026-10-14

按读者认可的稿件，将主线压缩为“控制要求—个人软件工作—测量与校准”。正文只介绍已确认职责、必要原理和报告转场；函数名、提交记录、测试细节与访问限制保留在此处。移除重复贡献表、额外控制/测量比较页和指标溯源页。保留示意阶跃图、编译与输运流程图，以及补偿模型附录。

当前八页 PDF 已编译并逐页渲染检查；无排版溢出、缺字或未定义引用。正文中未再展示提交编号和函数细节，职责依据仍保存在本笔记。
