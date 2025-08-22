from __future__ import annotations
import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    # include='all' so we see categorical counts too
    return df.describe(include='all')

def save_summary(summary: pd.DataFrame, path: str) -> None:
    summary.to_csv(path, index=True)
