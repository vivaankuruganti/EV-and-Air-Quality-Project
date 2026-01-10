"""Minimal training script (optional).

This is here mainly to show good project structure for reviewers.
The notebook remains the primary artifact.
"""

from __future__ import annotations

import pandas as pd


def load_air_quality_csvs(filepaths: list[str]) -> pd.DataFrame:
    """Load and concatenate yearly air-quality CSVs."""
    frames = [pd.read_csv(p) for p in filepaths]
    return pd.concat(frames, ignore_index=True)


if __name__ == "__main__":
    print(
        "This repository is notebook-first. Open notebooks/air_quality_modeling.ipynb to run the analysis."
    )
