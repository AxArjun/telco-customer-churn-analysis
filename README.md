# Telco Customer Churn Analysis & Prediction

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python\&logoColor=white)](https://www.python.org/) [![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white)](https://pandas.pydata.org/) [![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy\&logoColor=white)](https://numpy.org/) [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn\&logoColor=white)](https://scikit-learn.org/) [![SQL](https://img.shields.io/badge/SQL-Analytics-4479A1?logo=mysql\&logoColor=white)]() [![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite\&logoColor=white)](https://www.sqlite.org/) [![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi\&logoColor=black)](https://powerbi.microsoft.com/) [![Random Forest](https://img.shields.io/badge/Random%20Forest-Churn%20Prediction-228B22)]() [![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Predictive%20Analytics-red)]() [![Customer Analytics](https://img.shields.io/badge/Customer-Churn%20Analytics-blue)]() [![Data Visualization](https://img.shields.io/badge/Data%20Visualization-Matplotlib%20%26%20Seaborn-orange)]() [![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter\&logoColor=white)](https://jupyter.org/) [![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00?logo=googlecolab\&logoColor=white)](https://colab.research.google.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Project Status](https://img.shields.io/badge/Status-Completed-success.svg)]() m[![Business Intelligence](https://img.shields.io/badge/Business-Intelligence-0A66C2)]() [![Revenue Analytics](https://img.shields.io/badge/Revenue-Risk%20Analysis-purple)]() [![GitHub](https://img.shields.io/badge/GitHub-Portfolio%20Project-181717?logo=github\&logoColor=white)](https://github.com/)
               
## Overview               

This project delivers an end-to-end Customer Churn Analytics solution using SQL, Python, Machine Learning, and Power BI.

The objective is to identify key drivers of customer churn, quantify revenue risk, predict customer attrition, and provide actionable business recommendations for customer retention.

The project combines:

* SQL-based business analysis
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Prediction
* Interactive Power BI Executive Dashboard

---

## Business Problem

Customer churn directly impacts revenue and profitability in the telecommunications industry.

This project aims to answer:

* Which customers are most likely to churn?
* What factors contribute most to churn?
* How much revenue is at risk?
* Which customer segments should be prioritized for retention?
* What actions can reduce churn and improve customer lifetime value?

---

## Dataset

Telco Customer Churn Dataset

Dataset Size:

* 7,043 customers
* 33 business attributes
* Demographics
* Services subscribed
* Billing information
* Churn indicators
* Customer Lifetime Value (CLTV)

Key Fields:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure Months
* Internet Service
* Contract Type
* Monthly Charges
* Total Charges
* Churn Label
* Churn Score
* CLTV

This dataset is available in kaggle https://www.kaggle.com/datasets/blastchar/telco-customer-churn
---

## Project Architecture

Dataset
↓
SQL Analytics
↓
EDA & Business Insights
↓
Feature Engineering
↓
Random Forest Model
↓
Churn Predictions
↓
Power BI Executive Dashboard

---

## Repository Structure

```text
telco-customer-churn-analysis/

├── data/
│   ├── Telco_customer_churn.xlsx
│   ├── churn_predictions.csv
│   └── feature_importance.csv
│
├── notebooks/
│   ├── 01_sql_analytics.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_churn_prediction.ipynb
│
├── powerbi/
│   ├── Customer churn prediction.pbix
│   └── screenshots/
│
├── src/
│   └── convert_to_csv.py
│
├── LICENSE
└── README.md
```

---

## SQL Analytics

Key business questions answered:

### Contract Type Analysis

Month-to-Month customers exhibited significantly higher churn rates than annual contract customers.

### Revenue Risk Analysis

Revenue exposure was quantified by customer segment and churn category.

### Service Impact Analysis

Customer retention was strongly associated with:

* Online Security
* Tech Support
* Contract Length

### Customer Risk Segmentation

Customers were classified into:

* High Risk
* Medium Risk
* Low Risk

using churn score thresholds.

---

## Exploratory Data Analysis

Performed:

* Missing value analysis
* Distribution analysis
* Churn segmentation
* Correlation analysis
* Revenue analysis
* Customer profile exploration

Key Insights:

* Short tenure customers churn more frequently.
* Month-to-Month contracts are the strongest churn driver.
* Customers lacking Online Security and Tech Support exhibit higher churn rates.
* Fiber Optic customers show elevated churn risk.

---

## Feature Engineering

Implemented:

* Missing value handling
* Data type corrections
* Label encoding
* One-hot encoding
* Feature preparation for machine learning

Generated outputs:

* Model-ready dataset
* Feature importance dataset
* Prediction dataset

---

## Machine Learning

Model Used:

* Random Forest Classifier

Evaluation Metrics:

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 80.7% |
| Precision | 64.1% |
| Recall    | 53.5% |
| F1 Score  | 57.7% |
| ROC-AUC   | 84.3% |

Top Predictive Features:

1. Tenure Months
2. Total Charges
3. Monthly Charges
4. Contract Type
5. Online Security
6. Tech Support
7. Internet Service

---

## Power BI Dashboard

The dashboard contains 7 executive-level pages:

### Executive Summary & Revenue Impact

* Churn KPIs
* Revenue at Risk
* Customer Segmentation

### Churn Drivers

* Contract Analysis
* Service Analysis
* Churn Trends

### Voice of Customer

* Churn Reason Analysis
* Competitor Insights
* Service Quality Insights

### Customer Risk Intelligence

* High-Risk Customer Segmentation
* Churn Score Analysis

### Executive Recommendations

* Strategic Retention Recommendations
* Revenue Protection Opportunities

### AI Churn Insights

* Machine Learning Results
* Feature Importance Analysis

### Retention Simulator

* What-if Analysis
* Revenue Recovery Estimation
* Customer Retention Impact

---

## Business Recommendations

1. Prioritize Month-to-Month customers for retention campaigns.
2. Bundle Online Security and Tech Support services.
3. Target low-tenure customers within their first year.
4. Focus retention efforts on high-risk customer segments.
5. Offer incentives for migration to annual contracts.

---

## Technologies Used

### Analytics

* SQL
* SQLite

### Programming

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Random Forest

### Visualization

* Matplotlib
* Seaborn
* Power BI

---

## Results

The project demonstrates how data analytics and machine learning can be combined to:

* Predict customer churn
* Quantify revenue risk
* Prioritize retention actions
* Improve customer lifetime value
* Support executive decision making

---

## Author

Arjun Ramprasad

## 🤝 Contributing

Contributions, issue tracking, and feature recommendations are highly welcome. Feel free to fork this project, create a feature branch, and submit a pull request!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
