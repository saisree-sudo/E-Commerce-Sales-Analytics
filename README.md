# E-Commerce Sales Analytics

## Project Overview
An end-to-end beginner-friendly Data Analytics project that analyzes e-commerce sales, profit, products, customers, regions, and discounts.

## Objectives
- Analyze total sales and profit
- Find top-performing products and categories
- Compare regional performance
- Study monthly sales trends
- Analyze discount and profit patterns
- Prepare insights for business decisions

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- SQL / MySQL
- Power BI
- DAX
- Excel
- Git & GitHub

## Workflow
Dataset -> Python Cleaning -> EDA -> SQL Analysis -> Power BI Dashboard -> Insights

## How to Run Python
```bash
pip install -r requirements.txt
cd python
python data_cleaning.py
python eda.py
python analysis.py
```

## Power BI Measures
```DAX
Total Sales = SUM(Orders[Sales])
Total Profit = SUM(Orders[Profit])
Profit Margin = DIVIDE([Total Profit], [Total Sales])
Average Order Value = DIVIDE([Total Sales], DISTINCTCOUNT(Orders[Order_ID]))
```

## Dashboard Pages
1. Executive Overview
2. Product Performance
3. Customer Analysis
4. Business Intelligence

## Resume Description
Developed an end-to-end E-Commerce Sales Analytics solution using Python, SQL and Power BI to analyze sales, profitability, product performance, regional trends and discount patterns.
