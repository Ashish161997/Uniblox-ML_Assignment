import requests

url = "http://127.0.0.1:8000/predict"

input_dict = {
    'employee_id': 10002,
    'age': 60,
    'gender': 'Female',
    'marital_status': 'Single',
    'salary': 55122.97,
    'employment_type': 'Part-time',
    'region': 'West',
    'has_dependents': 'No',
    'tenure_years': 1.5
}

response = requests.post(url, json=input_dict)

print("Status:", response.status_code)
print("Response:", response.text)

# If successful:
try:
    print("Prediction:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Could not decode JSON response.")
