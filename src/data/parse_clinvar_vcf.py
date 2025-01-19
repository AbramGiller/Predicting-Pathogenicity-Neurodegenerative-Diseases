# src/data/parse_clinvar_vcf.py

import pandas as pd
from cyvcf2 import VCF
import config

def parse_clinvar_vcf():
    """
    Parse the ClinVar VCF file and produce a CSV with key fields.
    Each row corresponds to a single (variant, gene) pair if multiple genes are present.
    """
    vcf = VCF(config.CLINVAR_VCF_GZ)
    records = []

    for variant in vcf:
        chrom = variant.CHROM
        pos = variant.POS
        ref = variant.REF
        alt_list = variant.ALT  # Could have multiple ALT alleles
        qual = variant.QUAL if variant.QUAL is not None else 'NotProvided'
        fltr = variant.FILTER if variant.FILTER else 'NotFiltered'

        info = variant.INFO
        clnsig = info.get('CLNSIG', 'NotProvided')  # e.g. "Pathogenic;other"
        clnphen = info.get('CLNPHEN', 'NotProvided')  # phenotype
        geneinfo = info.get('GENEINFO', 'NotProvided')  # e.g. "GENE1:1234|GENE2:5678"

        # If ALT is multi-allelic, you may want multiple rows, but here we show just enumerating each:
        for alt in alt_list or ['None']:
            # Split GENEINFO by '|'
            if geneinfo == 'NotProvided':
                gene_entries = ['NotProvided']
            else:
                gene_entries = geneinfo.split('|')

            for gene_entry in gene_entries:
                if gene_entry == 'NotProvided':
                    gene_symbol, gene_id = ('NotProvided', None)
                else:
                    parts = gene_entry.split(':')
                    if len(parts) == 2:
                        gene_symbol, gene_id = parts
                    else:
                        # Fallback if unexpected format
                        gene_symbol, gene_id = (gene_entry, None)

                record = {
                    'Chromosome': chrom,
                    'Position': pos,
                    'Reference': ref,
                    'Alternate': alt,
                    'Quality': qual,
                    'Filter': fltr,
                    'Clinical_Significance': clnsig,   # keep raw multi-label for now
                    'Phenotype': clnphen,
                    'Gene_Symbol': gene_symbol,
                    'Gene_ID': gene_id
                }
                records.append(record)

    df = pd.DataFrame(records)
    return df

def main():
    df = parse_clinvar_vcf()
    df.to_csv(config.STAGE1_PARSED, index=False)
    print(f"Parsed VCF saved to {config.STAGE1_PARSED}")

if __name__ == "__main__":
    main()
