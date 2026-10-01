#!/usr/bin/env python3
"""Write the analytic provenance-retention reference (not clinical results)."""

import csv


with open("provenance_stress_reference.csv", "w", newline="", encoding="utf-8") as stream:
    writer = csv.writer(stream)
    writer.writerow(
        [
            "provenance_field_missingness_pct",
            "procedure_source_field_retained_pct",
            "duplicate_pair_detectability_reference_pct",
        ]
    )
    for missing in range(0, 100, 10):
        retained = 100 - missing
        writer.writerow([missing, f"{retained:.1f}", f"{retained * retained / 100:.1f}"])

print("Wrote provenance_stress_reference.csv")
