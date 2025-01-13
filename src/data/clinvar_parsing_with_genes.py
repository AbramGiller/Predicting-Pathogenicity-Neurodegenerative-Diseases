import pandas as pd

# Load the cleaned dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed_cleaned.csv')

# Parse the 'Gene' column into 'Gene_Name' and 'Gene_ID'
data[['Gene_Name', 'Gene_ID']] = data['Gene'].str.split(':', expand=True)

# Optional: Convert Gene_ID to numeric (if applicable)
data['Gene_ID'] = pd.to_numeric(data['Gene_ID'], errors='coerce')

# Drop the original 'Gene' column if no longer needed
data = data.drop(columns=['Gene'])

# Save the updated dataset
data.to_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed_with_genes.csv', index=False)

print("Gene column parsed. Updated data saved to data/processed/clinvar_parsed_with_genes.csv")
