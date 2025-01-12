import pandas as pd

# Load the cleaned dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed_with_genes.csv')

# Define encoding for Clinical_Significance
clinical_significance_mapping = {
    'Likely_benign': 0,
    'Uncertain_significance': 1,
    'Pathogenic': 2
}

# Map Clinical_Significance to numeric values
data['Clinical_Significance_Encoded'] = data['Clinical_Significance'].map(clinical_significance_mapping)

# Drop rows with unmapped categories (if any)
data = data.dropna(subset=['Clinical_Significance_Encoded'])

# Save the updated dataset
data.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_encoded.csv', index=False)

print("Clinical_Significance encoded. Updated data saved to data/processed/clinvar_encoded.csv")
