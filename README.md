# AI Optimism vs Job Reality: A 2025 Global Data Story

**Goal:** Examine whether public optimism about AI aligns with changes in employment for AI-adjacent occupations in Europe (Eurostat) and the U.S. (BLS).

## TL;DR
- EU **AI-adjacent** jobs = ISCO OC2 (Professionals) + OC3 (Technicians). We compute 2025H1 vs 2024H1 growth by country.
- U.S. baseline from BLS Employment Projections (2024–2034), highlighting faster growth in Computer/Math roles.
- Public sentiment from Ipsos Global Trends & Ipsos *Our Life with AI*, triangulated with Stanford HAI Chapter 8.
- We test alignment: **Optimism (%) vs AI-adjacent job growth (%)**.

## Data
- `Eurostat LFS (lfsq_egais)` — quarterly employment by occupation (2023Q1–2025Q2). Place source files in `data/raw/`.
- `BLS National Employment Matrix (XLSX)` and EP 2024–2034 (PDF).
- `Ipsos Global Trends 9th Edition (PDF)`, `Ipsos – Our Life with AI (PDF)`, `Stanford HAI 2025 Ch.8 (PDF)`.
- `PwC Global AI Jobs Barometer 2025 (PDF)` — context (wage premium).

References/helpers live in `/reference` (AI-exposed mappings, ISO3 map, methods note).

## Methods (High level)
1. **EU Employment:** Sum Q1+Q2 to form half-year totals for 2023–2025. Compute YoY % growth for OC2+OC3 by country.
2. **Sentiment:** Extract country-level optimism and AI attitude percentages from Ipsos/HAI → CSV.
3. **Merge:** Harmonize country names (ISO3), then join growth to sentiment.
4. **U.S. Context:** Compare BLS growth projections for AI-adjacent SOCs.
5. **Analysis:** Scatter (optimism vs job growth), with Pearson/Spearman; maps and ranked tables.

> Detailed caveats and normalization choices are in [`reference/METHODS_AND_LIMITS.md`](reference/METHODS_AND_LIMITS.md).

## Repo Structure
```
data/
  raw/            # put source Excel/PDF/CSV here (ignored by git)
  processed/      # small merged CSVs to commit
notebooks/        # analysis notebooks
src/              # reusable functions
visuals/          # exported charts for README/LinkedIn
reference/        # mappings, crosswalk templates, methods note
dashboard/        # (optional) Streamlit app
```

## Reproduce
```bash
# Python 3.10+ recommended
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Open notebooks
jupyter notebook
```

## Planned Outputs
- EU AI-adjacent growth table & map
- U.S. growth vs decline bars (BLS)
- Optimism heatmap (Ipsos)
- **Correlation:** optimism vs job growth (scatter + line)
- PwC wage premium infographic (context)

## Limitations (Short)
- ISCO/SOC are proxies for “AI jobs”; no native AI code.
- Survey questions differ across sources; aligned qualitatively, not pooled.
- 2025 figures are **H1 (Q1+Q2)** year-to-date.

## License
MIT
