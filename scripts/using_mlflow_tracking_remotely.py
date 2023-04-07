import os
import mlflow

mlflow.set_tracking_uri("databricks")
os.environ["DATABRICKS_HOST"] = "https://adb-7851734333608688.8.azuredatabricks.net//"
os.environ["DATABRICKS_TOKEN"] = ""

# set experiment
experiment_path = "/Users/alex.barreto@databricks.com/experiments/leclub1"
mlflow.set_experiment(experiment_path)

# tracking
with mlflow.start_run(run_name="Training") as run:
    mlflow.set_tag("action", "test2222")
    mlflow.log_metric("acc", 0.99)
    mlflow.log_param("param", "my value")
