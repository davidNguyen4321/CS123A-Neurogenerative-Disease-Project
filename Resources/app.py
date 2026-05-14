from Bio import Align
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

try:
    csvName = input()
    pd.read_csv(csvName)
except Exception as e:
    print(str(e))