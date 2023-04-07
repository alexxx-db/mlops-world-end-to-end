import os
import mlflow

mlflow.set_tracking_uri("databricks")
os.environ["DATABRICKS_HOST"] = "https://adb-7851734333608688.8.azuredatabricks.net//"
os.environ["DATABRICKS_TOKEN"] = "dapi919854b931d50edf9a4a77b1b1ac40b3-2"

# set experiment
experiment_path = "/Users/alex.barreto@databricks.com/experiments/leclub1"
mlflow.set_experiment(experiment_path)

# tracking
with mlflow.start_run(run_name="Training") as run:
    mlflow.set_tag("action", "test2222")
    mlflow.log_metric("acc", 0.99)
    mlflow.log_param("param", "my value")
