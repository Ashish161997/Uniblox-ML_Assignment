import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np 
import pandas as pd
from config import config

model = joblib.load(f"{config['MODEL_PATH']}\enrollment_model_.joblib")

app = FastAPI()

class inputData(BaseModel):
    employee_id: int
    age:int
    gender:str
    marital_status:str
    salary:float
    employment_type:str
    region:str
    has_dependents:str
    tenure_years:float

@app.get("/")
def home():
    return {"message":"Employee Enrollment (Insurance) Prediction API"}

@app.post("/predict")
async def predict(data: inputData):
    try:
        print("Received data:", data)
        input_dict = data.model_dump()
        print("Input dict:", input_dict)

        df = pd.DataFrame([input_dict])
        print("DataFrame:\n", df)

        prediction = model.predict(df)
        print("Prediction:", prediction)

        return {"enrollment_prediction": int(prediction[0])}
    
    except Exception as e:
        print("Error during prediction:", str(e))
        return {"error": str(e)}


