# Retail Sales Analysis

** Final Project**  
**Name:** Atanu Manna

## About this project

For this project, I worked with the Online Retail dataset. I used Python to clean the data and understand the sales. I also made charts and a Power BI dashboard to show the results.

## Project aim

The aim of this project is to check:
- How sales changed over time
- Which products had more sales
- Which countries had more sales
- What useful information we can get from the sales data

## Dataset

I used the Online Retail dataset from the UCI Machine Learning Repository.

Dataset link: https://archive.ics.uci.edu/dataset/352/online+retail

The dataset has information such as invoice number, product, quantity, invoice date, unit price, customer ID and country.

## Tools used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI Desktop
- Git and GitHub

## Data cleaning

First, I checked the dataset and its columns. I checked missing values and duplicate rows. I removed duplicate records. I did not use cancelled invoices or rows with zero or negative quantity or price for the positive sales analysis.

I calculated revenue for each row using:

`LineRevenue = Quantity * UnitPrice`

I did not fill missing customer IDs with fake values.

## Analysis

I used Python to find:
- Total revenue
- Monthly sales
- Sales by country
- Sales by product
- Customer sales
- Correlation between some numeric columns
- Possible outliers in line revenue

## Charts

The `visuals` folder has the charts made for this project:

1. Monthly revenue
2. Top countries by revenue
3. Top products by revenue
4. Quantity and revenue
5. Correlation heatmap
6. Revenue by weekday

## Power BI dashboard

The Power BI dashboard is saved in:

`powerbi/Retail_Sales_Dashboard.pbix`

It shows sales KPIs, revenue by country, revenue by product and monthly revenue. It also has a country filter.

## Some findings

- The United Kingdom has the highest revenue in this dataset.
- November 2011 has the highest monthly revenue in the analysed data.
- February 2011 has the lowest monthly revenue in the analysed data.
- Thursday has the highest revenue by weekday.
- DOTCOM POSTAGE is at the top of the product revenue summary.

These findings are based on this dataset only.

## Recommendations

1. The business can check its top-selling products and make sure enough stock is available.
2. The business can study monthly and weekday sales patterns before planning offers or promotions.

## Limitation

This dataset has sales prices but does not have product cost information. So, revenue is not the same as profit. The data is also from an older period.

## How to run the Python file

Install the required libraries:

```bash
pip install -r requirements.txt
```

Put the original Excel dataset in `data/raw/Online Retail.xlsx`.

Then run:

```bash
python src/analyze_retail.py
```

The Python file saves the processed data in `data/processed` and the charts in `visuals`.

## Folder details

- `data/` - dataset and processed files
- `src/` - Python analysis file
- `visuals/` - charts
- `reports/` - final project report
- `powerbi/` - Power BI dashboard
- `presentation/` - project presentation
