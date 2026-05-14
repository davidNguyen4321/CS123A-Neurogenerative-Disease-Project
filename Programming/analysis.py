import pandas as pd
from scipy.stats import chi2_contingency

print("Loading data...")

df = pd.read_csv("output_data.raw", sep=r"\s+", nrows=100)

print("Data loaded!")
print("Shape:", df.shape)

snp_cols = df.columns[6:16]

results = []

for i in range(len(snp_cols)):
    for j in range(i + 1, len(snp_cols)):
        snp1 = snp_cols[i]
        snp2 = snp_cols[j]

        table = pd.crosstab(df[snp1], df[snp2])
        chi2, p, dof, expected = chi2_contingency(table)
        corr = df[snp1].corr(df[snp2])

        results.append({
            "SNP_1": snp1,
            "SNP_2": snp2,
            "Chi_square": chi2,
            "p_value": p,
            "Correlation": corr
        })

results_df = pd.DataFrame(results)
results_df.to_csv("snp_analysis_results.csv", index=False)

print("Analysis complete.")
print(results_df.head())