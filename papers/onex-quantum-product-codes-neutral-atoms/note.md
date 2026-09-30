---
type: paper
title: "Architecture and Compilation Co-Design for High-Rate Quantum Product Codes on Neutral Atom Arrays"
authors: [Adrian Liu, Wan-Hsuan Lin, Daniel Bochen Tan, Qian Xu, Jason Cong]
year: 2026
status: reading
tags: []
source: "source.pdf"
original_filename: "read-2608.20164v1.pdf"
provenance: "https://arxiv.org/abs/2608.20164; arXiv v1 PDF retrieved from https://arxiv.org/pdf/2608.20164v1 on 2026-09-30. Original filename records the temporary local download name."
reading_dates: [2026-09-23, 2026-09-30]
---

# Architecture and Compilation Co-Design for High-Rate Quantum Product Codes on Neutral Atom Arrays

## Source and reading coverage

[Original PDF](source.pdf), arXiv:2608.20164v1, dated 20 August 2026.

**Provisional discussion checkpoint, saved 2026-09-30 at the reader's request.** The reader is pausing for other business and intends to review these notes and continue later. The discussion is not finished. Codex explanations below have not been confirmed as the reader's understanding.

On 2026-09-23, Codex read the main text (PDF pp. 1–13) and appendices A–C (PDF pp. 14–18); references were skimmed. PDF page indices and printed page numbers coincide. Text was extracted locally. Figure 1, Figure 4, and the constraints on p. 14 were also inspected in rendered pages; the remaining figures were not comprehensively visually audited. On 2026-09-30, follow-up reading revisited the formulation and compaction in Appendix A.1–A.3, the benchmarks and formulation ablation, the zoned and lifted-product evaluations, and relevant references. No compiler implementation, solver certificates, or experimental reproduction was inspected.

The initial conversational explanation was too compressed. The reader requested the problem background and methodology, followed by questions about scheduling, initial placement, distance compaction, SMT modeling, symmetry, and comparisons. This note preserves that discussion for resumption.

## Source claims

### Problem and motivation

The authors motivate high-rate quantum LDPC codes as a way to reduce physical-qubit overhead. Their check-to-data interactions can be nonlocal on a fixed grid. Neutral-atom arrays can supply this connectivity by transporting atoms, but transport takes time and must respect AOD control constraints. In particular, channels on the same control axis cannot cross. Planning placement, gate execution, and rearrangement therefore becomes a combinatorial compilation problem (§§1–2.1, PDF pp. 1–3).

The target application is repeated syndrome extraction for quantum memory. The relevant duration is the physical execution time of a round. Compiler runtime is a separate cost. The authors argue that general 2D compilation and local constructive routing leave substantial rearrangement overhead (§1; §4.2).

### Product decomposition and pipeline

For HGP codes constructed from classical parity-check matrices H1 and H2, Eq. (1) contains tensor-product terms with identity factors. Each check-to-data edge fixes one product coordinate and varies the other. The product-aligned placement therefore partitions interactions into horizontal and vertical groups. Compatible row problems execute in parallel, followed by compatible column problems (Fig. 1; §2.2–3.1, PDF pp. 2–4).

ONEX takes an ordered gate-stage schedule derived from edge coloring and applies three phases (Fig. 4; §3.2, PDF p. 5):

1. **Depth search using SMT:** jointly choose qubit placements and gate-stage times, seeking a feasible plan at minimum depth within the specified 1D model and input schedule.
2. **Movement compaction using MILP:** retain structural features of one plan and optimize its spatial coordinates to reduce displacement.
3. **Iterative refinement:** tighten displacement or duration bounds in SMT, obtain another plan, and compact it again. Parallel solver seeds and speculative searches over bounds reduce wall-clock search time.

### What the SMT formulation fixes and optimizes

Appendix A.1 (PDF p. 14) supplies a fixed ordered schedule S = [s0, …, sL−1], N qubits, M traps, and a candidate number T of discrete time steps. Its principal variables are the trap indices π(q,t) and gate-stage times t(k). Each trap index decomposes into an interaction-site index σ(q,t) = floor(π(q,t)/2) and a binary within-site offset ℓ(q,t). There are two traps per interaction site.

The constraints enforce distinct traps, the prescribed stage order, co-location of each gate pair at an interaction site when its stage executes, isolation of idle qubits from one another, and preservation of relative order for atoms that both move during a transition. The no-crossing condition is conditional on both atoms moving; it is not a fixed ordering of every qubit throughout the entire execution.

The formulation includes initial placements π(q,0) among its variables and does not specify a fixed initial mapping. The stage sequence is fixed by t(k) < t(k+1). The authors use quantifier-free bit-vector constraints with Z3. They first find a feasible depth and then search downward until reaching the lower bound or proving the next smaller depth infeasible (Appendix A.1). A timeout or unknown result is not an infeasibility proof.

For repeated HGP syndrome extraction, the authors separately mention a lightweight solver that returns qubits to their initial placement (§4.2.2, PDF p. 7). The core formulation in Appendix A.1 alone does not describe the complete cyclic execution procedure.

### How distance compaction is modeled

Phase 2 starts with one depth-optimal solution. It preserves the left-to-right qubit ordering at every time slice and requires every previously stationary qubit to remain stationary across that transition. Trap coordinates remain variables; required gate pairings and other validity constraints remain enforced (Appendix A.2; Fig. 13, PDF pp. 14–15).

The physical coordinate is

\[
x_q^t = d_{\mathrm{site}}\sigma_q^t + d_{\mathrm{trap}}\ell_q^t.
\]

For each transition, the MILP introduces D(t), constrained to bound every atom's displacement through the two linear inequalities

\[
D_t \ge x_q^{t+1}-x_q^t,\qquad D_t \ge x_q^t-x_q^{t+1}.
\]

Its primary objective minimizes the sum of these per-transition maximum displacements. Its secondary objective minimizes total atom displacement. It therefore optimizes coordinate assignments within the retained structure rather than enumerating every minimum-depth SMT solution.

The timing model is nonlinear:

\[
\tau_t = 2t_{\mathrm{transfer}} + \sqrt{D_t/\alpha}.
\]

The authors explicitly state that the linear displacement objective differs from duration and accept a compacted solution only if evaluated duration improves. Phase 3 can change the movement structure through renewed SMT solving. Local refinement tightens transition bounds; global refinement uses a lookup table of quantized durations to encode an aggregate duration bound (Appendix A.2–A.3, PDF pp. 15–16).

### Benchmarks, comparisons, and reported evidence

The main memory benchmarks are HGP codes (§4.1; Fig. 14). Here n counts data qubits, excluding check ancillas:

| Code [[n,k,d]] | Data qubits | Logical qubits | Distance |
| --- | ---: | ---: | ---: |
| [[225,9,4]] | 225 | 9 | 4 |
| [[625,25,6]] | 625 | 25 | 6 |
| [[1225,49,8]] | 1225 | 49 | 8 |
| [[2500,100,12]] | 2500 | 100 | 12 |

The separate 1D benchmarks use edge-colored random classical (3,4)-regular Tanner graphs (§4.1; Table 2). Section 6 additionally studies a [[2610,744,d ≤ 16]] lifted-product code with lift size 45, from reference [6]. The upper bound on distance must not be restated as an established distance of 16.

| Evaluation | Baselines and scope |
| --- | --- |
| Main HGP memory | Xu et al.'s constructive 1D algorithm [50] and Enola's general 2D compiler [41], evaluated under the same stated neutral-atom architecture and timing assumptions |
| Formulation ablation | An author-constructed SMT/MILP-enhanced version of Xu et al.'s local routing formulation, compared with ONEX's joint formulation |
| Zoned architecture | PowerMove [30] and ZAC [21], plus decomposition-adapted PM-D and ZAC-D; these comparisons use single-round circuits |
| Lifted-product example | ONEX versus ONEX-Z; no corresponding prior-compiler comparison is reported in Table 3 |

Reference [50] is Xu et al., *Constant-overhead fault-tolerant quantum computation with reconfigurable atom arrays* (2024). Reference [41] is Tan et al., *Compilation for Dynamically Field-Programmable Qubit Arrays with Efficient and Provably Near-Optimal Scheduling* (2025). Specialized layouts such as qSIEVE [44] are discussed, not directly benchmarked; the authors argue that they exploit additional code structure (§1; §7).

Table 1 (PDF p. 6) reports modeled cycle durations of 6.66 ms for ONEX, 24.39 ms for Xu et al., and 280.36 ms for Enola at 2500 data qubits. Across the four HGP codes, the reported clock-rate improvement is 3.7–6.1× over Xu et al. and 29.8–42.1× over Enola. These are compiled plans evaluated with a timing model, not measured hardware executions.

Figure 7 (§4.3.2, PDF p. 9) reports an additional 1.77–2.88× duration improvement from ONEX over the solver-enhanced local baseline. This is evidence that the joint formulation contributes beyond replacing a heuristic with solver calls.

The authors simulate logical error rates with Stim and BP-OSD under their circuit-level noise and rearrangement-idling model. Appendix B reports 1.23–1.85× lower single-round logical error rates at physical error rate 0.005 than the Xu et al. baseline. This is model-dependent simulation evidence.

Compilation remains expensive: §4.4 reports a mean of 12.8 hours to find depth-6 solutions at 1D size N = 70, corresponding to HGP n = 2500. This is a feasible-solution timing measurement, not a separately established total time for all optimization and optimality certification. The experiments use a 192-core server; parallel solver configurations appear in Appendix C.

### Scope and limits stated in the source

The main application is memory; logical operations are proposed future work (§7). The depth guarantee belongs to the specified 1D formulation and input schedule. Phase 2 explicitly uses a surrogate distance objective. The zoned experiments use single-round circuits because the baselines do not natively support multi-round rearrangement; zoned fidelity is left for future work (§5). The LP case is one representative example with additional intra-lift and directional-transfer procedures (§6).

## My thoughts

2026-09-30 — reader's words, retained verbatim:

> here is a point. different color order I guess will infulence the movements.
>
> i also think the initial mapping will infulence the movements

## Codex interpretation

The central contribution is the match between product-code structure, Cartesian hardware control, and a smaller exact search problem. The overall process chooses a schedule first, optimizes placement and rearrangement conditional on that schedule, then improves duration. This is narrower than joint optimization over all valid schedules and all physical plans.

The reader's two observations concern different choices. Color order is fixed in the published formulation; initial placement is free. Different valid color orders can create different placement transitions, although not every permutation must change the optimum. Any proposed schedule reordering must preserve syndrome-extraction behavior. The return-to-start procedure also needs to be considered when assessing a complete repeated round.

> [!hypothesis]
> Suggested by Codex; not yet verified. Searching over valid color-stage orders may improve ONEX's resulting duration beyond its fixed-schedule results. The rationale is that different stage adjacencies impose different rearrangement requirements. Test this by holding a code and coloring fixed, validating candidate orders, and recompiling them with matched resource budgets. Record depth, duration, initial placement, and cyclic return cost. The paper discussion examined does not quantify this opportunity.

**Symmetry remains an implementation question.** The paper does not describe explicit symmetry-breaking constraints. Dimensional decomposition, bit-vector encoding, incremental solving, seed portfolios, and bound speculation are documented, but do not establish elimination of equivalent assignments. Under symmetric hardware and compatible boundary conditions, left-right reflection produces equivalent plans; a constraint selecting one orientation could remove that symmetry. This is a Codex proposal, not a reported ONEX feature. Fixing an arbitrary full initial qubit order would generally remove genuinely different solutions, because the gate graph distinguishes qubits. Similarly, Phase 2's order preservation deliberately restricts the feasible subspace; it is not just symmetry elimination.

**Correction, 2026-09-30.** Codex's initial explanation incorrectly suggested that the idle-site constraint might omit protection against idle atoms sharing an active gate site. Each site has exactly two traps; the gate pair occupies both, and injectivity excludes a third atom. The stated constraints already cover that case. The earlier suspicion is withdrawn on this basis; it should not be carried forward as a paper defect.

**Clarification, 2026-09-30.** The earlier compaction explanation was imprecise about the objective: Phase 2 minimizes the sum of per-transition maximum displacements, then total displacement. It does not independently minimize every transition or prove minimum physical duration.

## Open questions and resumption points

The following reader comments are retained verbatim. The answers underneath are provisional Codex explanations, not confirmed reader understanding.

2026-09-30 — reader, about distance compaction:

> how it shorten the distance. enumerate both solutions in 2?
> or model those

- Current answer: Phase 2 uses a MILP over coordinates within one SMT-derived structure. Phase 3 can supply other structures. The formulation and distance-versus-duration distinction are recorded above.
- To revisit: work through a small valid trajectory and Figure 13 to show precisely which coordinates can move and which order/stationarity relations remain fixed.

2026-09-30 — reader, about the solver formulation:

> this processs heavy rely on the SMT. Thus how to model the problem matters. explain this. And how it avoid the symmetry.

- Current answer: Appendix A.1 specifies the placement/time variables and five constraint families. Figure 7 provides a formulation ablation. Explicit symmetry handling was not found in the paper text.
- To answer further: inspect an available implementation for symmetry constraints, bounded arithmetic, initial/boundary conditions, and the distinction between feasible and certified optimal results. Code availability has not been established in this discussion.

2026-09-30 — reader, about evaluation:

> if they compared with other prior work. And which codes they used.

- Current answer: code parameters and comparisons are tabulated above. Main HGP, standalone 1D, zoned single-round, and LP results have different scopes.
- To answer further: inspect the actual seed matrices and benchmark instances, baseline configuration and scheduling choices, and how independently optimized 1D plans are composed into cyclic memory execution. Parameters alone do not identify exact parity-check matrices.

Additional question arising from the reader's scheduling observation, recorded by Codex on 2026-09-30: how much do valid color orders and cyclic boundary handling change the achievable movement depth and duration? A controlled recompilation experiment would answer this. No measured gap has been established.

**Suggested place to resume:** a small example of the SMT variables and constraints, followed by compaction of the same trajectory. Then examine color-order sensitivity and symmetry handling in any available implementation.

## Important locations

- PDF pp. 2–3, Fig. 1 and Eq. (1): product-code decomposition into row and column interactions.
- PDF pp. 4–5, Figs. 3–4: physical execution protocol and compiler pipeline.
- PDF pp. 6–7, Tables 1–2: benchmarks, timing assumptions, comparisons, and cyclic-return discussion.
- PDF p. 9, Fig. 7 and §4.4: formulation ablation and compilation scaling.
- PDF pp. 10–13, Figs. 10–12 and Table 3: zoned comparison and LP example.
- PDF pp. 14–16, Appendix A and Fig. 13: SMT constraints, MILP compaction, feedback, and parallelism.
- PDF pp. 16–18, Fig. 14 and appendices B–C: logical-error simulation and solver parallelism.
