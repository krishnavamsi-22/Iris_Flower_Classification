import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np

# Load the dataset
data = pd.read_csv('IRIS.csv')

# Check for data leakage or imbalance
print("Dataset class distribution:")
print(data['species'].value_counts())

# Preprocessing
X = data.iloc[:, :-1]  # Features (sepal and petal measurements)
y = data['species']    # Target variable

# Encode target labels
y = LabelEncoder().fit_transform(y)

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Verify split distribution
print("Training set class distribution:")
print(np.bincount(y_train))
print("Testing set class distribution:")
print(np.bincount(y_test))

# Model training
model = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)
cross_val_scores = cross_val_score(model, X_train, y_train, cv=10)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = np.mean(cross_val_scores)
report = classification_report(y_test, y_pred, target_names=['Setosa', 'Versicolor', 'Virginica'])

# Print results
print(f"Cross-Validated Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n")
print(report)
