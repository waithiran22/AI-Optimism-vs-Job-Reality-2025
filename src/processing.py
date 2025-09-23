import pandas as pd

def half_year_sum(df, time_col='TIME', value_col='VALUE', group_cols=('GEO',)):
    """Sum Q1+Q2 for each year into H1 totals."""
    out = {}
    for year in (2023, 2024, 2025):
        mask = df[time_col].isin([f"{year}Q1", f"{year}Q2", f"{year}-Q1", f"{year}-Q2"])  # handle both formats
        tmp = (df[mask]
               .groupby(list(group_cols), as_index=False)[value_col]
               .sum()
               .rename(columns={value_col: f"emp_{year}H1"}))
        out[year] = tmp
    # merge 2023/2024/2025
    m = out[2023].merge(out[2024], on=list(group_cols), how='outer').merge(out[2025], on=list(group_cols), how='outer')
    return m

def yoy_cols(df, a='emp_2024H1', b='emp_2025H1', outcol='yoy_25vs24'):
    df[outcol] = (df[b] - df[a]) / df[a] * 100
    return df
