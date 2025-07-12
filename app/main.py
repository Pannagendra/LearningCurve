# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn

model = mlflow.sklearn.load_model("mlruns/0/<run_id>/artifacts/model")

app = FastAPI()

class Input(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    Fare: float

@app.post("/predict")
def predict(data: Input):
    input_df = [[data.Pclass, data.Sex, data.Age, data.Fare]]
    prediction = model.predict(input_df)[0]
    return {"survived": int(prediction)}
