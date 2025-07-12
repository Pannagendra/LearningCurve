# airflow/dags/retrain_pipeline.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("daily_retrain_titanic",
         start_date=datetime(2023, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    retrain = BashOperator(
        task_id="retrain_model",
        bash_command="python /opt/airflow/src/train.py"
    )
