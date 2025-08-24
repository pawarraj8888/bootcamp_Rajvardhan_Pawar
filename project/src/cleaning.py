import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df):
    """Fill missing values in numeric columns with median."""
    return df.fillna(df.median(numeric_only=True))

def drop_missing(df, threshold=0.5):
    """Drop columns with missing values above threshold (default 50%)."""
    return df.dropna(axis=1, thresh=int((1-threshold) * len(df)))

def normalize_data(df):
    """Normalize numeric columns using Min-Max scaling. If none, return df unchanged."""
    out = df.copy()
    numeric_cols = out.select_dtypes(include='number').columns

    # nothing to scale
    if len(numeric_cols) == 0:
        return out

    scaler = MinMaxScaler()
    out[numeric_cols] = scaler.fit_transform(out[numeric_cols])
    return out