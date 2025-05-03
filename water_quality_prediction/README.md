# Water Quality Prediction Project

## 📋 Overview
Predict whether water is potable using classification models based on physicochemical properties. Emphasis on proper preprocessing, modeling, and evaluation.

## 📈 Dataset
- [Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)
- 3276 rows × 10 columns (features include pH, Hardness, Solids, Sulfate, Conductivity, etc.)

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## 🚀 Process
1. **EDA**: Analyzed missing values, feature distributions.
2. **Preprocessing**:
    - Handled missing values with imputation.
    - Normalized features where necessary.
3. **Modeling**:
    - Decision Tree Classifier.
    - Random Forest Classifier.
4. **Evaluation**:
    - Accuracy, Precision, Recall, F1-Score, ROC-AUC.
    - Confusion matrix and ROC curves.

## 📊 Results
- Random Forest outperformed Decision Tree in most evaluation metrics.
- Importance of features like Sulfate and Solids highlighted.

## ⚙️ How to Run
```bash
Open `Water_Quality_Prediction.ipynb` and execute all cells sequentially.
