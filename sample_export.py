import pandas as pd

# Load first 10 subjects from PLINK raw file
raw = pd.read_csv("output_data.raw", sep=r"\s+", nrows=10)

# Load SNP annotation file
bim = pd.read_csv(
    r"C:\Users\HP\Downloads\ADNI_GO_2_OmniExpress\ADNI_GO_2_Forward_Bin.bim",
    sep=r"\s+",
    header=None,
    names=["Chr", "SNP Name", "Genetic_Distance", "Position", "Allele1", "Allele2"]
)

# Take first 10 SNPs
bim_small = bim.head(10)

# Create clean table
rows = []

for _, snp in bim_small.iterrows():
    for _, subject in raw.iterrows():
        sample_id = subject["IID"]
        snp_name = snp["SNP Name"]

        # Try to find matching SNP genotype column in raw file
        matching_cols = [col for col in raw.columns if col.startswith(snp_name)]

        genotype = subject[matching_cols[0]] if matching_cols else "Not found"

        rows.append({
            "Sample ID": sample_id,
            "SNP Name": snp_name,
            "Allele1 Top": snp["Allele1"],
            "Allele2 Top": snp["Allele2"],
            "Allele1 Forward": snp["Allele1"],
            "Allele2 Forward": snp["Allele2"],
            "Chr": snp["Chr"],
            "Position": snp["Position"],
            "SNP": genotype
        })

output = pd.DataFrame(rows)

output.to_csv("sample_snp_spreadsheet.csv", index=False)

print("Sample SNP spreadsheet created successfully.")