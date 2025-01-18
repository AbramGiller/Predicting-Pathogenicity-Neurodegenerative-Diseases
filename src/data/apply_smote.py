import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_chromosome_encoded.csv')

# Separate features (X) and target variable (y)
X = data.drop(columns=['Clinical_Significance_Encoded'])
y = data['Clinical_Significance_Encoded']

# Keep only numeric columns in X
X_numeric = X.select_dtypes(include=['float64', 'int64'])

# Handle missing values (imputation with the median)
X_numeric = X_numeric.fillna(X_numeric.median())

# Split data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42, stratify=y)

# Apply SMOTE to the training data
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Save the resampled training data
X_train_smote = pd.DataFrame(X_train_smote, columns=X_train.columns)
y_train_smote = pd.Series(y_train_smote, name='Clinical_Significance_Encoded')

X_train_smote.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/X_train_smote.csv', index=False)
y_train_smote.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/y_train_smote.csv', index=False)

# Save the test data (unchanged)
X_test.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/X_test.csv', index=False)
y_test.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/y_test.csv', index=False)

print("SMOTE applied. Resampled training data saved to the processed folder.")
