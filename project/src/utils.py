
import pandas as pd

def get_summary_stats(df, category_col="category", numeric_col="value"):
    summary = df.describe()
    grouped = df.groupby(category_col)[numeric_col].agg(["mean", "sum"])
    return summary, grouped
