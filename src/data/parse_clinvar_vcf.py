from cyvcf2 import VCF
import pandas as pd

def parse_clinvar_vcf(vcf_path):
    """
    Parses a ClinVar VCF file and extracts relevant variant information.

    Parameters:
    - vcf_path (str): Path to the ClinVar VCF file.

    Returns:
    - pd.DataFrame: DataFrame containing extracted variant data.
    """
    vcf = VCF(vcf_path)
    records = []
    
    for variant in vcf:
        # Extract basic variant information
        chrom = variant.CHROM
        pos = variant.POS
        ref = variant.REF
        alt = variant.ALT[0] if variant.ALT else None
        id = variant.ID
        qual = variant.QUAL if variant.QUAL is not None else 'Not Provided'
        filter = variant.FILTER if variant.FILTER else 'Not Filtered'
        
        # Extract INFO fields
        info = variant.INFO
        clinical_significance = info.get('CLNSIG', 'Not Provided').replace(';', ',')  # Replace semicolons if any
        phenotype = info.get('CLNPHEN', 'Not Provided').replace(';', ',')  # Replace semicolons if any
        gene_info = info.get('GENEINFO', 'Not Provided')
        
        # Split multiple genes if present
        genes = gene_info.split('|') if gene_info != 'Not Provided' else ['Not Provided']
        
        for gene in genes:
            record = {
                'Chromosome': chrom,
                'Position': pos,
                'Reference': ref,
                'Alternate': alt,
                'ID': id,
                'Quality': qual,
                'Filter': filter,
                'Clinical_Significance': clinical_significance,
                'Phenotype': phenotype,
                'Gene': gene
            }
            records.append(record)
    
    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    vcf_file = "/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/raw/clinvar.bgz.vcf"  # Adjust the path as needed
    df = parse_clinvar_vcf(vcf_file)
    
    # Save the parsed data to a CSV file
    df.to_csv("/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/processed/clinvar_parsed_enhanced.csv", index=False)
    print("ClinVar VCF file has been parsed and saved to data/processed/clinvar_parsed_enhanced.csv")

