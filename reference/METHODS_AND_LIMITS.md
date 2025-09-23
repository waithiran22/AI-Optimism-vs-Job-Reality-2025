
# Methods & Transparency

**Goal.** Compare employment growth in AI‑adjacent occupations with public optimism about AI across EU countries (and later U.S.).

**Definitions.**
- *AI‑adjacent (EU):* ISCO-08 groups OC2 (Professionals) and OC3 (Technicians & associate professionals) as proxies. Where 2‑digit are available, we include 21, 25, 31, 35.
- *AI‑adjacent (US):* SOC 2018 majors 15 (Computer & Mathematical) and 17 (Architecture & Engineering), plus selected 13 (analyst/quant roles). Exact SOC list documented in `ai_exposed_soc.csv`.
- *Sentiment:* Country‑level % optimistic about 2025 and AI (Ipsos Predictions / AI Monitor; Stanford HAI public opinion). Questions differ—used for triangulation, not pooled.

**Normalization.**
- Employment units are thousands of persons (Eurostat). We compute H1 totals (Q1+Q2) for each year and **YoY % growth**: (2025H1−2024H1)/2024H1.
- When comparing regions, we use **YoY %** to avoid level differences.

**Crosswalk.**
- A SOC↔ISCO crosswalk will be added in `soc_isco_crosswalk.csv` (based on official BLS / ILO tables). For now, aggregates are compared within each system.

**Weights.**
- Eurostat aggregates are already weighted. For U.S. CPS microdata, use `WTFINL` person weight; for earnings, use `EARNWT`.

**Caveats.**
- “AI job” is not a native code in ISCO/SOC; these are transparent proxies.
- Survey questions are not identical across sources; we compare patterns, not exact levels.
- Quarterly availability for 2025 means figures are **year‑to‑date (H1)**, not full‑year.
