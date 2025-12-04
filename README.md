# Caf-Pulse-Analytics


```markdown
# ☕ Café Sales Dashboard — Streamlit

![Dashboard](analysis_output/sales_by_hour_cleaned.png)

## Overview
This project is a **comprehensive sales analysis and dashboard for a cozy neighborhood café**. It aims to help café owners and managers identify **high-performing time slots, popular items, and customer behavior patterns** to boost sales through targeted campaigns and informed decision-making.

The dashboard is built with **Python** and **Streamlit**, and includes advanced data cleaning, cohort analysis, repeat customer insights, and market-basket item co-occurrence analysis.

---

## 🚀 Key Features

- **Data Cleaning & Enhancement**
  - Robust parsing of dates, times, and transaction timestamps.
  - Automatic handling of currency symbols, negative amounts, and numeric inconsistencies.
  - Parsing and canonicalization of item/product names, including splitting multiple items per order.
  - Synthetic generation of `order_id` if missing.

- **Analytics & Insights**
  - **Sales by Hour & Day:** Identify peak business hours.
  - **Heatmaps:** Visualize sales patterns across days and hours.
  - **Top Selling Items:** Highlight best-selling products.
  - **Customer Cohort Analysis:** Understand retention patterns (if customer data exists).
  - **Repeat Customer Summary:** Track loyal customers.
  - **Item Co-occurrence Analysis:** Discover items frequently bought together (market-basket analysis).
  - **Numeric Correlations:** Correlation between numeric fields like amounts, quantities, etc.

- **Interactive Dashboard**
  - Built with **Streamlit**.
  - Display KPIs, tables, and plots.
  - Navigate through cleaned transaction data, top items, and co-occurrence tables.
  - Ready-to-run for local exploration or deployment.

---

## 📂 File Structure

```

cafe_dashboard_streamlit.zip
├── analysis_output/
│   ├── cleaned_transactions.csv
│   ├── exploded_items.csv
│   ├── top_items_enhanced.csv
│   ├── item_cooccurrence.csv
│   ├── cohort_matrix.csv
│   ├── repeat_customer_summary.csv
│   ├── numeric_correlations.csv
│   ├── sales_by_hour_cleaned.png
│   ├── heatmap_day_hour_cleaned.png
│   ├── top_items_cleaned.png
│   ├── streamlit_app.py
│   └── enhanced_report.txt
├── 01KA3C6HDNJ2WD10KGHCJJ111E.xlsx
└── README.md

````

---

## 🛠 Installation & Setup

1. **Clone or extract the project**:

```bash
unzip cafe_dashboard_streamlit.zip
cd analysis_output
````

2. **Create a virtual environment (recommended)**:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
# If requirements.txt is not included, install manually:
pip install pandas numpy matplotlib streamlit
```

4. **Run the Streamlit Dashboard**:

```bash
streamlit run streamlit_app.py
```

---

## 📊 Usage

* Explore **cleaned transactions** and KPIs.
* View **sales trends by hour and day** to determine peak business times.
* Check **top-selling items** and **frequently bought combinations**.
* Analyze **customer retention** and repeat orders (if customer data exists).
* All plots and tables are interactive and downloadable via the Streamlit interface.

---

## 💡 Recommendations

* Use customer identifiers (email/phone) for more accurate cohort analysis.
* Merge similar items using fuzzy matching for cleaner top-items insights.
* Extend the dashboard with **filters by day, hour, or product category** for granular analysis.
* Optionally, deploy online via **Heroku, Streamlit Cloud, or Google Cloud** for remote access.

---

## 📄 Reports

* `enhanced_report.txt`: Summary of cleaning steps, analysis performed, and output files.
* All CSVs can be used for further **Excel analysis or machine learning tasks**.

---

## 🔗 References & Tools

* Python (pandas, numpy, matplotlib)
* Streamlit for dashboard
* Market-basket analysis (item co-occurrence)
* Cohort & repeat customer analysis

---

## ⚡ Conclusion

This project provides a **robust and professional solution for café sales analysis**, enabling managers to make data-driven decisions, boost sales, and improve customer retention. The dashboard is **ready-to-use** and **extensible** for further advanced analytics.
```

