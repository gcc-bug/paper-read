---
type: paper
title: "Asymptotically Good Quantum Codes with Addressable Transversal T Gates"
authors: [Tongyin Lin, Bujiao Wu, Bin Cheng]
year: 2026
status: reading
tags: []
source: "source.pdf"
original_filename: "2609.35129v1.pdf"
provenance: "Selected by the reader through https://scirate.com/arxiv/2609.35129. arXiv v1 PDF retrieved from https://arxiv.org/pdf/2609.35129v1 on 2026-10-10; original_filename records the temporary local download name."
reading_dates: [2026-10-02, 2026-10-09, 2026-10-10]
---

# Asymptotically Good Quantum Codes with Addressable Transversal T Gates

## Source and reading coverage

[Original PDF](source.pdf), arXiv:2609.35129v1. The arXiv stamp says 28 September 2026; the manuscript title page says 29 September 2026. PDF page indices and printed page numbers coincide.

**Discussion checkpoint consolidated on 2026-10-10 at the reader's request.** The discussion moved from the paper's contribution to prerequisites in quantum error correction. Status remains `reading`: the construction's detailed algebraic-geometry and binary-embedding proofs have not been worked through with the reader. The second selected paper, arXiv:2609.39556, has not been read in this discussion.

On 2026-10-02, Codex made a first pass through the main text (§§1–6, PDF pp. 1–16) and selected numerical material in Appendix D (PDF pp. 26–27); references were skimmed. The phase argument on p. 7 and numerical bounds on p. 27 were checked against rendered PDF pages. On 2026-10-09–10, discussion revisited the prior-work gap, transversal gates, examples, and mathematical definitions. During consolidation on 2026-10-10, Codex rechecked metadata, §§1–1.2, Lemma 3.1, §6, and Corollary D.1 using local PDF extraction and rendered pp. 7 and 27. This is not a complete proof audit, independent literature audit, implementation inspection, or experimental reproduction. Extraction and page images remain outside the repository.

For the theorem background, Codex also consulted Bryan Eastin and Emanuel Knill, *Restrictions on Transversal Encoded Quantum Gate Sets* (2009), [supporting PDF](references/eastin-knill-transversal-gate-restrictions.pdf), arXiv:0811.4262v2. Retrieved from https://arxiv.org/pdf/0811.4262v2 on 2026-10-10, with temporary original filename `eastin-knill-0811.4262v2.pdf`. Consultation covered PDF p. 1's error-detection condition and definition of transversality, pp. 2–3's group argument, Theorem 1 and Corollary 1, and p. 4's scope and circumventions. PDF pp. 2–4 have matching printed labels; the first PDF page has no printed page number. Its references were not independently followed. This is a supporting reference, not a separate paper-reading record.

## Source claims

### Problem, motivation, and prior-work gap

The authors seek one binary CSS code family with constant encoding rate, linear minimum distance, and independently selectable transversal logical powers of \(T=\operatorname{diag}(1,e^{i\pi/4})\). Rate \(K/N\) and relative distance \(D/N\) must stay bounded away from zero as block length grows. Full addressability requires a fixed code and encoding, with physical one-qubit gates implementing \(T\) on any selected logical qubit and identity on the others (Definition 1.1, PDF p. 3).

The following comparison is the authors' account, not an independent assessment of every cited construction (§§1–1.2, PDF pp. 2–5):

| Prior construction | Achieved property | Missing for the precise target here |
| --- | --- | --- |
| Golowich–Guruswami, Nguyen, and addressable extensions by He et al. | Good binary codes with transversal logical CCZ, including selected logical triples | A logical T implemented solely by single-qubit physical powers of T |
| Berardini et al.; Reddy–Kashyap CSS-T families | Good parameters and preservation under physical transversal T | The stated induced logical actions are identity and S-dagger, respectively |
| Hastings–Haah / Haah families | Logical T, growing dimension and distance | Rate vanishes asymptotically |
| Wills's divisible-monomial construction | Constant rate and simultaneous transversal logical T without correction | Its proved distance lower bound, \(2^{\Omega(\sqrt{\log N})}\), does not establish linear distance |

Simultaneous T on all logical qubits does not by itself establish selection of individual ones. The paper also explicitly acknowledges independent concurrent work by San-José achieving related good codes and addressable rotations via hierarchy lowering. Its stated methodological distinction is direct prescription of weighted-divisibility coefficients using fivefold binary overlap conditions (§1.2, PDF p. 5). Do not describe this paper as the sole resolution of compatibility.

### Main idea and phase mechanism

Lemma 3.1 starts with a classical binary code containing words \((x,y)\), where selected information coordinates \(x\) will label the logical basis. Puncturing removes those coordinates from every codeword; shortening additionally requires those coordinates to be zero before removing them. The resulting nested classical codes define a CSS quantum code (PDF pp. 5–7).

For a requested logical exponent vector \(c\in\mathbb Z_8^K\), the construction supplies physical exponents \(b(c)\in\mathbb Z_8^N\) such that

\[
\sum_j b_j(c)y_j\equiv\sum_\ell c_\ell x_\ell\pmod8
\]

for every string \(y\) in the encoded superposition associated with \(x\). Applying \(\bigotimes_jT^{b_j(c)}\) therefore gives every term of that superposition the same required logical phase. In terms of the fixed encoding isometry \(E\),

\[
T^{b(c)}E=ET^c.
\]

This action is exact and needs no subsequent Clifford correction. The exponents depend linearly on \(c\) over \(\mathbb Z_8\) (Theorem 1.2; Lemma 3.1, Eqs. (13)–(16), PDF pp. 3, 7).

### Construction and assumptions

The authors use algebraic-geometry codes over \(\mathbb F_{1024}\) with a 15-multiplication property: coordinate sums of products of sixteen codewords vanish. A fixed binary embedding converts these identities into even fivefold overlaps. The binary 4-multiplication property then permits a lift from parity coefficients to weighted divisibility modulo eight: \(a=p+2t+4z\), with \(t,z\) found through binary linear systems. Normalizing an invertible coefficient matrix on information coordinates gives independently prescribed logical phases (Lemmas 4.1–4.4, PDF pp. 8–12).

Theorem 4.5 restricts selected field coordinates to a trace-one binary subspace, compresses their images, and punctures/shortens. The outer code and dual distances yield linear bounds on both quantum directional distances (PDF pp. 12–14). These are exact coding statements; the distance's error-correction interpretation assumes ideal recovery. They are not a noisy syndrome-extraction or hardware threshold analysis.

### Results and limitations

For the Appendix D embedding, the authors report a binary inner code \([244,10,100]\) and derive

\[
\frac{K_i}{N_i}\longrightarrow\frac1{241804},\qquad
\liminf_i\frac{D_{X,i}}{N_i}\ge\frac{92500}{241804},\qquad
\liminf_i\frac{D_{Z,i}}{N_i}\ge\frac1{241804}.
\]

Hence \(\liminf_i D_i/N_i\ge1/241804\). The rate is an asymptotic value; the distances are lower bounds, not measured distances. The reported embedding search certifies a feasible length of 244, not global minimality (Corollary D.1 and preceding text, PDF p. 27).

The authors leave good quantum LDPC codes with this precise addressable T property open, along with the full space-time tradeoff including noisy syndrome extraction, ancillary preparation, complementary logical gates, and classical processing (§6, PDF pp. 15–16).

## My understanding

2026-10-10 — reader's words:

> OK. I see. I missunderstand some very important and basic knowledge in this area. But current seesion truly help.

## My thoughts

Reader's earlier words, retained from this discussion:

> It looks just some code tips. But i guess more important math limit below those

## Codex interpretation

### What the contribution does and does not establish

The three desired properties are compatible; the gap was a construction problem, not a theorem forbidding their coexistence. Good storage parameters alone do not determine the available logical gates. A collective logical \(T^{\otimes K}\) supplies one phase pattern; addressability needs patterns isolating each of \(K=\Theta(N)\) logical qubits within a fixed encoding.

The explicit rate corresponds asymptotically to 241,804 physical qubits per logical qubit. Thus "constant overhead" is a scaling statement and need not mean small overhead. This is principally a theoretical compatibility result. It does not evade Eastin–Knill, since addressable powers of T alone are not universal.

### Code space, encoding, and orthogonal projection

For N physical qubits, the physical Hilbert space is \(\mathcal H=(\mathbb C^2)^{\otimes N}\), of dimension \(2^N\). A code encoding K logical qubits uses a \(2^K\)-dimensional subspace \(\mathcal C\). An encoding isometry \(E\) maps logical states into that subspace, with \(E^\dagger E=I_L\). The orthogonal projector is \(P=EE^\dagger\).

For example, the bit-flip repetition encoding has \(|0_L\rangle=|000\rangle\), \(|1_L\rangle=|111\rangle\), and

\[
\mathcal C=\operatorname{span}\{|000\rangle,|111\rangle\},\qquad
P=|000\rangle\langle000|+|111\rangle\langle111|.
\]

"Span" means all linear combinations. The code space is a set of vectors; P is an operator. It keeps the component in the code space and removes the perpendicular component: \(P|000\rangle=|000\rangle\), \(P|010\rangle=0\). Writing P is a mathematical description, not an instruction to physically measure during a gate. This repetition example protects against bit flips, not arbitrary single-qubit errors; its quantum distance is one.

For a fixed subspace and inner product, the orthogonal projector is unique. Its conditions are

\[
P^2=P,\qquad P^\dagger=P,\qquad\operatorname{image}(P)=\mathcal C.
\]

Idempotence means projecting twice changes nothing further. Hermiticity supplies orthogonality: \(\langle P\psi|(I-P)\psi\rangle=\langle\psi|(P-P^2)|\psi\rangle=0\). If Hermiticity is dropped, many oblique projectors can share an image. For example, \(\begin{pmatrix}1&a\\0&0\end{pmatrix}\) projects onto the first coordinate axis for every a, but is orthogonal only when a=0. Different orthonormal bases of the same subspace give the same P.

### Operator support and local error detection

An operator supported on a set S has the form \(O_S\otimes I_{\overline S}\): it acts only on those physical qubits, possibly jointly. For example, \(X\otimes I\otimes Z\) has support \(\{1,3\}\). Support describes which qubits an operator touches; transversality describes its factorization. Thus \(T^{\otimes15}\) is transversal but has support on all fifteen qubits.

For an exact distance-D code, any operator supported on fewer than D qubits obeys

\[
POP=c_OP.
\]

This is the error-detection condition. Read POP from right to left: restrict the input to the code, apply O, and project the output back. For an encoded input,

\[
O|\psi_L\rangle=c_O|\psi_L\rangle+(I-P)O|\psi_L\rangle.
\]

The second term can be nonzero. Logical triviality of the projected action does not mean the physical state is unchanged. In an orthonormal logical basis, \(\langle a_L|O|b_L\rangle=c_O\delta_{ab}\): off-diagonal matrix elements vanish and all diagonal elements agree. For a local observable, the expectation is independent of the encoded state; local observation cannot reveal the logical information.

In the repetition example, \(X_1\) sends \(\alpha|000\rangle+\beta|111\rangle\) to \(\alpha|100\rangle+\beta|011\rangle\). Both output basis states are outside the code space, so \(PX_1P=0\). The amplitudes survive in an error space and can be recovered. This example establishes detection of this particular bit flip, not detection of all one-qubit operators. If O is unitary and preserves the code, its scalar action has unit magnitude and is only an overall phase.

### Why physical T works for one code and fails for another

The following are Codex's worked examples, not new results of the paper. Their weight distributions and CSS X/Z distances were checked by finite enumeration during consolidation on 2026-10-10.

For the 15-qubit quantum Reed–Muller code, label physical positions by nonzero \(v\in\mathbb F_2^4\). Define \(y(a)_v=a\cdot v\pmod2\) for each \(a\in\mathbb F_2^4\). The sixteen strings form a linear code C0. With C1 generated by C0 and the all-ones string, the CSS encoding is

\[
|0_L\rangle=\frac14\sum_a|y(a)\rangle,\qquad
|1_L\rangle=X^{\otimes15}|0_L\rangle.
\]

The zero string has weight zero; each of the fifteen nonzero strings has weight eight. Their complements have weights fifteen and seven. These are selected strings, not all strings of those weights. The CSS code has \([[15,1,3]]\), with \(D_X=7\) and \(D_Z=3\).

For any physical bit string y,

\[
T^{\otimes N}|y\rangle=e^{i\pi|y|/4}|y\rangle.
\]

All terms in the first encoded state therefore acquire phase 1; all terms in the second acquire \(e^{-i\pi/4}\). Thus physical \(T^{\otimes15}\) implements logical T-dagger, and \((T^\dagger)^{\otimes15}\) implements logical T. These operations are transversal because they factor into one-qubit gates. The phase calculation separately proves their valid logical action.

For the 7-qubit Steane code, the analogous construction labels positions by nonzero \(v\in\mathbb F_2^3\). Its logical zero is an equal superposition of one weight-zero string and seven weight-four strings. Applying physical \(T^{\otimes7}\) leaves the first amplitude positive and flips the signs of the other seven. The output is not proportional to logical zero. Logical one has disjoint support on complemented weight-three and weight-seven strings, so the output is not any combination of the two logical basis states either: it leaves the code space.

| Code | Weights within logical zero | Weights within logical one | Uniform physical T |
| --- | --- | --- | --- |
| Steane, \([[7,1,3]]\) | 0 and 4 | 7 and 3 | Does not preserve the code space |
| Reed–Muller, \([[15,1,3]]\) | 0 and 8 | 15 and 7 | Implements logical T-dagger |

A logical diagonal gate must preserve the relative amplitudes within each encoded basis state while adjusting phases between logical basis states. One cannot infer this from physically applying T on every wire.

Weight conditions are constrained by code linearity. For binary strings, \(|u\oplus v|=|u|+|v|-2|\operatorname{supp}(u)\cap\operatorname{supp}(v)|\). If every codeword's weight is divisible by eight, pair overlaps must be divisible by four; the three-string inclusion-exclusion identity additionally implies even triple overlaps. Divisibility therefore constrains many related codewords, not just individually chosen examples. Weighted versions organize the controllable phases used in this paper.

### Generators, physical gates, and logical gates

A Hermitian operator H generates a one-parameter family \(U(\theta)=e^{-i\theta H}\). The matrix exponential is defined by its convergent power series. Equivalently, if \(H|h_m\rangle=\lambda_m|h_m\rangle\), then \(U(\theta)|h_m\rangle=e^{-i\theta\lambda_m}|h_m\rangle\). H specifies which eigenvectors accumulate which phases as the parameter changes. Differentiation gives the equivalent definition \(H=i\,dU/d\theta|_{\theta=0}\).

For example, \(H=|1\rangle\langle1|\) generates \(\operatorname{diag}(1,e^{-i\theta})\). A single endpoint unitary generally has multiple Hermitian logarithms because phases are defined modulo \(2\pi\); the specified family for all real \(\theta\) has a unique generator. H here denotes a generator, not the Hadamard gate.

For physical one-qubit generators \(h_j\), implicitly extended by identities on other qubits,

\[
U_j(\theta)=e^{-i\theta h_j},\qquad
U(\theta)=\bigotimes_jU_j(\theta)
=e^{-i\theta H},\qquad H=\sum_jh_j.
\]

The \(h_j\) are generators; the \(U_j\) are gates; U is the transversal physical operation. H is a physical generator. If this entire evolution preserves the code, the induced logical generator is \(H_L=E^\dagger HE\).

### Eastin–Knill: exact boundary and proof outline

The theorem excludes a universal set of transversal unitary logical gates for a fixed exact code that encodes nontrivial information and detects arbitrary single-subsystem errors, with finite-dimensional physical subsystems. Universality means approximating every logical unitary arbitrarily well. In the group argument, the transversal partition is fixed; changing codes, using measurements/feed-forward, or other operations adds ingredients outside that gate group (Eastin–Knill supporting PDF, pp. 1–4, Theorem 1 and Corollary 1).

Local error detection gives \(Ph_jP=c_jP\). If a continuous transversal evolution preserves the code at every parameter value, its physical generator also preserves the code and

\[
H_L=E^\dagger HE=\left(\sum_jc_j\right)I_L.
\]

Only an overall logical phase results. This conclusion is about continuous code-preserving evolution; without code preservation, projected scalar matrix elements do not describe the full dynamics.

Why do isolated discrete gates not evade the argument and become universal by composition? Products of transversal gates in the fixed partition remain transversal, and products of code-preserving gates preserve the code. All such gates form a closed subgroup of a compact finite-dimensional matrix group. The closed-subgroup theorem makes this a compact Lie group. Its connected identity component acts trivially on logical states up to phase by the generator argument. A compact Lie group has finitely many connected components, and each component has one logical action up to phase. Hence only finitely many distinct transversal logical actions are available on the fixed code, even after arbitrary compositions.

The limit step matters: a discrete rotation by an irrational fraction of a full turn generates a dense set, whose closure is the continuous circle. A purported dense universal transversal set would likewise have its limits in the closed code-preserving group. The theorem forbids the nontrivial continuous logical action those limits would require. Compactness alone does not imply that an arbitrary discrete subset is finite; the Lie-group structure and connected-component quotient are essential.

### Intermediate states and the actual cost of the example

For \(R(\theta)=\operatorname{diag}(1,e^{i\theta})\), uniform \(R(\theta)^{\otimes15}\) gives the weight-zero and weight-eight components of logical zero phases 1 and \(e^{i8\theta}\). They agree at \(\theta=\pi/4\) but not at generic angles. The path can leave the original code space and return at the special endpoint. This invalidates the hypothesis of code preservation at every angle in the continuous-generator argument; it does not invalidate the completed logical T-dagger gate.

Clarification of the earlier explanation: leaving the original code space at intermediate times is not, by itself, a fault-tolerance failure or an overhead cost. A product of one-qubit operations does not spread a single local fault to other qubits. This is a structural error-propagation statement, not a complete hardware noise analysis or a claim that arbitrary syndrome measurements are valid mid-pulse.

The useful 15-qubit code nevertheless lacks a universal transversal set; uniform physical Hadamard does not preserve it. Other fault-tolerant methods are needed for universal computation. Repeating fixed blocks stores more logical qubits at constant rate but leaves the overall distance at three. Making one-logical-qubit blocks arbitrarily large instead loses constant rate. These observations motivate why the paper's family-level result is stronger than a small transversal-T example.

## Open questions and place to resume

The reader's questions asked why the three properties were difficult to combine, why uniform physical T fails on other codes, and what code space, projection, support, and generator mean. The later questions focused on the distinction between physical and logical action and the discrete-to-continuous step in Eastin–Knill. The explanations above record the answers provided, not an independent claim that every prerequisite is mastered. On 2026-10-10 the reader said the discussion helped and requested notes.

- Codex, 2026-10-10 — Next construction question: work through Lemma 3.1 with a small explicit generator matrix, identifying shortening, puncturing, logical labels, and phase coefficients. A worked example would connect the prerequisites back to the paper's mechanism.
- Codex, 2026-10-10 — Next algebra question: why does fivefold binary overlap make the parity-lifting linear systems consistent, and how does normalization create a separately addressable phase for each logical qubit? Revisit Lemmas 4.1–4.2, PDF pp. 8–9.
- Codex, 2026-10-10, following §6 — Practical significance remains unresolved without a syndrome-extraction, decoding, connectivity, and complementary-gate cost model. The asymptotic coding bounds do not answer this.
- Reading queue — arXiv:2609.39556 remains the reader's second selected paper, to be handled after this one.

## Important locations

- PDF pp. 2–5, §§1–1.2: motivation, definition of addressability, prior-work comparison, and concurrent San-José construction.
- PDF pp. 5–7, §§2–3 and Lemma 3.1: CSS states, puncturing/shortening, weighted divisibility, and physical-to-logical phase calculation.
- PDF pp. 8–9, Lemmas 4.1–4.2: lifting coefficients modulo eight and prescribing information-coordinate phases.
- PDF pp. 9–14, Lemmas 4.3–4.4 and Theorem 4.5: AG codes, binary embedding, compression, and X/Z distance bounds.
- PDF pp. 14–16, §§5–6: embedding optimization and open LDPC/architecture questions.
- PDF pp. 26–27, Appendix D and Corollary D.1: explicit embedding and numerical bounds.
- Supporting Eastin–Knill PDF pp. 1–3: error detection, code preservation, Lie-group proof, and transversality corollary; p. 4: scope and alternative fault-tolerant ingredients.
