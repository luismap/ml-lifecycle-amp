# Parse command-line arguments. This script expects
# one argument: the string `true` or `false`:
import sys

if len(sys.argv) > 1 and sys.argv[1].lower() == 'false':
  fit_intercept = False
else:
  fit_intercept = True

if len(sys.argv) > 2:
  filter_data = int(sys.argv[2])
else:
  filter_data = 400

# Import modules:
import mlflow
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump

mlflow.set_experiment("lineal")
mlflow.start_run()

# Read and prepare data:
flights_pd = pd.read_csv('data/flights.csv')


flights_clean_pd = flights_pd \
  .filter(['dep_delay', 'arr_delay']) \
  .dropna() \
  .loc[flights_pd.dep_delay < filter_data, :]

features = flights_clean_pd.filter(['dep_delay'])
targets = flights_clean_pd.filter(['arr_delay'])

train_x, test_x, train_y, test_y = train_test_split(
  features,
  targets,
  test_size=0.2
)


# Specify the model and train it using the training
# sample:
model = LinearRegression(fit_intercept=fit_intercept)
model.fit(train_x, train_y)


# Evaluate the model using the test sample. Track the
# value of R-squared (rounded to four digits after the
# decimal) to compare experiment results:
r2 = model.score(test_x, test_y)
mlflow.log_metric('R_squared', round(r2, 4))
mlflow.log_param('is_intercept', fit_intercept)
mlflow.log_param('capped_dep_delay_at', filter_data)


# Save the model for future use:
dump(model, 'model.joblib')
mlflow.log_artifact('model.joblib')

mlflow.end_run()
