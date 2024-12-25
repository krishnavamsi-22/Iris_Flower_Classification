# Iris Flower Classification
This repository contains the implementation of a machine learning model to classify Iris flowers into three species: Setosa, Versicolor, and Virginica.

## Objectives
- Use the Iris dataset to develop a classification model.
- Explore data preprocessing, feature scaling, and hyperparameter tuning.
- Evaluate the model's performance using cross-validation.

## Approach
1. Loaded the Iris dataset and checked for class distribution to ensure balance.
2. Preprocessed the data:
   - Encoded target labels.
   - Scaled feature values using `StandardScaler`.
   - Split the data into training and test sets with stratification.
3. Trained a Random Forest Classifier:
   - Tuned hyperparameters to prevent overfitting.
   - Evaluated performance using 10-fold cross-validation.
4. Achieved results:
   - Cross-validated accuracy: **(Insert Accuracy Here)**%
   - Test set classification report: (Insert report summary).

## Challenges
- Ensuring proper class distribution during splitting.
- Avoiding overfitting while maximizing accuracy.

## Results
The model performed well with (Insert Accuracy Here)% accuracy on the test set.

## Usage
1. Clone the repository.
2. Install required dependencies (`pip install -r requirements.txt`).
3. Run the script: `python iris_classification.py`.
