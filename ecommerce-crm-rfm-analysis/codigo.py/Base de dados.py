import pandas as pd

caminho_do_csv = r"C:\Users\Rafael\.cache\kagglehub\datasets\abbas829\ecommerce-sales-dataset\versions\1\ecommerce_sales_analytics_5000.csv"


df = pd.read_csv(caminho_do_csv, encoding="latin-1")
#=======================================================
# ETAPA 2: PROCESSAMENTO & LIMPEZA (PANDAS)
# =======================================================
print("\nIniciando o processamento dos dados do E-commerce...")

df = df.drop_duplicates()

# --- 2. PROCEDIMENTO ÂNCORA (Preencher Região Nula via Customer ID)
# Se houver alguma compra onde a região veio vazia, usamos o 'customer_id' 
# para mapear em qual região esse cliente já comprou antes e preencher o nulo.

# Passo A:  o dicionário âncora (Mapeia ID -> Região onde há dados)
ancora_regioes = (
    df.dropna(subset=['customer_id', 'region'])
    .drop_duplicates(subset=['customer_id'])
    .set_index('customer_id')['region']
    .to_dict()
)

# Passo B: Aplicamos a âncora para salvar os registros nulos de 'region'
df['region'] = df['region'].fillna(df['customer_id'].map(ancora_regioes))


# --- 3. SEGUNDA ÂNCORA: MÉTODO DE PAGAMENTO PREFERENCIAL
# Mesma lógica: se o método de pagamento estiver nulo, assume o padrão do histórico do cliente
ancora_pagamentos = (
    df.dropna(subset=['customer_id', 'payment_method'])
    .drop_duplicates(subset=['customer_id'])
    .set_index('customer_id')['payment_method']
    .to_dict()
)
df['payment_method']

print("\nProcessamento dos dados completo.")
#=======================================================
# ETAPA 3: Exportação para o sqlserver 
# =======================================================

import pyodbc
from sqlalchemy import create_engine
import urllib

print("\n--- Iniciando a carga para o SQL Server ---")

# 1. Configuração dos parâmetros de conexão
# Se o seu banco não tiver senha (autenticação do Windows), deixe trusted_connection=yes
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"          # Ou o nome da sua instância do SQL Server
    "DATABASE=ecommerce_sales;" # COLOQUE O NOME DO SEU BANCO DE DADOS AQUI
    "Trusted_Connection=yes;"
)

# 2. Criando a engine de conexão do SQLAlchemy
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

try:
    # 3. Enviando o DataFrame tratado para o SQL Server
    df.to_sql(name="vendas_ecommerce", con=engine, if_exists="replace", index=False)
    print("🚀 Dados carregados com sucesso no SQL Server!")

except Exception as e:
    print(f"❌ Erro ao carregar dados: {e}")