import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DADOS_SIES = BASE_DIR / "logs" / "sies.csv"

print("Procurando arquivo em:", DADOS_SIES)

df = pd.read_csv(DADOS_SIES, sep=";", encoding="cp1252")

#print(df.head())

#print(df.shape) # 137,914 linhas e 8 colunas

#print(df.columns) # ['TX_SIGLA', 'IBGE', 'TX_INSUMO', 'ANO', 'MES', 'QTDE', 'ORIGEM', 'TX_AREA'] -- string

#print(df.info()) # nenhum nulo

#print(df.isnull().sum()) #0 nulos

#print(df.describe())

#descobrir quantidade de amostras dos insumos
"""""
pd.set_option("display.max_rows", None)
print(df["TX_INSUMO"].value_counts())

"""

#print(df.shape)
#print(df.columns.tolist())
#print(df.info())
#print(df.isna().sum())
#print(df.head(10))

print(df["QTDE"].sum())
print(df["QTDE"].mean())



