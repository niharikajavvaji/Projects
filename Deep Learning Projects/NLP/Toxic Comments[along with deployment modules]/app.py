# predict.py
import pickle
import sys

# Load model
with open("toxic_comments_model.pkl", "rb") as f:
    model = pickle.load(f)

# Take arguments from the command line
input_data = [[float(x) for x in sys.argv[1:]]]
prediction = model.predict(input_data)
print(f"Result: {prediction}")
