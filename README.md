# Auditable Evidence Boundaries for Validation of Surgical Artificial Intelligence

Public reproducibility archive, version 1.0.

## Scope
This archive supports the validation-evidence analyses reported in the manuscript. It contains frozen aggregate study facts, machine-readable evidence definitions, provenance-stress inputs, and an executable reconstruction of the deterministic Validation Evidence Auditor.

## Critical provenance note
The prior study record preserved the names of the reproducibility files, frozen numerical results, manifest schema, and experimental protocols. The original byte-for-byte Python/CSV files were not available in the current workspace when this archive was assembled. Therefore:
- `data/frozen_results.json` records the frozen reported results.
- executable scripts are **reconstructed implementations** of the documented protocol, not represented as the original source-file bytes.
- synthetic/example manifests are clearly marked and are not clinical observations.

## Not included
Raw surgical images/videos, direct patient identifiers, model weights, or any material that could permit patient re-identification are not redistributed.

## Main frozen facts
17/17 patients crossed the supplied development-validation boundary; reported supplied-split accuracy was 99.0%. A 12/5 patient-disjoint repair was non-estimable for the cutting class. A 13/4 patient-disjoint repair retained all five classes, contained 726 validation clips, and yielded 75.8% accuracy. The 23.2 percentage-point contrast is descriptive, not causal.

The separate frozen local manifest contained 781 PNG records, 476 unique SHA-256 images, 305 repeated records, 254 exact-duplicate hash groups, and 118 cross-prefix hash groups.

## Reproduction
`python code/validation_integrity_auditor.py data/manifest_schema_example.csv --out example_audit.json`

The example manifest is synthetic and is provided only to demonstrate the interface.
The auditor requires nonempty `sample_id` and `clinical_unit_id`, a 64-character
hexadecimal SHA-256 digest, and a `train`, `validation`, `val`, or `test` split
for every row. Invalid rows stop the audit rather than being silently omitted.
`cross_split_hash_groups` counts exact-content hashes observed in more than one
split. `endpoint_support` lists observed evaluation labels only; whether a
prespecified endpoint is estimable requires an external class specification.

Run the regression tests with `python -m unittest discover -s tests -v`.
Run `python code/run_provenance_stress.py` to regenerate the analytic
`provenance_stress_reference.csv` in the current directory.
