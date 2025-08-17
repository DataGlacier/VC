from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

# Step 1: Load toy data
iris = load_iris()
X, y = iris.data, iris.target

# Step 2: Train and save model
model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'model.joblib')

print("Model trained and saved!")