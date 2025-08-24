from __future__ import annotations
from pathlib import Path
import os
import pandas as pd
from dotenv import load_dotenv

# -- Load .env once and expose dirs --
load_dotenv()
DATA_DIR_RAW = Path(os.getenv("DATA_DIR_RAW", "data/raw"))
DATA_DIR_PROCESSED = Path(os.getenv("DATA_DIR_PROCESSED", "data/processed"))
for d in (DATA_DIR_RAW, DATA_DIR_PROCESSED):
    d.mkdir(parents=True, exist_ok=True)

def _ensure_parquet_engine() -> str:
    try:
        import pyarrow  # noqa: F401
        return "pyarrow"
    except Exception:
        try:
            import fastparquet  # noqa: F401
            return "fastparquet"
        except Exception as e:
            raise RuntimeError(
                "Parquet engine not available. Install 'pyarrow' or 'fastparquet'."
            ) from e

def _ensure_parent(path: Path | str) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def write_df(df: pd.DataFrame, path: Path | str) -> Path:
    p = _ensure_parent(path)
    ext = p.suffix.lower()
    if ext == ".csv":
        df.to_csv(p, index=False)
    elif ext == ".parquet":
        _ensure_parquet_engine()
        df.to_parquet(p, index=False)
    else:
        raise ValueError(f"Unsupported extension: {ext}")
    return p

def read_df(path: Path | str, schema: dict[str, str] | None = None, parse_dates: list[str] | None = None) -> pd.DataFrame:
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".csv":
        if schema is None and parse_dates is None:
            return pd.read_csv(p)
        return pd.read_csv(p, dtype=schema, parse_dates=parse_dates)
    elif ext == ".parquet":
        _ensure_parquet_engine()
        return pd.read_parquet(p)
    else:
        raise ValueError(f"Unsupported extension: {ext}")
