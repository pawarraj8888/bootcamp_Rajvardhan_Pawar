
## Formats Used
- **CSV**: simple, human-readable, works everywhere but can lose type fidelity (e.g., dates load as strings).  
- **Parquet**: efficient, columnar format that preserves dtypes and is faster/smaller. Requires either `pyarrow` or `fastparquet`.  

Using both formats allows compatibility (CSV) and reproducibility + efficiency (Parquet).

## How Code Reads/Writes
- `src/io_utils.py` provides:
  - `write_df(df, path)` → saves DataFrame to CSV or Parquet, based on file extension.  
  - `read_df(path, schema=None, parse_dates=None)` → loads DataFrame, with options to enforce column dtypes for CSV.  
- The notebook imports `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` from `.env` so paths are environment-driven, not hardcoded.  
- Validation in the notebook confirms both formats reload correctly, showing why Parquet is recommended for reproducible storage.
