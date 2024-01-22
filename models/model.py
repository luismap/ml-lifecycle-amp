# Import required modules:
from joblib import load

# Load the trained model:
model = load('models/current-model/model.joblib')

# Define a function that can be called to generate
# predictions from the model:
def pred_arr_delay(args):
  dep_delay = args["dep_delay"]
  prediction = model.predict([[dep_delay]]).item()
  return {"pred_arr_delay": round(prediction)}

# Example input:
#```
#{"dep_delay": 43}
#```

# Example output:
#```
#{"pred_arr_delay": 38}
#```

pred = pred_arr_delay({"dep_delay":3})
print(pred)
