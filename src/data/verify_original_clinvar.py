from cyvcf2 import VCF

# Path to the original ClinVar VCF file
vcf_file = '/Users/s2222119/Predicting-Pathogenicity-Neurodegenerative-Diseases/data/raw/clinvar.vcf.gz'

# Open the VCF file
vcf = VCF(vcf_file)

# Counters for missing and total values
quality_missing = 0
filter_missing = 0
phenotype_missing = 0
total_variants = 0

for record in vcf:
    total_variants += 1

    # Check 'QUAL' field
    if record.QUAL is None:
        quality_missing += 1

    # Check 'FILTER' field
    if record.FILTER is None or record.FILTER == []:
        filter_missing += 1

    # Check 'Phenotype' field (custom INFO field, update key based on header inspection)
    if 'PHENOTYPE' in record.INFO:
        if not record.INFO.get('PHENOTYPE'):
            phenotype_missing += 1
    else:
        phenotype_missing += 1

# Print results
print(f"Total Variants: {total_variants}")
print(f"Missing Quality: {quality_missing} ({(quality_missing / total_variants) * 100:.2f}%)")
print(f"Missing Filter: {filter_missing} ({(filter_missing / total_variants) * 100:.2f}%)")
print(f"Missing Phenotype: {phenotype_missing} ({(phenotype_missing / total_variants) * 100:.2f}%)")
