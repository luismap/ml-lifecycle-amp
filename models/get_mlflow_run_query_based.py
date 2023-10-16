from mlflow.tracking import MlflowClient
import mlflow

experiment_name = "lineal"

experiment = mlflow.set_experiment(experiment_name)
  
client= MlflowClient()

query = "metrics.R_squared DESC"
runs = client.search_runs(experiment.experiment_id, order_by=[query])
#print(runs)

run = runs[0]

run_id = run.info.run_id

print(run)
print(run.data.metrics)
print(run.data.params)

#dowload the mode for the current experiment
client.download_artifacts(run_id,path=".", dst_path="models/current-model/")