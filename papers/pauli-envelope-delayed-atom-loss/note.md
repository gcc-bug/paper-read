---
type: paper
title: "Low-Overhead Surface Code with Delayed Atom-Loss Detection via Pauli Envelope"
authors:
  - Pengyu Liu
  - Shi Jie Samuel Tan
  - Eric Huang
  - Umut A. Acar
  - Hengyun Zhou
  - Chen Zhao
year: 2026
status: reading
source: "https://arxiv.org/abs/2603.04156v3"
original_filename: "2603.04156v3.pdf"
provenance: "Downloaded from https://arxiv.org/pdf/2603.04156v3 on 2026-10-10; arXiv v3 dated 2026-10-05."
reading_dates: [2026-10-10, 2026-10-12]
---

# Low-Overhead Surface Code with Delayed Atom-Loss Detection via Pauli Envelope

## Source and reading coverage

[Source PDF](source.pdf) — arXiv:2603.04156v3, 33 PDF pages.

2026-10-10: Reading discussion started. Codex consulted the abstract and main text (Sections I–VIII, PDF pages 1–13), the readout-error extensions in Appendices C.5 and D.3, and selected solver-timeout details in Appendix M.2. Definitions and Figures 5–9 were checked against rendered PDF pages 5, 7, and 8. Main-text PDF page indices match printed page labels. Appendix proofs have not been systematically checked.

2026-10-12: Discussion consolidated by content at the reader's request. Sections II–VII were revisited, together with selected statements and arguments in Appendices C.5, D.3, F, G, L, and M.1–M.2. Appendix F, Definition 6 and Theorems 7–8, were checked for correction without loss-location reports; the theorem page was also visually inspected. Figure 7(b,c) was inspected to clarify shuttling and syndrome-extraction validity. The note summarizes the completed discussion, not a complete proof audit; `status: reading` is retained because appendix proofs have not been systematically checked. No code was reproduced or experiment independently run.

### Supporting-reference consultation, 2026-10-12

These are supporting references for checking the selected paper's hardware assumptions, not separate paper-reading targets.

- Chiu et al., *Continuous operation of a coherent 3,000-qubit system*, Nature 646, 1075–1080 (2025), DOI [10.1038/s41586-025-09596-6](https://doi.org/10.1038/s41586-025-09596-6). [Publisher PDF](references/continuous-operation-coherent-3000-qubit-system.pdf), 22 PDF pages. Original download filename: `s41586-025-09596-6.pdf`; downloaded from `https://www.nature.com/articles/s41586-025-09596-6.pdf` on 2026-10-12. Consultation was limited to relevant passages on imaging, qubit manipulation/readout, and the main-text pointer to the complementary loss-resolving-readout experiment. Publisher HTML was consulted alongside locally extracted PDF text; this is not a full reading.
- Bluvstein et al., *A fault-tolerant neutral-atom architecture for universal quantum computation*, Nature 649, 39–46 (2026), DOI [10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5). [Publisher PDF](references/fault-tolerant-neutral-atom-architecture.pdf), 30 PDF pages. Original download filename: `s41586-025-09848-5.pdf`; downloaded from `https://www.nature.com/articles/s41586-025-09848-5.pdf` on 2026-10-12. Detailed consultation: Fig. 1b (PDF page 2, printed page 40), Methods “Spin-to-position conversion with a 1D optical lattice” (PDF page 10), and Methods “Decay to Rydberg P states” and “Loss detection for improved QEC” (PDF page 12). PDF pages 2, 10, and 12 were rendered and visually checked. Methods pages have no printed page labels. Selected HTML passages on the imaging histogram, measurement/re-initialization timing, and simulation procedure were also consulted. No full-paper reading is claimed.
- [Supplementary Information for Bluvstein et al.](references/fault-tolerant-neutral-atom-architecture-supplement.pdf), 55 PDF pages. Original download filename: `41586_2025_9848_MOESM1_ESM.pdf`; downloaded on 2026-10-12 from `https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-025-09848-5/MediaObjects/41586_2025_9848_MOESM1_ESM.pdf`. Only a text search for readout/loss-identification calibration terminology was performed; the supplement has not been read systematically.

The selected paper's Algorithm 1 / Eqs. (3)–(6), Mid-SWAP Figures 7–8, and Appendix M.1 sampling procedure were revisited for this discussion. Source bytes were preserved for all supporting PDFs. Supporting-reference findings below are limited to these consulted passages.

## Source claims

### Problem and physical model

The paper studies delayed atom-loss detection in alkali-atom architectures, primarily using rotated surface codes. Loss is learned at eventual measurement, rather than at the moment it occurs. A report identifies the measured atom as lost but leaves its loss time uncertain. Loss can persist through several interactions, so the circuit must periodically measure and replenish every physical atom, including atoms carrying data. (Sections I–II, pp. 1–4.)

In the paper's ideal loss model, all subsequent gates involving a lost atom are removed. Gates not involving it remain present. Several losses do not generally compose by XORing their individually observed detector patterns: removing one gate changes how other faults propagate. Figure 3 gives a small nonlinear-composition example. This is the difficulty that a standard independent Pauli detector error model does not directly capture. (Section II, pp. 3–4.)

The model has three-outcome readout, `0`, `1`, or `lost`. A missing binary measurement bit is assigned a uniformly random bit when computing detectors and logical observables; the loss flag is supplied separately. The main distance results assume perfect loss flags. The paper describes measurement as destructive and the end of an atom's life cycle, with measured atoms discarded. The experimental meaning of destruction and reuse needs the distinction discussed below. (Sections II–III, pp. 3–5.)

The ideal gate-removal model and the simulation's additional noise are separate layers. Section VII.A includes ordinary circuit-level depolarizing noise; Appendix M.1 explicitly says that an atom whose partner is lost undergoes an idling error. The simulation therefore does not leave the surviving partner noise-free, but it does not derive a general conditional partner channel from Rydberg-pulse physics. (pp. 11, 32.)

### Pauli envelope: objects, construction, and guarantee

The formal objects are:

| Object | Meaning |
| --- | --- |
| \(C\) | Original Clifford circuit, with its scheduled gates retained |
| \(p\) | Pauli fault configuration: operators assigned to faulty space-time locations |
| \(\ell\) | Physical loss history: which atoms are lost and at which space-time locations |
| \(r=R(\ell)\) | Observed loss-location report, assuming perfect reporting |
| \(L(r)=\{\ell:R(\ell)=r\}\) | Loss histories compatible with that report |
| \(D\) | Detector outcomes; for repeated checks, commonly changes between consecutive measurements |
| \(O\) | Logical-observable flip to be predicted by the decoder |
| \(S(p,\ell)\) | All detector–logical pairs \((D,O)\) with nonzero probability for the specified faults |

Definition 2 calls a set \(E(r)\) of Pauli configurations an envelope when, for every additional Pauli configuration \(p\),

\[
S(p,L(r))\subseteq S(p\oplus E(r),\varnothing).
\]

Here \(\varnothing\) means no loss, and \(p\oplus E=\{p\oplus e:e\in E\}\). The right-hand circuit is the original circuit with hypothetical Pauli insertions. The loss histories themselves are not elements of this Pauli set. The guarantee covers both detector and logical outcomes, including when ordinary Pauli faults are also present. (Section III.A, Definition 2, pp. 4–5.)

This is support inclusion, not equality of physical probability distributions. Definition 4 counts an envelope as failing if **any** covered outcome is decoded incorrectly, rather than averaging over its hypothetical Pauli configurations. Lemma 1 and Theorem 1 then give a sufficient decoding condition and the bound \(P_{\mathrm{LER}}\le P_{\mathrm{fail}}\). (p. 5.)

For circuits generated by CZ, H, and S, Lemma 2 constructs a single-history envelope by permitting Pauli operators at the loss location, after subsequent H gates on that atom, and just before its measurement. With \(\Pi_i=\{I,X,Y,Z\}\) at location \(i\), the construction is \(\Pi_1\oplus\cdots\oplus\Pi_k\). Lemma 3 composes envelopes for multiple losses and takes a union over uncertain loss times. The construction is compatible with CNOT circuits by compiling CNOTs into CZ and H. (Section III.B, p. 6.)

For one reported atom,

\[
E(r)=\bigcup_{\ell\in L(r)}E(\ell).
\]

For several reported atoms, their single-atom envelopes compose as Pauli sets. This composable bounding construction is what avoids having to characterize every nonlinear multi-loss outcome distribution exactly. Figure 4 illustrates a data-atom loss with five candidate loss locations. (Lemmas 2–3 and Example 1, p. 6.)

### Mid-SWAP: design and loss propagation

The earlier SWAP syndrome-extraction approach exchanges physical data and ancilla roles at the end of a round and thereby eventually measures each physical atom. The paper analyzes it and introduces Mid-SWAP, moving the atom-shuttling step to immediately after the first CNOT layer in each round. The remaining CNOT interactions retain their schedule. This is a new circuit design in this paper, building on prior replenishment techniques. (Section IV, pp. 6–8; Figs. 5–8.)

In Figure 7(b), the red line follows a **physical atom**, while wire labels identify circuit sites. The tracked atom participates at ancilla site \(Z_1\) at tick 1, moves to data site \(D_1\) for ticks 2–4, moves back after tick 5, and serves as an ancilla for ticks 6–8 before measurement. Figure 7(c) supplies the local circuit identity that makes the role exchange compatible with the intended syndrome extraction.

The useful distinction is in the atom's life cycle. In the earlier SWAP schedule, one early loss can have both a data-error component and an ancilla hook-error component. In Mid-SWAP, the ordering bounds one loss to **either** a data error **or** a hook error, not both in the sector analyzed. A hook error is a correlated data error arising from propagation through an ancilla's sequence of interactions. (Section IV.B, Fig. 8 and Lemma 4, pp. 7–9.)

The paper attributes the earlier SWAP circuit's limitation to this combined propagation and gives loss distance \(d_{\mathrm{loss}}\sim d/2\), even with Envelope-MLE, versus \(\sim d\) for Mid-SWAP plus Envelope-MLE. This is a circuit–decoder comparison, not a decoder-only result. (Section IV.A and Appendix B.2; Table I.)

Figure 9 describes the resulting restricted detector-pattern families. In the logical-Z decoding sector, one reported Z-ancilla loss can select at most one of three spatial detector pairs forming a Z-shaped path; an X-ancilla loss has a fixed spatial pair or none. The logical-X sector is handled symmetrically. These restrictions connect the circuit design to decoder constraints and distance proofs. (Lemma 4, pp. 8–9.)

The claimed equal space-time cost uses the circuit accounting in Table I: qubit count times duration of a syndrome-extraction round, relative to standard rotated surface-code extraction. It is not a measured complete hardware wall-clock cost. Section VII.A also alternates gate order between rounds so that boundary atoms are replenished; a fixed order would leave some boundary atoms unrefreshed. (Table I, p. 2; Section VII.A, p. 11; Appendix L.)

### Decoders: Envelope-MLE and Envelope-Matching

MLE means maximum-likelihood estimation. Algorithm 1 chooses the most likely **joint fault configuration under its independent Pauli-envelope model**. It does not claim exact maximum likelihood for the microscopic physical loss distribution, or a sum over every fault configuration in a logical equivalence class. (Section V, pp. 9–10.)

Let \(y_i\in\{0,1\}\) select ordinary Pauli mechanism \(i\), and \(x_{m,j}\in\{0,1\}\) select envelope outcome pattern \(j\) for measured atom \(m\). Preprocessing records each pattern's detector vector and logical flip, \((D_{m,j},O_{m,j})\). Given observed detector vector \(s\) and loss flags \(r\), the decoder solves:

\[
\begin{aligned}
\min_{x,y,z}\quad &\sum_i w_i y_i+\sum_{m,j}\lambda_{m,j}x_{m,j}\\
\text{subject to}\quad
&\sum_iD_{i,u}y_i+\sum_{m,j}D_{m,j,u}x_{m,j}-2z_u=s_u
&&\text{for every detector }u,\\
&\sum_jx_{m,j}=r_m
&&\text{for every measured atom }m,\\
&x_{m,j},y_i\in\{0,1\},\quad z_u\in\mathbb Z.
\end{aligned}
\]

The integer \(z_u\) is a standard linear encoding of the paper's modulo-2 detector constraint. The weights are

\[
w_i=-\log\frac{p_i}{1-p_i},\qquad
\lambda_{m,j}=-\log\Pr[(D_{m,j},O_{m,j})\mid r_m=1].
\]

The envelope-pattern probabilities use the loss probabilities of candidate times, with the envelope's Pauli operators weighted uniformly. These are probabilities in the chosen surrogate model. Exactly one **aggregate outcome pattern**, which may have zero detector flips, is selected per reported lost atom. It is not necessarily one single-qubit Pauli insertion. After optimization,

\[
O_{\mathrm{pred}}=
\bigoplus_i y_i^*O_i\;\oplus\;
\bigoplus_{m,j}x_{m,j}^*O_{m,j}.
\]

These are Algorithm 1 and Eqs. (3)–(6), p. 9, with the parity constraint rewritten as a linear equality. MILP means mixed-integer linear programming.

The exclusivity constraint prevents explaining a syndrome by freely combining several mutually exclusive patterns for the same reported atom. The paper identifies the absence of this constraint, and direct linear combination of individual physical loss patterns, as weaknesses of Average-MLE. The envelope's composition property addresses the latter while retaining a covering guarantee. (Section V, pp. 9–10.)

Envelope-Matching is a cheaper minimum-weight perfect matching (MWPM) approximation. It reweights edges associated with reported losses to a finite fraction of ordinary Pauli edge weights, discouraging selection of multiple loss edges without enforcing the full MILP exclusivity constraint. Algorithm 2 uses \(0.5w\) for spatial edges and \(0.25w\) for temporal edges in its stated construction; evaluation additionally tunes hyperparameters. Its distance guarantee is weaker than Envelope-MLE's. (Section VI, pp. 10–11; Appendix J.)

### Guarantees: what is proved and what depends on the code

The principal results concern the specified rotated surface code, gate ordering, loss/replenishment model, and decoder. Code distance alone does not determine them for an arbitrary code or circuit.

| Result | Statement | Scope |
| --- | --- | --- |
| Theorem 1 | \(P_{\mathrm{LER}}\le P_{\mathrm{fail}}\) | Correctly covering Pauli envelope; a conservative upper bound |
| Theorem 2 | Envelope-MLE succeeds if \(n_l+2n_p<d\) | Mid-SWAP; perfect reports; small-error/minimum-Pauli-count limit |
| Theorem 3 | \(d_{\mathrm{loss}}\sim d\) | Independent loss and Pauli noise; Mid-SWAP plus Envelope-MLE |
| Lemma 6 and Theorem 4 | Matching failure requires \(2n_p+1.5n_l\ge d\); \(d_{\mathrm{loss}}\sim2d/3\) | Stated graph/weight assumptions and independent-noise analysis |
| Appendix F, Theorem 7 | Correct \(\lfloor(d_h-1)/2\rfloor\) losses without loss-location reports | Mid-SWAP construction; hook-error distance \(d_h\) |
| Appendix F, Theorem 8 | Correct \(n_l<d_s\) losses with reports | Segment-hook distance \(d_s\) |

Theorem 2 is an error-count condition, and the paper supplies an indistinguishability construction at its boundary to establish tightness. It is not by itself a stochastic threshold theorem. Theorem 3 adds independent-noise assumptions and a counting argument to obtain suppression as distance increases. (pp. 9–11; Appendices C–D.)

Definition 1 defines loss distance through a uniform small-error bound with a distance-independent \(p_{\mathrm{th}}>0\):

\[
P_{\mathrm{LER}}=O\!\left[p_{\mathrm{th}}^{-d}
\left(p_{\mathrm{loss}}^{d_{\mathrm{loss}}}+p_{\mathrm{Pauli}}^{d/2}\right)\right].
\]

The definition includes mixed loss–Pauli terms. The notation \(\sim d\) and \(\sim2d/3\) is used up to additive constants; it is not an exact finite-distance numerical prediction. The paper simplifies the Pauli exponent from \((d+1)/2\) to \(d/2\) for this uniform bound. (Definition 1, p. 4.)

Appendix F defines \(d_h\) as the minimum number of hook errors and ordinary single-qubit errors needed for a logical operator, and \(d_s\) using segment-hook errors. For the rotated surface-code construction the authors state \(d_h=d_s=d\). Thus the pure-loss count comparison is:

| Loss reports | Guaranteed correctable losses | Example at \(d=9\) |
| --- | --- | --- |
| No location reports | \(\lfloor(d-1)/2\rfloor\) | 4 |
| Location reports available | Up to \(d-1\) | 8 |

These are the stated count guarantees, not thresholds, not arbitrary mixed-noise guarantees, and not demonstrations of a real-time implementation. They retain the circuit's bounded-lifetime/replenishment assumptions. (Appendix F, pp. 26–27; continuation on p. 27 states \(d_s=d_h=d\).)

### Imperfect reports and no reports

Appendices C.5 and D.3 propose report-aware extensions. For an unreported atom, the MLE extension relaxes \(\sum_jx_{m,j}=0\) to \(\sum_jx_{m,j}\le1\) and adds a penalty for a hidden-loss hypothesis. Theorem 5 preserves loss-distance scaling under its specified independent error assumptions: physical loss and missed detection each scale with \(p_{\mathrm{loss}}\), so an undetected loss has probability of order \(p_{\mathrm{loss}}^2\). (Appendix C.5, p. 22; Appendix D.3.)

Those modified decoders were not used in the numerical evaluation. Section VII.A instead feeds noisy reports to the original decoders, testing robustness rather than the guarantees of the modified algorithms. Completely absent reporting is different from rare independent missed detection and cannot inherit the stronger exponent by this argument. (pp. 11, 22.)

### Evidence: simulations, experimental re-decoding, and runtime

**Simulation model and procedure.** Section VII.A uses circuit-level depolarizing noise, losses sampled after operations, and noisy loss reports. For two-qubit gates, each atom is independently lost with probability \(p_{\mathrm{loss}}/2\). The noise parameterization is

\[
p_{\mathrm{readout}}=p_{\mathrm{loss}}=p\eta,\qquad
p_{\mathrm{Pauli}}=p(1-\eta).
\]

False-loss and missed-loss reports each have the specified probability \(p_{\mathrm{readout}}/2\). The paper sets \(p_{\mathrm{Pauli}}=10^{-9}\) at \(\eta=1\) to avoid divergent numerical weights. Thus its evaluation label “pure loss” does not imply that all loss reports are perfect. It performs \(3d\) extraction rounds. (p. 11.)

Stim does not simulate atom loss natively in this work. Appendix M.1 samples a physical loss history, removes the affected gates, inserts Pauli/idling noise, and samples the resulting Clifford circuit with gauge-detector handling. Missing measurement bits are masked so they do not reveal information beyond the supplied loss report. To reduce recompilation cost, it samples two Pauli shots per sampled loss configuration, introducing a small correlation between those paired shots. (p. 32.)

**Matched circuit/decoder comparisons.** The reported pure-loss fitted thresholds are:

| Circuit | Average-MLE | Envelope-MLE |
| --- | --- | --- |
| Earlier SWAP | 3.35% | 3.89% |
| Mid-SWAP | 4.18% | 4.75% |

Changing only the circuit or only the decoder improves the threshold; combining both gives the reported approximately 42% increase. These are fitted circuit-level simulation results under the stated noise model. Figure 10's threshold fitting uses \(d\in\{5,7,9\}\); other distance-fit evaluations include \(d=11\). A fitted low-error slope \(d_{\mathrm{eff}}\) is not identical to the asymptotic theorem exponent at every finite size or error rate. (Sections VII.A–B, Fig. 10, pp. 11–12; finite-size discussion in Appendix M.)

Envelope-Matching plus Mid-SWAP improves the corresponding matching comparison from 3.42% to 4.38%. The paper also evaluates repeated transversal logical CNOT circuits, providing evidence beyond a memory experiment within its simulation model. (Sections VII.D–E, p. 13; Figs. 12–13.)

**Experimental data.** Section VII.C re-decodes data from reference [10], rather than demonstrating a newly implemented physical Mid-SWAP circuit. It reports an error-suppression factor improvement from \(1.69\pm0.08\) to \(2.01\pm0.11\) for the standalone MLE comparison, and from \(2.14\pm0.13\) to \(2.24\pm0.14\) in a hybrid with a machine-learning decoder. Figure 11 defines the factor using the ratio of per-round logical error rates at \(d=3\) and \(d=5\). These are reported estimates on existing hardware data; the small hybrid gain and uncertainties should remain visible. (pp. 12–13.)

**Runtime evidence.** Each simulated MLE shot is one Gurobi MILP, with a 60-second limit and a 1% relative optimality gap. Across most \(d=9\) runs, fewer than 0.02% of shots reach that limit; near-threshold Mid-SWAP/Envelope-MLE is an exception at approximately 1.2%. Increasing the limit to 300 seconds on 200,000 cached near-threshold shots eliminates limit hits and changes only five logical failures, which the authors describe as statistically insignificant. These checks address the effect of the solver limit on their numerical results. The cap is not the mean decoding time. (Appendix M.2, p. 32.)

### Physical readout, reuse, and leakage: findings from supporting references

Reference [10] uses spin-to-position conversion. It transfers the computational states to levels with different responses to a state-selective optical lattice, pins one state, moves the other approximately \(2\,\mu\mathrm m\), and images the positions. One occupied position represents one qubit outcome, the other represents the other outcome, and neither occupied position indicates loss. This is eventual loss-resolving measurement using additional optical control and camera imaging, not continuous loss monitoring. (Fig. 1b, PDF p. 2; Methods “Spin-to-position conversion with a 1D optical lattice,” PDF p. 10; “Loss detection for improved QEC,” PDF p. 12.)

The experiment retains atoms for reuse after reinitialization. The readout destroys the measured qubit's unknown coherence, but does not intentionally remove every measured atom. This is a correction to describing “destructive” as necessarily destroying the physical atom. Continued computation requires resetting/repreparing the measured atom and preserving or transferring the information that is still needed elsewhere. It is not continued use of the same unknown measured state. (Reference [10], Fig. 1b and Methods, PDF pp. 2, 10, 12.)

The reported readout errors are 0.87(7)% for the dark state, 0.05(5)% for the bright state, and 0.24(2)% readout-associated loss. The last number is not a measured probability of missing an already lost atom. The inspected passages and limited supplement search did not establish a separate complete calibration of false-loss and missed-loss reports. The mechanism is experimentally supported; perfect reporting is not established by these numbers. (Reference [10], Methods, PDF p. 10.)

Reference [10] explicitly distinguishes three leakage processes:

| Event | Effect and observation described in the experiment |
| --- | --- |
| Atom physically leaves the trap | Turns off the CZ interaction while still applying gate error |
| Leakage to another ground-state hyperfine level | At large magnetic field, can turn off CZ like loss, but is not detected by loss detection; under their operating conditions residual off-resonant coupling can cause repeated errors |
| Population left in Rydberg levels | Can affect later gates and other sites, producing large temporal/spatial correlations |

The experiment uses low atomic density and several hundred microseconds between gates to allow Rydberg population to decay or leave the trap. It reports that Rydberg-leakage effects are not apparent under these conditions, and that at least 80% of its leakage in repeated QEC is loss. This supports a particular operating regime, not a general equivalence between leakage and gate-removing loss. (Methods “Decay to Rydberg P states” and “Leakage types with neutral atoms,” PDF p. 12.)

The selected paper explicitly excludes the heralded mid-circuit leakage case discussed for alkaline-earth atoms. Its full-text leakage passages do not supply a general model for persistent hyperfine/Rydberg leakage with state-dependent partner noise. The simulation's idling channel covers one limited partner-noise model. (Selected paper, Section II, p. 3; Section VII.A, p. 11; Appendix M.1, p. 32.)

### Source-stated limitations and outlook

The authors call for more detailed realistic hardware-noise analysis, further work beyond surface codes, decoders between exact envelope optimization and matching, and possible use of envelopes in learned decoding. Appendix F provides a general-CSS discussion, rather than establishing that the rotated surface-code numbers transfer unchanged to arbitrary codes. (Section VIII, p. 13; Appendix F.)

Appendix G's favorable correlated-loss result concerns both atoms being lost during the same two-qubit gate in its specified model. It does not establish that correlated leakage-induced partner errors are favorable. Its numerical comparison restricts loss to two-qubit gates and omits Pauli errors. (Appendix G, pp. 27–28.)

## My understanding

On the importance of the physical loss history \(\ell\):

> oh, yes. it is very important. but i miss it at first

On interpreting uncertain loss time through possible Pauli explanations:

> given some qubit loss when measurment, and we don't know when they missed, and which gates are skipped. And under such case, which pauli error could produce same dector results with probility of atom loss assumption (which contain time)

## My thoughts

> I think this work is a good one work.

> The details in real physical experiments is very improtant to check the assumption in the origin paper

On measured-state continuity:

> it is a very realted work compared with some before. the only problem is that after the measurment, the qubit can't be continusly used

On decoder scaling:

> the d is too small. those number are not clear proof of theri performance. cause with the d increase, the sureface code cost will increase as d^2. Thus a small d not meaning that it still could work without run out of time when d change

On learning from the paper's organization:

> I also wonder how this paper was organization. cause it contain so much, and be oragnized in one work. maybe it could help for my writing skills. And the technique, bound prove, numberical check is also sounds well. Maybe help my research skills.

## Codex interpretation

### What an envelope does, and what it does not do

The reader's uncertain-time description captures the central inference problem: knowing which measured atom is absent does not determine which earlier gates failed to execute. The envelope covers the resulting possible detector–logical outcomes with Pauli configurations in the intact circuit. Loss-time probabilities then contribute to the decoder's surrogate weights, but support inclusion alone does not supply exact physical probabilities.

An ordinary Pauli configuration can include fault type and fault location, for example “X on qubit p after gate g1.” An envelope is not the unrestricted set of all faults, and it is not a syndrome-equivalence class that exists first and is then merely changed by loss. It is constructed to cover the outcomes of a specified loss history or report. Enlarging compatible histories can enlarge the covering set, but one must retain the logical outcome and the quantification over additional Pauli faults.

For a teaching example, take the three-qubit repetition code with checks \(Z_1Z_2\) and \(Z_2Z_3\). Errors \(X_1\) and \(X_2X_3\) both give syndrome \((1,0)\), but their product is the logical flip \(X_1X_2X_3\). Consequently, reproducing the detector pattern alone is insufficient. This example explains the definition; it is not the paper's surface-code simulation.

### Why the Mid-SWAP circuit remains a syndrome measurement

Figure 7(c) initially looked suspicious to the reader. It is a circuit identity on a constrained input subspace, not an identity for swapping two arbitrary unknown qubits. If ancilla \(a\) starts in \(|0\rangle\) and data qubit \(q\) is \(\alpha|0\rangle+\beta|1\rangle\), then

\[
\operatorname{CNOT}_{q\to a}|0\rangle_a|\psi\rangle_q
=\alpha|00\rangle_{aq}+\beta|11\rangle_{aq}.
\]

That state is unchanged by exchanging its two registers. By linearity the identity also holds when the data is entangled with other qubits. Thus the inserted physical role exchange need not change the ideal logical circuit at that point. The state restriction is essential.

A small illustrative Z-parity measurement is:

```text
# a and q1 identify circuit sites; physical atoms exchange sites.
prepare a in |0>
CNOT(q1 -> a)
shuttle_exchange(a, q1)   # equivalent to SWAP for this ideal illustration
CNOT(q2 -> a)
measure a in Z           # measures Z(q1) Z(q2)
```

This is a teaching circuit for one ideal check, not a full noisy surface-code schedule. The benefit comes from repeated cycles and their atom life cycles: physical atoms are eventually measured/replenished, and changing the phase order limits each modeled loss to the error families used in the proof. “SWAP” here must not be automatically charged as a separately synthesized three-CNOT gate; the paper realizes the role exchange through atom shuttling. Conversely, actual movement, readout, reset, and timing costs require hardware accounting beyond the local ideal identity.

### Exact formulation, practical decoder, and scaling

The paper contributes a framework, a circuit design, two decoders, proofs, simulation comparisons, and re-analysis of existing experimental data. It is more than an analysis of a pre-existing Mid-SWAP technique. These contributions belong together because the envelope exposes propagation structure, Mid-SWAP improves that structure, and the decoder exploits its restrictions.

MILP accuracy and distance guarantees do not establish scalable decoding. The reader's objection to small-distance runtime evidence is justified. A distance-d surface-code layout has spatial size of order \(d^2\); with the paper's \(3d\) rounds, the space-time measurement/fault data scale at least on the order of \(d^3\), before envelope preprocessing and optimization overhead. This is an input-size observation, not a proven runtime exponent for the MILP.

Different sampled loss histories produce different modified Stim circuits. That is the sampling procedure, not extra knowledge supplied to the decoder: the hidden true history is not handed to Envelope-MLE. Its report-dependent envelope families cover compatible histories. A statement that every history produces a separately supplied exact DEM would go beyond the described procedure and confuse the simulation's internal knowledge with the decoder's observations.

The reported time-limit study supports robustness of the fitted numerical conclusions at the tested sizes. It does not supply latency distributions, memory scaling, sustained throughput, or a real-time deadline guarantee at much larger distances. Envelope-Matching is the practical approximation offered by the paper, with a weaker protection guarantee; its existence does not prove that Envelope-MLE will scale.

### No reports, imperfect reports, and leakage are different problems

Without loss flags, syndromes still contain useful error information. A decoder can correct some unlocated loss-induced patterns without uniquely determining which atom was physically lost. Appendix F already establishes a no-report count guarantee, so the basic possibility question is answered within the paper's model.

However, setting every \(r_m=0\) in the original Envelope-MLE forces every loss-pattern selector to zero. That does not implement the no-report theorem. One needs a model/decoder that permits hidden-loss patterns. The rare-missed-report extension offers one mechanism, but with no detector at all the missed-detection probability conditioned on a loss is 1, and the hidden-loss probability is order \(p_{\mathrm{loss}}\), not order \(p_{\mathrm{loss}}^2\).

Likewise, “no loss flag” and “no physical ability to refresh absent sites” are different. Periodic fresh initialization/replenishment still has to bound fault persistence. The paper's theorem does not cover an absent site that remains unrefreshed indefinitely.

A present but leaked atom can differ in both observation and dynamics. If it simply disables later gates, unreported-loss reasoning may be relevant after checking readout and refresh assumptions. If it continues to corrupt partners, one event creates a different, possibly correlated fault family. The paper's original envelope and distance proof cannot be assumed to cover that family just by changing a scalar error rate.

> [!hypothesis]
> Suggested by Codex; not yet verified. A leakage-history envelope could include the partner errors caused by that history. To make this useful, first obtain an experimentally supported conditional channel or a conservative covering fault family, then check whether its effects remain local and bounded through replenishment. Re-establish support inclusion, distance, and decoder cost. The current paper does not prove this extension, and its novelty has not been checked.

### Research and writing lessons

The transferable lesson is a dependency between contributions, not the authors' documented discovery chronology:

```text
physical bottleneck and observation model
    -> representation that makes the difficulty analyzable
    -> circuit intervention derived from that representation
    -> decoder exploiting the new structure
    -> guarantee and its failure boundary
    -> cheaper approximation with an explicit tradeoff
    -> matched evidence for effectiveness, attribution, and limits
```

The representation is valuable because it guides design as well as proof. Mid-SWAP addresses a particular propagation mechanism; exclusivity addresses a particular decoding ambiguity. The exact formulation supplies a strong reference and guarantee, while matching supplies a practical route. Neither “more techniques” nor “a theorem plus experiments” alone explains the coherence of the work.

| Paper section | Question it answers | Bridge to the next contribution |
| --- | --- | --- |
| II: Atom loss | What is physically assumed, and why is standard Pauli composition insufficient? | Establishes the need for a new analytical representation and a common metric |
| III: Pauli envelope | What can be preserved or bounded in a composable Pauli description? | Makes loss propagation analyzable and exposes circuit-design constraints |
| IV: Circuit design | How can the schedule reduce the harmful error family? | Supplies restricted patterns for decoding and proof |
| V: Envelope-MLE | How can a decoder enforce those restrictions, and what protection follows? | Provides a strong reference point and identifies the cost of exact constraints |
| VI: Envelope-Matching | Which structure can a cheaper decoder retain? | Creates a protection/efficiency tradeoff for evaluation |
| VII: Evaluation | Do the components help separately and together under matched conditions? | Separates effectiveness, attribution, empirical transfer, and implementation limits |

For developing a rough idea, begin with the smallest meaningful bottleneck or counterexample. Seek a representation only if it helps explain or change that bottleneck. Derive the intervention from the mechanism, choose an appropriate guarantee, and use a bounded test with support, defeat, and inconclusive outcomes. Do not force a theorem, an exact solver, or a second algorithm into every project.

For writing, organize around one central question and explain why each result enables the next. Keep assumptions and proof intuition visible; use appendices for long derivations and implementation details. Assign a distinct question to each experiment. A simulation can validate behavior under a model without validating the model's microscopic physical assumptions, and rare solver timeouts can coexist with unresolved scalability.

At the reader's request, these lessons were incorporated into the installed `review-research-ideas` and `review-and-write-technical-papers` skills on 2026-10-12, in the separate skills repository commit `7b90657` (`Improve research development and paper argument workflows`). That maintenance result is separate from this reading-note commit.

## Open questions

### Physical validity and correlated partner noise

- **Origin:** Reader's objections to the untouched-partner abstraction and to conflating loss with leakage.
- **Status, 2026-10-12:** Partly answered. The simulation includes idling noise, and reference [10] describes additional leakage mechanisms. General state-dependent partner noise and persistent leakage are not covered by the inspected model/results.
- **What would answer it:** Calibrated gate/readout behavior conditioned on trap loss, hyperfine leakage, and Rydberg leakage, including event timing, persistence, partner corruption, and spatial correlations; then a revised envelope/circuit analysis and matched numerical evaluation.

### Protection and cost with limited loss information

- **Origin:** Reader's question about a detector that cannot identify which atom is lost.
- **Status, 2026-10-12:** Basic correctability is answered by Appendix F, Theorem 7. Performance with realistic missed/false reports, inference from syndromes alone, and an operational replenishment protocol remains to be evaluated. The no-report count guarantee must not be presented as a new proposed result.
- **What would answer it:** A defined observation model and refresh protocol, a decoder that allows hidden losses, and comparisons of logical protection and computational cost. The report-aware extensions need numerical evaluation under their actual assumptions.

### Decoder scalability beyond tested distances

- **Origin:** Reader's criticism that small d and rare timeouts do not establish large-d performance.
- **Status, 2026-10-12:** Open. Appendix M.2 checks solver-limit sensitivity at tested sizes, not scalable real-time decoding.
- **What would answer it:** Runtime distributions and tails, memory, preprocessing, timeout/fallback behavior, and sustained throughput over increasing distance and temporal window, under a frozen noise model and equal accuracy/resource contract. Treat timeouts as incomplete optimization, not proof of impossibility.

### Readout calibration and complete hardware accounting

- **Origin:** Reader's request to verify the physical loss detector and concern about post-measurement reuse.
- **Status, 2026-10-12:** The spin-to-position mechanism and atom retention are supported by reference [10]. Complete false-loss/missed-loss calibration was not established in the inspected passages. Equal circuit space-time cost does not settle full operating cost.
- **What would answer it:** Separate calibrated confusion probabilities for `0`, `1`, and `lost`, plus movement, measurement, reset/cooling, refill, classical processing, and decoder timing in the intended device. Distinguish retained atoms from preserved measured quantum states.

## Important locations

For the selected paper, PDF page indices match printed page labels at the locations cited here. Reference [10]'s Methods pages are cited by PDF index because they have no printed page labels.

| Location | Use |
| --- | --- |
| Section II, pp. 3–4; Figs. 2–3 | Physical loss/observation model and nonlinear composition |
| Section III, pp. 4–6; Definitions 1–4; Lemmas 1–3 | Loss distance, formal envelope, probability-bound distinction, construction |
| Section IV, pp. 6–9; Figs. 5–9 | Earlier SWAP versus Mid-SWAP; circuit identity; exclusive propagation families |
| Section V, pp. 9–10; Algorithm 1; Eqs. (3)–(7) | MLE variables, weights, constraints, guarantee and tightness |
| Section VI, pp. 10–11; Algorithm 2 | Matching approximation and weaker distance |
| Section VII, pp. 11–13; Figs. 10–13 | Noise parameters, matched simulations, experimental re-decoding, logical circuits |
| Appendix C.5, p. 22; Appendix D.3 | Theoretical report-aware extensions; not used in numerical evaluation |
| Appendix F, pp. 26–27 | Hook/segment-hook distances; correction with and without reports |
| Appendix G, pp. 27–28 | Correlated atom-loss extension and restricted numerical model |
| Appendix L | Alternating gate order and boundary replenishment |
| Appendix M.1–M.2, p. 32 | External loss sampling with Stim; Gurobi caps and sensitivity checks |
| Reference [10], Fig. 1b, PDF p. 2; Methods, PDF pp. 10, 12 | Loss-resolving readout, atom reuse, leakage types, and residual partner effects |
