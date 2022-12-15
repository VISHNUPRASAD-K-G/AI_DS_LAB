import pandas as pd
csv=pd.read_csv("CSV.csv")
print(csv)
sr=csv.sort_values(["MARK"],ascending=False)
print("\n  SORTED CSV FILE(Descending Order)")
print("    ----------------------------\n\n",sr)
