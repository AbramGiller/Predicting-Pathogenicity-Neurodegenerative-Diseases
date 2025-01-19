# src/data/encode_features.py

import pandas as pd
import numpy as np
import config

def map_clnsig(raw_label):
    """
    Given a raw CLNSIG string which might contain multiple labels, return a single label.
    Priority: Pathogenic > Likely_pathogenic > Benign > ...
    Adjust as desired.
    """
    # Split multi-label by ';'
    labels = raw_label.split(';') if raw_label != 'NotProvided' else ['Uncertain_significance']
    labels = [l.strip() for l in labels]

    # Example priority logic
    if any("pathogenic" in l.lower() for l in labels):
        return 2  # Pathogenic
    if any("benign" in l.lower() for l in labels):
        return 0  # Benign
    # fallback
    return 1  # uncertain or conflicting

def encode_clinical_significance(df):
    df['Clinical_Significance_Encoded'] = df['Clinical_Significance'].apply(map_clnsig)
    # Drop original if you don’t need it
    df.drop(columns=['Clinical_Significance'], inplace=True)
    return df

def handle_missing_values(df):
    # If you prefer a numeric median fill, first pick numeric columns:
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # For object columns, you might fill with 'NotProvided' or some placeholder
    obj_cols = df.select_dtypes(include=[object]).columns
    df[obj_cols] = df[obj_cols].fillna('NotProvided')

    return df

def main():
    df = pd.read_csv(config.STAGE1_PARSED)
    
    # Encode clinical significance
    df = encode_clinical_significance(df)
    
    # Handle missing values
    df = handle_missing_values(df)

    # Save interim dataset
    df.to_csv(config.STAGE2_ENCODED, index=False)
    print(f"Feature-encoded dataset saved to {config.STAGE2_ENCODED}")

if __name__ == "__main__":
    main()
