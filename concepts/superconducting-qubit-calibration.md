---
type: concept
title: "Superconducting-qubit calibration: quantities and physical meaning"
aliases: [0918 calibration guide]
---

# Superconducting-qubit calibration: quantities and physical meaning

Consolidated 2026-09-29; extended 2026-10-08. [Reading map and references](../maps/superconducting-qubit-calibration.md) · [Detailed readout figure](iq-readout-and-assignment.md) · [Hardware, signals, and calibration progression](superconducting-qubit-hardware-and-signals.md).

## Codex interpretation

The organizing question is: **what was controlled, what was observed, and which physical parameter can be inferred?** A number such as 0.8 could be a probability, a control setting, or a phase in radians. Its column, units, and estimator determine its meaning.

The 0918 folder contains 64 calibration cases in six families, totaling 57,993 nonempty numeric CSV rows. This is a collection of measurements and annotations, not one experiment or a stored quantum-state tensor. The CSVs are headerless numeric arrays. The workbooks contain supplied diagnoses and parameter estimates; those annotations are not independent ground truth.

The purpose of the physical measurements is to find operating frequencies, calibrate state rotations and readout, and characterize relaxation/coherence. A useful conceptual dependency chain is:

```text
Locate readout resonances → locate qubit transition → calibrate drive pulse
                                      ↕                    ↕
                               refine frequency ← improve readout
                                                           ↓
                                               characterize T1 and Ramsey
```

Actual calibration is iterative; this diagram is not a verified chronological reconstruction of the 64 cases.

## The recorded arrays

Columns below are in file order. A scan point is generally a summarized response, whereas a GMM row contains one IQ observation from each preparation group. Do not interpret every CSV row as one quantum shot.

| Family | Cases | Columns | Target |
| --- | ---: | --- | --- |
| Resonator spectroscopy | 6 | frequency (GHz), phase (rad), raw magnitude, scaled magnitude, I, Q | Candidate readout-resonator frequencies |
| Qubit spectroscopy | 18 | frequency (GHz), phase (rad), raw magnitude, scaled magnitude, I, Q | Candidate qubit transition frequency $f_{10}$ |
| Rabi oscillation | 16 | drive-amplitude setting, phase (rad), raw magnitude, scaled magnitude, I, Q | Pulse amplitude for a chosen rotation, especially π |
| GMM readout | 10 | index, I without π, Q without π, I with π, Q with π | Preparation-group discrimination and readout calibration |
| T1 visibility | 6 | delay (μs), P0 with π, P1 with π, P0 without π, P1 without π | Energy-relaxation time and preparation/readout contrast |
| T2 Ramsey | 8 | delay (μs), P0, P1 | Ramsey coherence time $T_2^*$ and oscillation frequency |

T1 preparation ordering is inferred from the traces and annotations; its CSVs lack explicit channel headers. GMM preparation channels are explicitly labeled by the INI files. Spectroscopy/Rabi I and Q and pulse-amplitude settings lack an absolute calibration in these records. The scaled-magnitude factor can differ between files.

The folder name `0918` is not an established acquisition date. The workbook uses source group `session_20260803`, while the GMM case-001 INI records creation on 2026-08-14. Preserve these distinct labels instead of calling all data “acquired September 18.”

## Excitation, transition frequency, and peaks or valleys

For energy eigenstates |0⟩ and |1⟩ with $E_1>E_0$,

$$
f_{10}=(E_1-E_0)/h.
$$

The states have different energies. The transition has one resonant frequency, which can drive upward or downward transitions depending on the initial state and pulse. Exciting a qubit means increasing its excited-state population, not necessarily transferring it completely to |1⟩. A pulse may create |ψ⟩ = α|0⟩ + β|1⟩ with $P_1=|\beta|^2$.

Qubit-spectroscopy case 001 reports $f_{10}=4.119$ GHz and shows an upward readout feature. Resonator-spectroscopy case 001 shows multiple dips. One transition need not produce two peaks corresponding to two states. Peak/dip polarity depends on the readout observable, resonator response, and background; it is not a universal label for excitation versus relaxation.

Spectroscopy needs a resolvable, reproducible feature and sufficient scan range/resolution. Multiple features, a clipped feature, or excessive broadening complicate parameter identification. A large peak alone does not establish which transition was driven. See Krantz Sec. V.A and Blais Sec. V.C.1/Fig. 19 for state-dependent resonator response; these describe the general mechanism, not a unique diagnosis of each local spectrum.

### 2026-10-08 clarification: anticipating peak or dip

Codex: the measurement convention and reference responses can predict feature polarity once calibrated. The target of an initial qubit-frequency scan is a reproducible state-dependent response, which may point either way. Under a linear scalar-readout model, $y=y_0+(y_1-y_0)P_1$: excitation produces a peak when $y_1>y_0$ and a dip when $y_1<y_0$. Neither sign identifies transition direction by itself. Magnitude and phase can depart from this linear model. A resonator-frequency scan probes a different scattering response, which can show a notch even with strong internal excitation. See [hardware and signal explanation](superconducting-qubit-hardware-and-signals.md#codex-interpretation-can-we-predict-peak-or-dip-before-a-scan) for examples and supporting references.

## π pulses and amplitude Rabi

A π pulse performs a π-radian (180-degree) rotation about a chosen transverse axis of the Bloch sphere. Ideally it maps |0⟩ to |1⟩ and |1⟩ to |0⟩, up to phase factors. A π/2 pulse creates a superposition from a basis state. The π is a state-rotation angle, not the value of the plotted readout phase and not the microwave carrier phase.

For an ideal resonant drive with a fixed rotation axis,

$$
\theta=\int\Omega(t)\,dt,\qquad P_1=\sin^2(\theta/2)
$$

when starting in |0⟩. Here Ω is angular Rabi frequency, in radians per unit time. Constant Ω gives θ = Ωt. Pulse phase sets the rotation axis; integrated drive strength sets the rotation angle. Krantz Sec. IV.D.1, Eqs. (92)–(94), provides the drive/rotation relation.

In this corpus, Rabi scans vary drive amplitude at a fixed pulse duration. If drive response is linear, rotation angle is proportional to that amplitude. Under the ideal model the π amplitude is half the full oscillation period measured from zero drive. A value such as `pi_amp=1.212` is a control setting, not a probability or an angle in radians.

### Why the plotted curve is not necessarily sin²

The original Rabi plots use readout `amp` (for example case 002) or `phase` (for example cases 015 and 016), not direct P1. Under a stable two-state linear readout model,

$$
\bar z(a)\approx [1-P_1(a)]z_0+P_1(a)z_1,\qquad z=I+iQ.
$$

This is a model for an **averaged measured signal**, not the qubit wavefunction. Taking magnitude or phase is nonlinear, so the displayed curve can differ from sin². Moreover, the mean of individual magnitudes is not generally the magnitude of the mean complex signal; the acquisition pipeline's averaging order matters.

Case 002 has a broad oscillation with scatter around a fit. Case 007 captures only a partial cycle. Case 015 plots phase and is titled “invalid.” A fit line does not certify its π estimate. Noise can produce scatter; structured residuals can indicate model mismatch, drift, or other effects. Without a noise model and error bars, visual distance from a curve cannot identify a cause or establish statistical rejection.

The local audit fits an IQ projection rather than blindly treating magnitude as population. Its half-period is explicitly a candidate diagnostic, not an approved control setting.

## T1: decay of excitation

The usual experiment is prepare with a π pulse, wait t, then read out; repeat to estimate P1. With stable preparation/readout and approximately stationary exponential relaxation,

$$
P_1(t)=B+A e^{-t/T_1}.
$$

At $t=T_1$, the excess above baseline B is $1/e\approx36.8\%$ of its initial value. This does not mean the measured probability must equal 0.368. A nonzero baseline and imperfect preparation change the vertical scale. See Krantz Fig. 5(a) and the Qiskit T1 tutorial's Background.

In the local figures, the presumed with-π P1 trace is blue and the low reference trace is red. The shared axis label is confusing; use CSV column mapping and the two traces together. P0 would rise during relaxation because $P_0=1-P_1$.

| Case | Initial presumed with-π P1 | Final P1 | Delay window (μs) | Observation |
| --- | ---: | ---: | --- | --- |
| 001 | 0.61875 | 0.1546875 | 0–134 | Overall decay |
| 002 | 0.91875 | 0.1234375 | 0–102 | Overall decay |
| 003 | 0.9140625 | 0.1640625 | 0–118 | Overall decay |
| 004 | 0.95625 | 0.95000 | 0–100 | Almost flat; no resolved decay |
| 005 | 0.934375 | 0.278125 | 0–100 | Noisy overall decay |
| 006 | 0.76875 | 0.090625 | 0–100 | Fast decay toward reference |

These are raw endpoint values checked on 2026-09-29, not fitted lifetimes. Case 004 does not independently establish a very long T1; sequence/acquisition problems and other explanations remain possible. Individual noisy points need not decrease monotonically. A valid T1 can exceed the scan duration, but limited decay makes its estimate sensitive to baseline and uncertainty.

The local audit fits contrast $P_1^{\pi}-P_1^{\mathrm{no\ \pi}}$ with both free and zero offsets. Workbook T1 estimates and these audit estimates may use different observables/models and should not be treated as interchangeable.

## Ramsey: coherence versus excitation

Excitation is population in |1⟩. Coherence is the maintained relative phase in a superposition. For

$$
|\psi\rangle=(|0\rangle+e^{i\phi}|1\rangle)/\sqrt2,
$$

both populations are 1/2 for every φ. If φ varies unpredictably between repetitions, ensemble interference contrast disappears without requiring a change in those populations.

Ramsey uses a π/2 pulse, free evolution, a second π/2 pulse, and readout. The second pulse converts relative phase into measurable population. A common restricted model is

$$
P_1(t)=B+A e^{-t/T_2^*}\cos(2\pi f t+\phi).
$$

If delay is measured in μs and f in MHz, ft is dimensionless; 1 MHz corresponds to a 1 μs period. The envelope lifetime and oscillation frequency are different parameters. Oscillation can include an intentional phase ramp or detuning; the observed frequency alone does not necessarily give the signed qubit-frequency correction.

Energy relaxation changes population and also damages coherence. Pure dephasing randomizes relative phase without energy exchange. Under matched stationary exponential relaxation/dephasing assumptions,

$$
1/T_2=1/(2T_1)+1/T_\phi,
$$

giving $T_2\leq2T_1$. Nonexponential Ramsey envelopes and unrelated acquisitions cannot be assessed by indiscriminately comparing their fitted time constants. Krantz Sec. III.B.2–3 and Figs. 4–5 explain these assumptions and deviations.

## Rules: identity, physical model, and intended use

| Layer | Examples | What it establishes |
| --- | --- | --- |
| Numerical identities | finite values; $0\leq P_i\leq1$; binary $P_0+P_1=1$; raw magnitude $=\sqrt{I^2+Q^2}$; phase $=\operatorname{atan2}(Q,I)$ modulo 2π | Internal consistency of the representation |
| File convention | GMM index 0…3199; correct column width; sorted scan axis | Compatibility with this corpus/parser, not a physical law |
| Model expectation | exponential relaxation, adequate oscillation sampling, stable readout response | Whether a restricted interpretation is plausible |
| Calibration acceptance | parameter uncertainty, repeatability, allowable gate/readout error, stability | Whether the result is good enough for a specified use |

I and Q can be negative; magnitudes cannot. Uncalibrated magnitudes may greatly exceed 1. Phase wrapping can create normal jumps. Binary normalization may be enforced by classification and does not establish absence of leakage. In other datasets, mitigated quasi-probabilities can fall outside [0,1]; they are not the raw probabilities tabulated here.

The local audit's flags include R² below 0.8, fewer than six samples per fitted cycle, and held-out linear balanced accuracy below 0.75. These are declared exploratory heuristics, not universal acceptance thresholds. Nyquist is a separate anti-aliasing consideration: more than two samples per period is only a necessary ideal-bandlimited criterion, not sufficient for precise finite noisy fits. This task did not rerun the audit or certify any case.

## Reader questions preserved from the discussion

The following are the reader's questions, not claims of understanding. Answers above are Codex explanations.

> can you explain here about the 'excites'?

> the \ket{0} and \ket{1} is in same frequencey? in most figure I see One big peak. while some of them in figure, only have valley

> from \ket{0} to \ket{1}?

> why i didn't see such line in the figure. And the point mostly far away from the line

> what's the \pi pulse meaning here? the \pi is in which place?

> current data seems don't show such trend

> what's difference with excitation

The questions about four-panel layout and prepared/assigned states are retained in the [readout note](iq-readout-and-assignment.md#reader-questions).

## Evidence and scope

- Raw values: [0918 data](../../agent_control/data/0918/) and its `meta_info_cn_v2.xlsx` annotation workbook. These links require the sibling checkout; the notes and downloaded reference PDFs remain readable without it.
- Implementation: [audit_raw_physics.py](../../agent_control/scripts/audit_raw_physics.py), especially `projection`, `audit_case`, and `POLICY`.
- Literature: [Krantz reference](../discussions/superconducting-qubit-calibration/references.md#a-quantum-engineers-guide-to-superconducting-qubits), [Blais reference](../discussions/superconducting-qubit-calibration/references.md#circuit-quantum-electrodynamics), and [official tutorial links](../discussions/superconducting-qubit-calibration/note.md#reading-order-and-references).

2026-09-29 — Codex consolidation: preserves the flat T1 exception, distinguishes plotted signal from population, and corrects any earlier implication that `0918` specifies the acquisition date. No reader endorsement of these explanations is inferred.
