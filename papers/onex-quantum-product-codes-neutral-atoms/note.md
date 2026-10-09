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
reading_dates: [2026-09-23, 2026-09-30, 2026-10-03, 2026-10-09]
---

# Architecture and Compilation Co-Design for High-Rate Quantum Product Codes on Neutral Atom Arrays

## Source and reading coverage

[Original PDF](source.pdf), arXiv:2608.20164v1, dated 20 August 2026.

**Provisional discussion checkpoint, saved 2026-09-30 at the reader's request.** The reader is pausing for other business and intends to review these notes and continue later. The discussion is not finished. Codex explanations below have not been confirmed as the reader's understanding.

On 2026-09-23, Codex read the main text (PDF pp. 1–13) and appendices A–C (PDF pp. 14–18); references were skimmed. PDF page indices and printed page numbers coincide. Text was extracted locally. Figure 1, Figure 4, and the constraints on p. 14 were also inspected in rendered pages; the remaining figures were not comprehensively visually audited. On 2026-09-30, follow-up reading revisited the formulation and compaction in Appendix A.1–A.3, the benchmarks and formulation ablation, the zoned and lifted-product evaluations, and relevant references. No compiler implementation, solver certificates, or experimental reproduction was inspected.

The initial conversational explanation was too compressed. The reader requested the problem background and methodology, followed by questions about scheduling, initial placement, distance compaction, SMT modeling, symmetry, and comparisons. This note preserves that discussion for resumption.

**Checkpoint update, 2026-10-09, requested by the reader.** The reading remains in progress. On 2026-10-03, Codex revisited §3.2 and Appendix A.1–A.3 (PDF pp. 4–5 and 14–15), including rendered pp. 14–15, to recover the earlier stopping points. On 2026-10-09, discussion covered MILP, discrete depth versus physical duration, parallel movements, and gate-pulse time. Codex consulted PDF pp. 4–7 and 14–15, inspected rendered pp. 4, 6, and 14, and added the detailed Phase 1 walkthrough below. The walkthrough is a Codex explanation of the source; its small example is constructed for teaching, not taken from the paper or produced by an ONEX run. No implementation or solver certificate was inspected. The earlier checkpoint and the reader's personal text are preserved.

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

#### Phase 1 equations and depth search — clarification, 2026-10-09

Appendix A.1 (PDF p. 14) describes a feasibility model at a candidate depth T. In the notation below, t indexes placement snapshots and t_k is the snapshot assigned to gate stage k. The fixed inputs are the qubits Q, trap count M, and ordered gate schedule S = [s_0, …, s_{L-1}]. Each s_k contains disjoint pairs that execute in parallel. The solver chooses the placements and gate-stage times jointly:

\[
0 \le \pi_q^t < M,\qquad 0 \le t_k < T,
\qquad \sigma_q^t=\lfloor\pi_q^t/2\rfloor,
\qquad \ell_q^t=\pi_q^t\bmod 2.
\]

Here π is a trap index, σ is an interaction-site index, and ℓ selects one of the site's two traps. These are bounded discrete variables, encoded using quantifier-free bit vectors (QF_BV), rather than unbounded mathematical integers. The following equations are mathematical presentations of the source constraints, not implementation code. Source quantifiers indicate constraints instantiated over the finite inputs; the reported solver encoding is quantifier-free.

1. **Distinct traps:** at every snapshot, two different qubits must have different trap indices:

   \[
   \pi_i^t\ne\pi_j^t\quad(i\ne j).
   \]

2. **Fixed stage order:** the solver chooses when each stage executes, but cannot reorder the input stages:

   \[
   t_k<t_{k+1}.
   \]

3. **Required gate pairs:** if stage k executes at snapshot t, each pair in that stage must share an interaction site:

   \[
   (t_k=t)\Rightarrow(\sigma_u^t=\sigma_v^t),
   \qquad (u,v)\in s_k.
   \]

   Combined with distinct traps, the pair occupies the two different traps of that site.

4. **Idle-qubit isolation:** let I_k be the qubits absent from all pairs in stage k. At that stage, different idle qubits must occupy different sites:

   \[
   (t_k=t)\Rightarrow(\sigma_i^t\ne\sigma_j^t),
   \qquad i\ne j\in I_k.
   \]

   Idle qubits cannot share a site with an active gate pair either: the pair already occupies both traps, and distinct-trap constraints leave no room for another atom. This site-isolation condition applies at gate stages; an intermediate snapshot without a gate stage is not subject to this particular condition.

5. **No crossing between co-moving atoms:** define m_q^t to mean that atom q changes traps between snapshots t and t+1:

   \[
   m_q^t\Leftrightarrow(\pi_q^t\ne\pi_q^{t+1}).
   \]

   If both i and j move in that transition, their relative order must be preserved:

   \[
   (m_i^t\land m_j^t)\Rightarrow
   \big[(\pi_i^t<\pi_j^t)\Leftrightarrow
   (\pi_i^{t+1}<\pi_j^{t+1})\big].
   \]

   The condition is on both atoms moving. It does not impose a single fixed order of all atoms throughout the execution.

The initial positions π_q^0 are variables too. No displacement objective or physical movement-time objective appears in this Phase 1 feasibility model. One SAT result supplies a placement table and stage times for the chosen T. UNSAT establishes that no assignment satisfies that model at that T; UNKNOWN or a timeout establishes neither feasibility nor infeasibility.

Appendix A.1.2 searches upward with short time budgets to find a feasible depth, then downward with larger budgets to seek a smaller one. The lower bound is T ≥ L because the L gate stages require strictly increasing snapshot indices. A solution at T* is depth-optimal within this fixed-schedule model if it reaches L or the next smaller depth T*−1 is proved UNSAT. Optimality is conditional on the specified inputs and constraints, and cannot be inferred from a timeout.

#### Discrete depth, parallel movement, and gate time — clarification, 2026-10-09

In Appendix A's indexing, there are T placement snapshots, t = 0, …, T−1, and T−1 transitions between them; the compaction sums in Appendix A.2 run from 0 to T−2. Section 4.2.2 informally calls T the number of rearrangement steps. Do not use that wording to erase the distinction between snapshots and transitions, or infer full-cycle boundary costs from the core model alone.

All compatible atoms moving in one transition form one parallel rearrangement layer. Its duration depends on the maximum physical displacement in that layer, not the sum of individual atom travel times. Gate stages execute at selected snapshots, after the required atoms have been brought together. Figure 3 (PDF p. 4) depicts gate pulses and rearrangements sequentially; gates within one stage execute in parallel. Thus, for the modeled 1D execution with L entangling stages, the rearrangement and gate contribution is

\[
\sum_{t=0}^{T-2}\tau_t+L\,t_{\mathrm{gate}},
\qquad
\tau_t=2t_{\mathrm{transfer}}+\sqrt{D_t/\alpha}.
\]

This expression does not by itself describe all preparation, measurement, or cyclic-return costs of a complete memory round. Section 4.1 (PDF p. 6) assumes t_gate = 0.36 μs, t_transfer = 15 μs, and α = 2.75 × 10^−3 μm/μs². The gate-stage count L is fixed during Phase 1, so its modeled pulse-time contribution is constant. Minimum discrete depth does not guarantee minimum elapsed movement time.

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

### Worked Phase 1 example — 2026-10-09

This is a Codex-constructed example of Appendix A.1's model, not a paper benchmark or an executed solver result. Use four qubits A, B, C, D and eight traps. Sites 0, 1, 2, 3 contain trap pairs (0,1), (2,3), (4,5), (6,7), respectively. The fixed input has two stages: s_0 = {(A,B)}, then s_1 = {(A,C)}. D is always idle.

For candidate T = 2, the stage times must be t_0 = 0 and t_1 = 1. One satisfying assignment is:

| Snapshot | A's trap | B's trap | C's trap | D's trap | Gate stage |
| --- | ---: | ---: | ---: | ---: | --- |
| 0 | 0 | 1 | 4 | 6 | A–B |
| 1 | 5 | 1 | 4 | 6 | A–C |

At snapshot 0, A and B share site 0; idle C and D occupy sites 2 and 3. At snapshot 1, A and C share site 2; idle B and D occupy sites 0 and 3. All traps are distinct. Only A moves, so there is no pair of co-moving atoms whose order could reverse. Under this model, A passing stationary B and C does not violate the conditional no-crossing constraint. The example has two snapshots, one rearrangement transition, and two gate stages. Since T = L = 2, this assignment attains the model's depth lower bound; no solver run is needed to check that fact for this small example.

For comparison, retain snapshot 0 but propose snapshot 1 as A = 0, B = 4, C = 1, D = 6. This puts A and C together and keeps idle B and D isolated. However, B and C both move, and their order reverses: B < C initially, but B > C finally. Constraint 5 rejects this simultaneous swap. An additional intermediate snapshot, or a different trajectory such as the valid one above, is required. This shows why gate co-location alone is an insufficient formulation and why the solver chooses movements and placements jointly.

SMT means *satisfiability modulo theories*: the solver finds values satisfying logical formulas together with rules for a chosen domain, here fixed-width bit vectors. Conceptually, one Phase 1 call answers “Does a valid placement-and-stage-time table exist at this T?” The outer depth search turns those feasibility answers into depth optimization. This is distinct from Phase 2's MILP (*mixed-integer linear programming*), which optimizes a linear displacement objective within a retained structure. The input coloring controls gate-stage count; Phase 1 controls discrete depth; Phase 2 controls a restricted distance objective; Phase 3 searches other structures under tighter bounds. The input coloring is described as near-optimal in §3.2, not as a general certificate of globally minimum gate depth.

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

**Development, 2026-10-09.** At the reader's request, the note now includes the Phase 1 equations, SAT/UNSAT depth search, a valid small trajectory and a rejected simultaneous swap, plus the distinctions between snapshots, parallel transitions, and gate-pulse duration. These are Codex explanations, not an endorsement or a record of confirmed reader understanding. The earlier resumption suggestion remains as historical context. Next useful step: work through compaction of a trajectory with unnecessary spatial gaps, then revisit symmetry and color-order sensitivity. Explicit symmetry handling and full-cycle boundary details remain unresolved.

## Important locations

- PDF pp. 2–3, Fig. 1 and Eq. (1): product-code decomposition into row and column interactions.
- PDF pp. 4–5, Figs. 3–4: physical execution protocol and compiler pipeline.
- PDF pp. 6–7, Tables 1–2: benchmarks, timing assumptions, comparisons, and cyclic-return discussion.
- PDF p. 9, Fig. 7 and §4.4: formulation ablation and compilation scaling.
- PDF pp. 10–13, Figs. 10–12 and Table 3: zoned comparison and LP example.
- PDF pp. 14–16, Appendix A and Fig. 13: SMT constraints, MILP compaction, feedback, and parallelism.
- PDF pp. 16–18, Fig. 14 and appendices B–C: logical-error simulation and solver parallelism.
