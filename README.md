# Auditable Evidence Boundaries in Surgical Model Validation

Code and reference tables for the accompanying study (version 1.0).

## Contents
This repository contains a validation-set integrity checker, a sample manifest,
reference tables, and the study results recorded for this release.

## Source of the files
The original Python and CSV files from the study were unavailable when this
release was prepared. The scripts here were written from the recorded methods;
they are not copies of the original files. `data/frozen_results.json` transcribes
the reported results. The sample manifest contains invented records, not
clinical observations.

Clinical images and videos, patient identifiers, and model weights are not
included. The reported study totals cannot be recalculated from this repository
without the underlying clinical files and manifest.

## Results recorded in this release
All 17 patients appeared on both sides of the supplied development/validation
split, for which the reported accuracy was 99.0%. A patient-disjoint 12/5 split
had no validation examples for the cutting class. A 13/4 split retained all five
classes; its 726 validation clips yielded 75.8% accuracy. The 23.2 percentage-
point difference describes two splits and does not establish a causal effect.

A separate local manifest listed 781 PNG files with 476 distinct SHA-256 hashes.
It contained 305 repeated records, 254 duplicate-hash groups, and 118 groups
whose files came from different source prefixes.

## Run the examples
Install the dependency with `pip install -r requirements.txt`, then run:

```bash
python code/validation_integrity_auditor.py data/manifest_schema_example.csv --out example_audit.json
python code/run_provenance_stress.py
python -m unittest discover -s tests -v
```

The checker requires a sample ID, a clinical-unit ID, a 64-character SHA-256
hash, and a valid split (`train`, `validation`, `val`, or `test`) on every row.
It stops if any of these values is missing or invalid. `cross_split_hash_groups`
counts hashes found in more than one split. `endpoint_support` lists labels
observed in the evaluation rows; deciding whether a planned endpoint can be
evaluated also requires the planned class list.
