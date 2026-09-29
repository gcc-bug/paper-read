# What exactly generates the four-panel 0918 readout labels?

**Status:** open. **Recorded:** 2026-09-29.

**Origin:** the reader asked how the [four-panel readout figure](../concepts/iq-readout-and-assignment.md) encodes preparation, assignment, amplitude, and error. General physics explains possible constructions, but the original plotting/estimator implementation is missing from the inspected calibration repository.

## What is established

- INI channels distinguish without-π and with-π preparation groups.
- Case 001 has 3,200 samples per preparation.
- Displayed F is the rounded average of displayed F0 and F1.
- Displayed visibility agrees with F0 + F1 − 1.
- `stateErr0/1` differ from 1 − F0/F1, and the plotted `sepErr` values are smaller still.

## What would answer the question

Recover the original plotting and analysis code, its version/configuration, and ideally intermediate arrays for acquisition `00855`. Establish:

1. Whether each panel colors points by preparation, fitted component, classifier output, or another label; explain any filtering between panels.
2. The IQ rotation, translation, projection, and scaling; identify each plotted axis relative to CSV columns.
3. The meaning of the circles, covariance assumptions, component centers, and GMM weights.
4. Exact definitions of SNR, visibility, stateErr, sepErr, F0, and F1, including thresholds and rounding.
5. Whether classification performance is fitted/evaluated on the same samples or independently held out.
6. Whether any measurement independently separates preparation, relaxation, and readout errors.

Reproduce the figure and numbers from the CSV under those settings. Matching displayed arithmetic alone is insufficient. A new classifier can provide a baseline but cannot retroactively establish the original estimator's semantics.

## Dated developments

- **2026-09-29, Codex:** consolidated the discussion and verified general readout references. Blais Eq. (116) and Krantz Sec. V.C support distinguishing fidelity conventions and overlap versus state-transition effects. Neither paper identifies the local estimator. No hardware intervention or new physical acquisition was performed.

Related: [calibration quantities](../concepts/superconducting-qubit-calibration.md), [reading map](../maps/superconducting-qubit-calibration.md).
