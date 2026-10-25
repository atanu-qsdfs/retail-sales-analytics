# Retail Sales Data Analytics & Business Intelligence
**InternNova Week 6 Capstone | Author: Atanu Manna**

## Dataset
Use the real UCI Online Retail dataset: https://archive.ics.uci.edu/dataset/352/online+retail  
Citation: Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33. License: CC BY 4.0.

The source covers transactions from a UK online retailer between 1 Dec 2010 and 9 Dec 2011. Download `Online Retail.xlsx` from UCI and place it in `data/raw/`. The raw file is intentionally not bundled because it is a large third-party dataset.

## Run
```bash
python -m pip install -r requirements.txt
python src/analyze_retail.py
```
The script creates a cleaned data file, summary tables, an audit JSON and six charts.

## Cleaning rules
Keep raw data unchanged; remove exact duplicate rows; parse dates and numeric fields; flag cancellation invoices beginning with C; exclude cancellations, non-positive quantities and non-positive prices from positive-sales analysis; calculate revenue as Quantity × UnitPrice in GBP. Missing CustomerID values are not fabricated and are excluded only from customer-level analysis. Outliers are flagged, not automatically deleted. Revenue is not profit because the source has no cost data.

## Contents
- `src/analyze_retail.py`: reproducible cleaning, EDA, six visualizations
- `powerbi/POWER_BI_BUILD_GUIDE.md`: DAX measures and dashboard steps
- `reports/GIT_WORKFLOW.md`: commands and three-commit plan
- `reports/FINAL_REPORT_TEMPLATE.md`: report structure and data-derived findings checklist
- `presentation/SLIDE_OUTLINE.md`: presentation outline
- `data/`: put the source file in `raw`; generated outputs go in `processed`
- `visuals/`: generated charts

## Git requirement
Make at least three meaningful commits. Example: `chore: add project structure`, `feat: add cleaning and EDA`, `feat: add charts and dashboard guide`, `docs: add final report and presentation`.

**Integrity note:** This package cannot publish a GitHub repository or create a native Power BI `.pbix` from this environment. Open Power BI Desktop, import the processed CSV, create the dashboard, save the `.pbix`, and take genuine screenshots before claiming those steps are complete.
