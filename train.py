import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import json
import os

# Load parameters
params = yaml.safe_load(open('params.yaml'))

# Create output folders
os.makedirs('model', exist_ok=True)
os.makedirs('metrics', exist_ok=True)

# Load data
df = pd.read_csv('data/iris.csv')
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=params['split']['test_size'], 
    random_state=params['train']['random_state']
)

# Train model
model = RandomForestClassifier(
    n_estimators=params['train']['n_estimators'],
    random_state=params['train']['random_state']
)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

# Save outputs
joblib.dump(model, 'model/model.pkl')
json.dump({'accuracy': acc}, open('metrics/eval.json', 'w'))

print(f"✓ Model trained! Accuracy: {acc:.2%}")