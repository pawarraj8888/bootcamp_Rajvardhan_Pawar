# src/cleaning.py
from __future__ import annotations
from typing import Iterable, Optional
import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols: Optional[Iterable[str]] = None) -> pd.DataFrame:
    """
    Replace NaNs in numeric columns with the column median.
    If cols is None, operate on all numeric columns.
    Returns a *new* DataFrame (no mutation).
    """
    out = df.copy()
    num_cols = out.select_dtypes(include=[np.number]).columns if cols is None else cols
    for c in num_cols:
        if c in out.columns:
            med = out[c].median(skipna=True)
            out[c] = out[c].fillna(med)
    return out

def drop_missing(df: pd.DataFrame, thresh: float = 0.95) -> pd.DataFrame:
    """
    Drop columns with > (1 - thresh) missing fraction.
    Example: thresh=0.95 keeps columns with at least 95% non-null values.
    """
    out = df.copy()
    nonnull_ratio = 1 - out.isna().mean()
    keep = nonnull_ratio[nonnull_ratio >= thresh].index
    return out[keep]

def normalize_data(df: pd.DataFrame, cols: Optional[Iterable[str]] = None, method: str = "zscore") -> pd.DataFrame:
    """
    Normalize numeric columns.
    method='zscore' -> (x - mean) / std
    method='minmax' -> (x - min) / (max - min)
    Non-numeric columns are left unchanged.
    """
    out = df.copy()
    if cols is None:
        cols = out.select_dtypes(include=[np.number]).columns

    for c in cols:
        if c not in out.columns: 
            continue
        s = out[c].astype(float)
        if method == "zscore":
            mu, sd = s.mean(), s.std(ddof=0)
            out[c] = (s - mu) / sd if sd != 0 else 0.0
        elif method == "minmax":
            mn, mx = s.min(), s.max()
            out[c] = (s - mn) / (mx - mn) if mx != mn else 0.0
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out
