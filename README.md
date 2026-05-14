# CS123A Neurodegenerative Disease Project

## Genomic and Bioinformatics Analysis of Alzheimer’s Disease

### Team Members
- Arhaam Azhari — Computer Science
- David Nguyen — Data Science
- Derek De Luna — Computer Science
- Anish Samanu — Molecular Biology

---

# Project Overview

This project focuses on the genomic and bioinformatics analysis of Alzheimer’s Disease (AD) using data from the Alzheimer’s Disease Neuroimaging Initiative (ADNI) database.

The objective of this project is to investigate potential relationships between genetic variants (SNPs) and neurodegenerative disease groups such as:
- Alzheimer’s Disease (AD)
- Mild Cognitive Impairment (MCI)
- Cognitively Normal (CN)

The project combines:
- Bioinformatics databases
- GWAS genetic datasets
- Python/Pandas analysis
- Statistical testing
- Data visualization

---

# Data Source

Primary dataset:
- ADNI GWAS Dataset (ADNIGO/2)

Additional phenotype/group information:
- ADNI subject identification table

---

# Technologies Used

- Python
- Pandas
- SciPy
- Matplotlib
- PLINK
- Git/GitHub

---

# Project Workflow

## 1. Data Acquisition
- Accessed ADNI database
- Downloaded GWAS genetic datasets
- Extracted PLINK binary files

## 2. Data Processing
- Converted PLINK data into readable format using PLINK
- Loaded SNP data into Python/Pandas
- Processed over 730,000 SNP columns

## 3. Statistical Analysis
- Performed Chi-Square testing
- Performed SNP correlation analysis
- Generated CSV result tables

## 4. Phenotype Integration
- Merged subject diagnosis labels with SNP data
- Categorized subjects into:
  - AD
  - MCI
  - CN

## 5. Visualization
- Generated SNP correlation graphs using Matplotlib

---

# Files Included

## Python Scripts
- `analysis.py`
- `graph.py`
- `inspect_excel.py`
- `phenotype_analysis.py`
- `sample_export.py`

## Output Files
- `sample_snp_spreadsheet.csv`
- `snp_analysis_results.csv`
- `snp_correlation_graph.png`

---

# Key Results

- Successfully processed ADNI GWAS genetic data
- Generated statistical SNP relationship analyses
- Linked phenotype classifications with subject genetic data
- Identified statistically significant SNP associations using Chi-Square testing and correlation analysis

---

# Future Work

- Expand phenotype-based SNP comparisons
- Integrate KEGG pathway analysis
- Investigate Alzheimer’s-related genes such as:
  - APP
  - PSEN1
  - PSEN2
  - APOE
  - SNCA

- Perform larger-scale biomarker and pathway analysis

---

# Course

CS/BIOL 123A — Bioinformatics  
San José State University
