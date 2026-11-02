# Power BI dashboard build guide
1. Run `python src/analyze_retail.py` first.
2. Open Power BI Desktop → Home → Get data → Text/CSV.
3. Import `data/processed/cleaned_sales.csv`.
4. Set InvoiceDate to Date/Time, Quantity to Whole Number, UnitPrice and LineRevenue to Decimal Number, and invoice/product/customer identifiers to Text.
5. Save as `powerbi/Retail_Sales_Dashboard.pbix`.

## DAX measures
```DAX
Total Revenue = SUM(cleaned_sales[LineRevenue])
Total Invoices = DISTINCTCOUNT(cleaned_sales[InvoiceNo])
Unique Customers = DISTINCTCOUNT(cleaned_sales[CustomerID])
Units Sold = SUM(cleaned_sales[Quantity])
Average Invoice Revenue = DIVIDE([Total Revenue], [Total Invoices], 0)
Revenue per Customer = DIVIDE([Total Revenue], [Unique Customers], 0)
```
Replace `cleaned_sales` if Power BI uses a different table name.

## Dashboard layout
- Title: Online Retail Sales Performance (2010–2011)
- KPI cards: Total Revenue (£), Total Invoices, Unique Customers
- Line chart: YearMonth vs revenue
- Bar chart: top 10 products by revenue
- Bar chart: revenue by country
- Column chart: revenue by weekday
- Optional scatter: Quantity vs LineRevenue
- Slicers: Country, InvoiceDate, Description or StockCode
- Use clear titles and GBP currency formatting.

Capture genuine screenshots of the dashboard, slicers, and fields/measures in Power BI Desktop. This guide is not a `.pbix` file; save the actual report from Power BI Desktop.
