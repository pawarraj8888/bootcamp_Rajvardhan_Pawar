from pathlib import Path
import pandas as pd

def _ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def write_df(df: pd.DataFrame, path: str | Path) -> Path:
    path = Path(path)
    _ensure_parent(path)
    ext = path.suffix.lower()
    if ext == ".csv":
        df.to_csv(path, index=False)
    elif ext == ".parquet":
        try:
            df.to_parquet(path, index=False)
        except Exception as e:
            raise RuntimeError("Parquet write failed. Install 'pyarrow' (preferred) "
                               "or 'fastparquet'.") from e
    else:
        raise ValueError(f"Unsupported extension: {ext}")
    return path

def read_df(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    ext = path.suffix.lower()
    if ext == ".csv":
        return pd.read_csv(path, low_memory=False, parse_dates=True)
    elif ext == ".parquet":
        try:
            return pd.read_parquet(path)
        except Exception as e:
            raise RuntimeError("Parquet read failed. Install 'pyarrow' or 'fastparquet'.") from e
    else:
        raise ValueError(f"Unsupported extension: {ext}")
