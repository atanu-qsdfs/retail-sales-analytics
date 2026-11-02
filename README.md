# Retail Sales Analytics

**InternNova — Week 6 Final Data Analytics Project**  
**Author:** Atanu Manna

## Project overview
This project explores the UCI Online Retail transaction dataset to understand sales trends, product performance, and country-level revenue. The analysis uses Python and common data-analysis libraries, with charts and a report prepared for review.

## Objectives
- Prepare transaction data for analysis by removing duplicate rows and excluding cancellations and non-positive sales lines from the positive-sales analysis.
- Calculate revenue as `Quantity × UnitPrice`.
- Explore monthly revenue, product performance, country sales, and sales patterns.
- Communicate findings through charts, a report, and a presentation draft.

## Dataset
The project uses the **Online Retail** dataset from the UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/352/online+retail

Citation: Chen, D. (2015). *Online Retail* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5BW33

## Key analysis notes
- Original records: 541,909
- Duplicate rows removed: 5,268
- Positive-sales rows analyzed: 524,878
- Revenue in the analyzed positive-sales rows: £10,642,110.80
- Unique invoices in the analysis: 19,960
- Identified customers: 4,338

**Important:** Revenue is not profit. The dataset does not provide product costs. Missing customer IDs were not fabricated. These results depend on the cleaning rules described in the report and audit file.

## Repository structure
- `src/` — Python analysis script
- `data/processed/` — processed summary tables and audit information; the full cleaned transaction CSV may be too large for browser upload
- `visuals/` — generated charts
- `reports/` — project report and workflow notes
- `presentation/` — presentation draft and outline
- `powerbi/` — instructions for creating a Power BI report

## Run the analysis
Install the libraries listed in `requirements.txt`, then run:

```bash
python src/analyze_retail.py
```

Place the original UCI workbook at `data/raw/Online Retail.xlsx` before running the script. The script may take time because the source workbook contains over half a million rows.

## Power BI status
This repository includes a Power BI build guide. A native `.pbix` dashboard is **not included** unless separately created and added.

## Deliverables
- Final report PDF in `reports/`
- Charts in `visuals/`
- Presentation draft in `presentation/`
- Processed summary tables in `data/processed/`

