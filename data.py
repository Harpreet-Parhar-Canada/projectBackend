import pandas as pd;

df = pd.read_csv('Com.csv');

x = set(df['Sector']);

print(x);
