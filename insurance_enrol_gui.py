import gradio as gr
import pandas as pd
import joblib
from config import config
# Load model and preprocessor
model = joblib.load(f"{config['MODEL_PATH']}/enrollment_model_.joblib")

def predict(employee_id, age, gender, marital_status, salary, 
            employment_type, region, has_dependents, tenure_years):
    
    input_dict = {
        'employee_id': employee_id, 
        'age': age,
        'gender': gender,
        'marital_status': marital_status,
        'salary': salary,
        'employment_type': employment_type,
        'region': region,
        'has_dependents': has_dependents,
        'tenure_years': tenure_years
    }
    
    df = pd.DataFrame([input_dict])
    
    # Directly using model if it's the pipeline (with preprocessor inside)
    pred = model.predict(df)
    return "✅ Enrolled" if pred[0] == 1 else "❌ Not Enrolled"

# Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label='Employee Id'),
        gr.Number(label='Age'),
        gr.Dropdown(['Female', 'Male', 'Other'], label='Gender'),
        gr.Dropdown(['Single', 'Divorced', 'Married', 'Widowed'], label='Marital Status'),
        gr.Number(label='Salary'),
        gr.Dropdown(['Part-time', 'Full-time', 'Contract'], label="Employment Type"),
        gr.Dropdown(['West', 'Midwest', 'Northeast', 'South'], label='Region'),
        gr.Dropdown(['No', 'Yes'], label='Has Dependents'),
        gr.Number(label='Tenure Years')
    ],
    outputs="text",
    title="Voluntary Insurance Enrollment Predictor"
)

interface.launch()
