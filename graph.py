import pandas as pd
import matplotlib.pyplot as plt

# Load results CSV
df = pd.read_csv("snp_analysis_results.csv")

# Remove rows with missing correlations
df = df.dropna(subset=["Correlation"])

# Take top 10 strongest correlations
top_df = df.sort_values(by="Correlation", ascending=False).head(10)

# Create labels
labels = top_df["SNP_1"] + " vs " + top_df["SNP_2"]

# Plot
plt.figure(figsize=(12,6))
plt.bar(labels, top_df["Correlation"])

plt.xticks(rotation=45, ha='right')
plt.ylabel("Correlation")
plt.xlabel("SNP Pairs")
plt.title("Top SNP Correlations")

plt.tight_layout()

# Save graph
plt.savefig("snp_correlation_graph.png")

print("Graph created successfully.")