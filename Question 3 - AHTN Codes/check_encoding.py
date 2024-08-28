import pandas as pd

# Specify an alternative encoding
ahtn_2017 = pd.read_csv(r'C:\Users\user\Downloads\AHTN_2017.csv', encoding='ISO-8859-1')
ahtn_2022 = pd.read_csv(r'C:\Users\user\Downloads\AHTN_2022.csv', encoding='ISO-8859-1')

print(ahtn_2017.head())
print(ahtn_2022.head())