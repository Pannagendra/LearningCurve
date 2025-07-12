# validate input data schema, log validation status to MLflow, and raise an exception if invalid
import mlflow
from typing import Dict

def validate_input(data: Dict):
    required_fields = ["age", "bp", "cholesterol"]
    missing = [key for key in required_fields if key not in data]

    with mlflow.start_run():
        if missing:
            mlflow.log_param("status", "fail")
            mlflow.log_param("missing_fields", ",".join(missing))
            raise ValueError(f"Missing fields: {missing}")
        else:
            mlflow.log_param("status", "pass")
            return True

# Example usage
validate_input({"age": 60, "bp": 120})
