---

## 2️⃣ Sales Prediction Project (Linear Regression + Streamlit + FastAPI)

```markdown
# Sales Prediction Project

## 📋 Overview
Predict sales based on TV advertisement spending using linear regression. Built a web app with Streamlit and an API using FastAPI for deployment.

## 📈 Dataset
- TV Ads vs Sales dataset.
- Feature: TV advertising budget.
- Target: Sales (in units).

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit (for web app)
- FastAPI (for REST API)

## 🚀 Process
1. **EDA**: Scatter plots, correlation checks between TV ads and sales.
2. **Modeling**:
    - Single feature linear regression: TV ➔ Sales.
    - (Optional) Multiple features could include Radio and Newspaper.
3. **Evaluation**:
    - R² Score, MSE, MAE.
    - Residual analysis and predictions visualization.
4. **Deployment**:
    - Streamlit app for interactive predictions.
    - FastAPI endpoint for API-based predictions.

## 📊 Results
- Strong positive correlation between TV ad spending and sales.
- Model performs well on unseen data.

## ⚙️ How to Run
```bash
Open `Sales_Ads_Prediction.ipynb` for model training.
Run `streamlit run app.py` for web app.
Run `uvicorn main:app --reload` for FastAPI.

