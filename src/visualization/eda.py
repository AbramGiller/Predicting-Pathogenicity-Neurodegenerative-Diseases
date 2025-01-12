import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_chromosome_encoded.csv')

# Set a style for plots
sns.set(style="whitegrid")

# 1. Target Variable Distribution
plt.figure(figsize=(8, 6))
data['Clinical_Significance_Encoded'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Distribution of Clinical Significance')
plt.xlabel('Clinical Significance (Encoded)')
plt.ylabel('Count')
plt.xticks([0, 1, 2], ['Likely_benign', 'Uncertain_significance', 'Pathogenic'], rotation=45)
plt.show()

# 2. Chromosome Distribution
chromosome_cols = [col for col in data.columns if col.startswith('Chromosome_')]
chromosome_counts = data[chromosome_cols].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
chromosome_counts.plot(kind='bar', color='orange')
plt.title('Variant Distribution Across Chromosomes')
plt.ylabel('Count')
plt.xlabel('Chromosome')
plt.show()

# 3. Top Genes Enriched for Pathogenic Variants
top_genes = data[data['Clinical_Significance_Encoded'] == 2]['Gene_Name'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genes.values, y=top_genes.index, palette='viridis')
plt.title('Top 10 Genes with Pathogenic Variants')
plt.xlabel('Count')
plt.ylabel('Gene Name')
plt.show()

# Select only numeric columns for correlation matrix
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = data[numeric_cols].corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Matrix')
plt.show()
