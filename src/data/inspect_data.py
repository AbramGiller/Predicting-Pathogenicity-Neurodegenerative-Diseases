import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed.csv')

# Convert Chromosome to string
data['Chromosome'] = data['Chromosome'].astype(str)

# Print unique Chromosome values to confirm conversion
print("Unique Chromosome values:", data['Chromosome'].unique())

# Optimize Clinical_Significance as a category
data['Clinical_Significance'] = data['Clinical_Significance'].astype('category')

# Save the cleaned dataset
data.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed_cleaned.csv', index=False)

print("Data types after cleaning:")
print(data.dtypes)
