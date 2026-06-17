# Telco Customer Churn Analysis & Prediction

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Project%20Status-In%20Progress-orange.svg)]()

An end-to-end data science and machine learning pipeline focused on identifying, analyzing, and predicting customer churn for a telecommunications provider. This repository hosts exploratory workflows, data preprocessing frameworks, and predictive modeling implementations designed to optimize customer retention strategies.

---

## 📌 Project Overview
Customer churn is a critical metric in the highly competitive telecom sector. Retaining an existing customer is significantly more cost-effective than acquiring a new one. This project aims to:
- Conduct thorough **Exploratory Data Analysis (EDA)** to reveal underlying churn drivers.
- Implement robust **Data Preprocessing & Feature Engineering** to handle data anomalies, types, and class imbalance.
- Construct and compare **Supervised & Unsupervised Machine Learning Models** to accurately forecast high-risk churn profiles and segment customer bases.

---

## 🗂 Repository Structure

├── data/
│   ├── raw/                  # Original, unaltered dataset files          
│   └── processed/            # Cleaned, encoded, and scaled data ready for modeling                         
├── notebooks/                        
│   ├── 01_eda_and_visualization.ipynb    # Deep dive analysis & statistical plots                                   
│   └── 02_model_training_evaluation.ipynb # ML experiments & pipeline engineering                   
├── src/                      # Production-ready operational modular scripts                     
│   ├── __init__.py                         
│   ├── data_preprocessing.py # Script for loading, cleaning, and formatting data                     
│   ├── feature_engineering.py# Encoding, scaling, and feature creation                  
│   └── model_pipeline.py     # Model architectures, training, and metrics evaluation              
├── requirements.txt          # Python dependencies required to reproduce environments              
└── README.md                 # Project documentation and guide                                   




## 📊 Dataset Profile

The project utilizes the classic **Telco Customer Churn** dataset (comprising 7,043 customer records with 21 underlying features):

* **Demographics:** Gender, SeniorCitizen, Partner, Dependents.
* **Services Contracted:** PhoneService, MultipleLines, InternetService (DSL/Fiber Optic/No), OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies.
* **Account/Billing Info:** Tenure (months), Contract type (Month-to-month/One year/Two year), PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges.
* **Target Label:** `Churn` (Yes/No - indicating if the customer departed within the last month).



## 🛠 Experimental Workflow & Pipeline

### 1. Preprocessing & Feature Engineering

* **Data Clean-up:** Identification and transformation of missing/whitespace strings in the `TotalCharges` column, handled via numeric coercion and imputation.
* **Dimensionality Reduction:** Dropped irrelevant tracking identifiers (`customerID`) which carry no predictive power.
* **Categorical Transformation:** Encoding of dichotomous and multi-class categorical features using binary mapping and One-Hot Encoding (`pd.get_dummies`).
* **Feature Scaling:** Standardization of numeric continuous values (`tenure`, `MonthlyCharges`, `TotalCharges`) using `StandardScaler` to optimize linear model convergence and distance metrics.

### 2. Predictive Modeling (Planned & In-Progress)

The codebase evaluates multiple modeling methodologies to find the best balance of precision and recall:

* **Supervised Classifiers:** Logistic Regression, Random Forest, and Gradient Boosting Frameworks (XGBoost/LightGBM).
* **Unsupervised Segmentation:** K-Means Clustering on scaled demographics and usage vectors to cluster high-risk and loyal customer profiles.
* **Class Imbalance Handling:** Application of balancing algorithms (e.g., SMOTE or adjusted class weighting) to address the minority churn class (~26%).

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed locally.

### Installation & Environment Setup

1. **Clone the repository:**
``bash
git clone [https://github.com/AxArjun/telco-customer-churn-analysis.git](https://github.com/AxArjun/telco-customer-churn-analysis.git)
cd telco-customer-churn-analysis

``


2. **Create and activate a virtual environment (Recommended):**
``bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

``


3. **Install the required packages:**
``bash
pip install -r requirements.txt

``


## 📈 Running the Project

* To interact with the exploratory work, execute the visual notebooks:
``bash
jupyter notebook notebooks/01_eda_and_visualization.ipynb

``


* Modular components within the `src/` directory can be executed individually or imported into custom workflows once datasets are placed within the local paths.
* 

## 🛠 Technologies & Tools Used

* **Core Engine:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualizations:** Matplotlib, Seaborn, Plotly
* **Machine Learning Infrastructure:** Scikit-Learn, XGBoost



## 📝 Ongoing Commit Roadmap

As this repository is under active development, the following changes are planned for upcoming updates:

* [ ] Integration of hyperparameter tuning using GridSearchCV/RandomizedSearchCV.
* [ ] Comprehensive validation reports (Confusion Matrix, ROC-AUC curve, F1-Score analysis).
* [ ] Adding localized scripts to export trained model pipelines via `pickle`/`joblib`.

## 🤝 Contributing

Contributions, issue tracking, and feature recommendations are highly welcome. Feel free to fork this project, create a feature branch, and submit a pull request!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

``

***

### 💡 Tips for Customization as you work on it:
1. **`requirements.txt`**: Make sure you generate this file in your root folder using `pip freeze > requirements.txt` once your environment is configured.
2. **Model Evaluation Metrics Table**: As soon as you finalize your baseline scores inside your notebook, you can add a markdown results table to the **Predictive Modeling** section to show off your model's performance (Accuracy vs. F1-Score).

```
