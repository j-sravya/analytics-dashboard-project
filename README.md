# Analytics Dashboard Project

## Overview

This project analyzes e-commerce sales performance using Python, SQL, and Power BI concepts to generate business insights and interactive dashboard visualizations.

## Objective

The goal of this project is to understand customer behavior, revenue trends, product performance, and operational metrics using data analytics techniques.

## Key Business Questions

* Which categories generate the highest revenue?
* Which cities contribute most to sales?
* Which products perform best?
* What customer segments are most valuable?
* Which payment methods are most used?
* How do monthly sales trends change over time?

## Tools Used

* Python
* Pandas
* SQL
* Matplotlib
* Jupyter Notebook
* Power BI

## Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Dashboard Design
* Business Insight Generation
* SQL Querying
* KPI Reporting
* Data Visualization

## Project Structure

```text
analytics-dashboard-project/
|
├── README.md
├── requirements.txt
├── data/
│   └── ecommerce_sales_data.csv
├── notebooks/
│   └── ecommerce_sales_analysis.ipynb
├── dashboard/
│   ├── dashboard.pbix
│   └── dashboard_layout_concept.md
├── src/
│   └── analysis.py
├── insights/
│   └── business_insights.md
├── visuals/
│   ├── city_wise_sales.png
│   ├── customer_segment_distribution.png
│   ├── monthly_sales_trend.png
│   ├── payment_method_usage.png
│   ├── profit_by_category.png
│   ├── revenue_by_category.png
│   ├── shipping_type_distribution.png
│   └── top_10_products.png
└── sql/
    └── ecommerce_queries.sql
```

## Dataset

The dataset contains 1,500 synthetic e-commerce order records created for portfolio demonstration. It includes Indian cities and states, customer segments, product categories, payment methods, shipping types, sales values, profit, and delivery performance.

Key columns:

* order_id
* order_date
* customer_id
* customer_segment
* product_category
* product_name
* quantity
* unit_price
* total_sales
* profit
* city
* state
* payment_method
* shipping_type
* delivery_days

## Key KPIs

* Total Revenue: Rs. 19,236,966.82
* Total Profit: Rs. 3,071,051.73
* Total Orders: 1,500
* Average Order Value: Rs. 12,824.64
* Top Category: Electronics
* Best City: Bengaluru
* Most Used Payment Method: UPI

## Key Insights

* Electronics and Fashion categories drive the highest revenue.
* UPI is the most commonly used payment method.
* Bengaluru and Hyderabad contribute strongly to sales.
* Consumer segment generates the largest number of orders.
* Monthly sales show growth during festive and year-end seasons.
* Laptop is the best-performing product by revenue.

## Dashboard Features

* KPI cards for revenue, profit, orders, and average order value
* Monthly trend analysis
* Category and product comparisons
* City-wise sales analysis
* Customer segment analysis
* Payment method and shipping analysis
* Suggested filters for month, city, customer segment, and product category

## Visualizations

The `visuals/` folder contains matplotlib charts for:

* Monthly sales trend
* Revenue by category
* Top 10 products
* City-wise sales
* Customer segment distribution
* Payment method usage
* Profit by category
* Shipping type distribution

## SQL Analysis

The `sql/ecommerce_queries.sql` file contains portfolio-ready SQL queries for revenue, trends, top products, customer segments, city performance, profit, average order value, payment methods, and shipping analysis.

## How to Run

1. Clone the repository.
2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Open the notebook:

```bash
jupyter notebook notebooks/ecommerce_sales_analysis.ipynb
```

4. Run the Python analysis script:

```bash
python src/analysis.py
```

## Power BI Dashboard

The `dashboard/` folder contains a Power BI dashboard concept with four pages:

* Executive Overview
* Sales Analysis
* Customer Insights
* Product Performance

Use `data/ecommerce_sales_data.csv` as the data source in Power BI Desktop and recreate the layout described in `dashboard/dashboard_layout_concept.md`.

## Disclaimer

Dataset is synthetic/sample data created for portfolio demonstration purposes. No web scraping was used.
