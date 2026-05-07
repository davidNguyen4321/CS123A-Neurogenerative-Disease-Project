import pandas as pd

print("Loading SNP data...")

# Load SNP data
snp_df = pd.read_csv("output_data.raw", sep=r"\s+", nrows=100)

print("Loading phenotype data...")

# Load phenotype labels
pheno_df = pd.read_excel("Copy of ADNI_group_ID_data.xlsx")

# Keep only needed columns
pheno_df = pheno_df[['Group ', 'Sample ID']]

# Rename columns for easier merging
pheno_df.columns = ['Group', 'IID']

# Convert IDs to string
snp_df['IID'] = snp_df['IID'].astype(str)
pheno_df['IID'] = pheno_df['IID'].astype(str)

print("Merging datasets...")

# Merge datasets
merged = pd.merge(snp_df, pheno_df, on='IID', how='inner')

print("Merged Shape:", merged.shape)

# Count subjects per group
print("\nSubjects per Group:")
print(merged['Group'].value_counts())

# Save merged data
merged.to_csv("merged_phenotype_data.csv", index=False)

print("\nMerged phenotype dataset created successfully.")