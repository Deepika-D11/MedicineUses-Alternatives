import pandas as pd

file_path = r"medicines_50.csv"
df = pd.read_csv(file_path)  # Corrected path
print("CSV file loaded successfully!")
print(df.columns)  

