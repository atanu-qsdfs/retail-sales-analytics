from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"/"Online Retail.xlsx"
OUT=ROOT/"data"/"processed"
VIS=ROOT/"visuals"
OUT.mkdir(parents=True,exist_ok=True); VIS.mkdir(parents=True,exist_ok=True)

def main():
    if not RAW.exists():
        raise FileNotFoundError(f"Download Online Retail.xlsx from https://archive.ics.uci.edu/dataset/352/online+retail and save it to {RAW}")
    raw=pd.read_excel(RAW,engine="openpyxl")
    required=["InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"]
    if not set(required).issubset(raw.columns): raise ValueError(f"Expected columns: {required}")
    audit={"source_rows":int(len(raw)),"missing_before":{str(k):int(v) for k,v in raw.isna().sum().items()},
           "duplicate_rows_before":int(raw.duplicated().sum())}
    df=raw.copy()
    for c in ["InvoiceNo","StockCode","Description","Country"]:
        df[c]=df[c].astype("string").str.strip()
    df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"],errors="coerce")
    for c in ["Quantity","UnitPrice"]: df[c]=pd.to_numeric(df[c],errors="coerce")
    df=df.drop_duplicates().copy()
    df["IsCancellation"]=df["InvoiceNo"].str.upper().str.startswith("C",na=False)
    df["LineRevenue"]=df["Quantity"]*df["UnitPrice"]
    df["YearMonth"]=df["InvoiceDate"].dt.to_period("M").astype("string")
    audit.update({"duplicates_removed":int(audit["duplicate_rows_before"]),"rows_after_dedup":int(len(df)),
                  "missing_after_dedup":{str(k):int(v) for k,v in df.isna().sum().items()},
                  "missing_customer_id_rows":int(df.CustomerID.isna().sum()),
                  "cancellation_rows":int(df.IsCancellation.sum())})
    sales=df[(~df.IsCancellation)&(df.Quantity>0)&(df.UnitPrice>0)&df.InvoiceDate.notna()&df.Description.notna()].copy()
    audit["positive_sales_rows"]=int(len(sales))
    sales["CustomerID"]=sales["CustomerID"].astype("Int64").astype("string")
    sales.to_csv(OUT/"cleaned_sales.csv",index=False)
    monthly=sales.groupby("YearMonth",as_index=False).agg(Revenue_GBP=("LineRevenue","sum"),Units=("Quantity","sum"),Invoices=("InvoiceNo","nunique"),Customers=("CustomerID","nunique"))
    monthly.to_csv(OUT/"monthly_sales.csv",index=False)
    country=sales.groupby("Country",as_index=False).agg(Revenue_GBP=("LineRevenue","sum"),Units=("Quantity","sum"),Invoices=("InvoiceNo","nunique"),Customers=("CustomerID","nunique")).sort_values("Revenue_GBP",ascending=False)
    country.to_csv(OUT/"country_sales.csv",index=False)
    product=sales.groupby(["StockCode","Description"],as_index=False).agg(Revenue_GBP=("LineRevenue","sum"),Units=("Quantity","sum"),Invoices=("InvoiceNo","nunique")).sort_values("Revenue_GBP",ascending=False)
    product.to_csv(OUT/"product_sales.csv",index=False)
    cust=sales.dropna(subset=["CustomerID"]).groupby("CustomerID",as_index=False).agg(Revenue_GBP=("LineRevenue","sum"),Invoices=("InvoiceNo","nunique"),Units=("Quantity","sum"),LastPurchase=("InvoiceDate","max")).sort_values("Revenue_GBP",ascending=False)
    cust.to_csv(OUT/"customer_sales.csv",index=False)
    sales[["Quantity","UnitPrice","LineRevenue"]].describe().to_csv(OUT/"descriptive_statistics.csv")
    corr=sales[["Quantity","UnitPrice","LineRevenue"]].corr(numeric_only=True); corr.to_csv(OUT/"correlation_matrix.csv")
    q1,q3=sales.LineRevenue.quantile([.25,.75]); iqr=q3-q1
    audit.update({"positive_sales_revenue_gbp":float(sales.LineRevenue.sum()),"unique_invoices":int(sales.InvoiceNo.nunique()),
      "unique_customers_nonmissing":int(sales.CustomerID.nunique()),"unique_products":int(sales.StockCode.nunique()),
      "date_min":str(sales.InvoiceDate.min()),"date_max":str(sales.InvoiceDate.max()),
      "line_revenue_iqr_lower":float(q1-1.5*iqr),"line_revenue_iqr_upper":float(q3+1.5*iqr),
      "line_revenue_outlier_rows":int(((sales.LineRevenue<q1-1.5*iqr)|(sales.LineRevenue>q3+1.5*iqr)).sum())})
    (OUT/"analysis_audit.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
    sns.set_theme(style="whitegrid")
    m=monthly.copy(); m["Month"]=pd.to_datetime(m.YearMonth)
    plt.figure(figsize=(10,5)); plt.plot(m.Month,m.Revenue_GBP,marker="o"); plt.title("Monthly Online Retail Revenue"); plt.xlabel("Month"); plt.ylabel("Revenue (£ GBP)"); plt.xticks(rotation=45); plt.tight_layout(); plt.savefig(VIS/"01_monthly_revenue.png",dpi=180); plt.close()
    top=country[country.Country!="United Kingdom"].head(10).sort_values("Revenue_GBP")
    plt.figure(figsize=(10,6)); plt.barh(top.Country,top.Revenue_GBP); plt.title("Top 10 Countries by Revenue (excluding United Kingdom)"); plt.xlabel("Revenue (£ GBP)"); plt.ylabel("Country"); plt.tight_layout(); plt.savefig(VIS/"02_top_countries_ex_uk.png",dpi=180); plt.close()
    top=product.head(10).sort_values("Revenue_GBP"); labels=top.Description.fillna(top.StockCode).astype(str).str.slice(0,38)
    plt.figure(figsize=(10,6)); plt.barh(labels,top.Revenue_GBP); plt.title("Top 10 Products by Revenue"); plt.xlabel("Revenue (£ GBP)"); plt.ylabel("Product"); plt.tight_layout(); plt.savefig(VIS/"03_top_products.png",dpi=180); plt.close()
    sample=sales.sample(min(8000,len(sales)),random_state=42)
    plt.figure(figsize=(9,6)); plt.scatter(sample.Quantity,sample.LineRevenue,alpha=.25,s=12); plt.title("Quantity vs Line Revenue (sample up to 8,000 rows)"); plt.xlabel("Quantity"); plt.ylabel("Revenue (£ GBP)"); plt.tight_layout(); plt.savefig(VIS/"04_quantity_vs_revenue.png",dpi=180); plt.close()
    plt.figure(figsize=(7,5)); sns.heatmap(corr,annot=True,fmt=".2f",cmap="vlag",vmin=-1,vmax=1); plt.title("Correlation Between Numeric Sales Measures"); plt.tight_layout(); plt.savefig(VIS/"05_correlation_heatmap.png",dpi=180); plt.close()
    sales["Weekday"]=sales.InvoiceDate.dt.day_name(); order=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    weekday=sales.groupby("Weekday").LineRevenue.sum().reindex(order)
    plt.figure(figsize=(9,5)); plt.bar(weekday.index,weekday.values); plt.title("Revenue by Day of Week"); plt.xlabel("Day of week"); plt.ylabel("Revenue (£ GBP)"); plt.xticks(rotation=30); plt.tight_layout(); plt.savefig(VIS/"06_weekday_revenue.png",dpi=180); plt.close()
    print(json.dumps({k:audit[k] for k in ["source_rows","rows_after_dedup","positive_sales_rows","positive_sales_revenue_gbp","unique_invoices","unique_customers_nonmissing","unique_products","line_revenue_outlier_rows"]},indent=2))
    print("Outputs created in data/processed and visuals.")
if __name__=="__main__": main()
