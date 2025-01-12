import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_encoded.csv')

# Perform one-hot encoding on the 'Chromosome' column
chromosome_encoded = pd.get_dummies(data['Chromosome'], prefix='Chromosome')

# Merge the encoded columns back into the dataset
data = pd.concat([data, chromosome_encoded], axis=1)

# Optionally, drop the original 'Chromosome' column
data = data.drop(columns=['Chromosome'])

# Save the updated dataset
data.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_chromosome_encoded.csv', index=False)

print("Chromosome column encoded. Updated data saved to data/processed/clinvar_chromosome_encoded.csv")
