import os

import mlflow

mlflow_uri = "http://localhost:5000" # change to your uri + port

mlflow.set_tracking_uri(mlflow_uri)

exp_id = mlflow.set_experiment("mlflow_test1")

mlflow.log_param("param1", "value1")
mlflow.log_param("param2", "value2")

for i in range(10):
    mlflow.log_metric("metric1", value=1/(i+1), step=i)
    
mlflow.log_artifact('./requirements.txt')
mlflow.end_run()