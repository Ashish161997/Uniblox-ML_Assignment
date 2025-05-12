## 📌 Problem-Statement

As part of a company-wide modernization initiative, a new voluntary insurance product is being piloted. The business wants to use ML to predict whether an employee will opt in to this product using demographic and employment-related data.

---

## 🚀 Getting Started


### 📦 Install Dependencies

Before running the interfaces, install the required Python packages:

```bash
pip install -r requirements.txt
```

## 🧪 How to Run

### Option 1 🖼️ GUI Interface (Gradio)

Run the Gradio interface:

```bash
python insurance_enrol_gui.py
```

### Option 2 🌐 API Interface (FastAPI)

Start the API server:

```bash
cd RESTAPI_
uvicorn main:app --reload

#In request_.py, specify the parameters based on your chosen configuration.

python request_.py
```


### 📊 EDA and Modeling

All Exploratory Data Analysis, feature engineering, and model selections (ML & DL) are documented in:

**`Uniblox-ML home assignment.ipynb`**

This notebook includes:

- 🔍 **Data Cleaning & Transformations**
- 📈 **Feature Significance** (p-values, correlation)
- 🤖 **Model Comparison**:
  - Logistic Regression
  - Random Forest
  - Deep Neural Network (PyTorch)
- 📊 **Evaluation Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC AUC
- 🔬 **Feature Importance Analysis**:
  - RandomForest-based importance

---

### ✅ Evaluation Metrics (Best Model)

| Metric     | Score |
|------------|-------|
| Accuracy   | 0.999 |
| Precision  | 0.998 |
| Recall     | 1.000 |
| F1 Score   | 0.999 |
| ROC AUC    | 1.000 |
