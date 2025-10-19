from sklearn.datasets import load_iris
import pandas as pd
import os

# Create data folder
os.makedirs('data', exist_ok=True)

# Load iris dataset
data = load_iris(as_frame=True)

# Combine features and target
df = pd.concat([data.data, pd.Series(data.target, name='target')], axis=1)

# Save to CSV
df.to_csv('data/iris.csv', index=False)

print("✓ Data prepared successfully! Check data/iris.csv")