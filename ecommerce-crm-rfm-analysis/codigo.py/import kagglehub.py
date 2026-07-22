import os
import kagglehub
import pandas as pd

# ==========================================
# 1. ETAPA DE EXTRAÇÃO (Extract)
# ==========================================
def extrair_dados_kaggle(dataset_name: str) -> str:
    """Baixa o dataset do Kaggle e retorna o caminho do arquivo CSV."""
    try:
        print(f"-> Iniciando o download do dataset: {dataset_name}...")
        path = kagglehub.dataset_download(dataset_name)
        
        # Identifica o arquivo CSV automaticamente
        arquivos = os.listdir(path)
        if not arquivos:
            raise FileNotFoundError("Nenhum arquivo encontrado na pasta baixada.")
            
        file_path = os.path.join(path, arquivos[0])
        print(f"[OK] Dados extraídos com sucesso em: {file_path}")
        return file_path
        
    except Exception as e:
        print(f"[ERRO] Falha na extração dos dados: {e}")
        return None

# ==========================================
# 2. ETAPA DE CARREGAMENTO E VISUALIZAÇÃO
# ==========================================
def carregar_e_validar_dados(file_path: str) -> pd.DataFrame:
    """Carrega o arquivo CSV em um DataFrame e exibe um resumo inicial."""
    if not file_path:
        return None
        
    try:
        df = pd.read_csv(file_path)
        print("\n" + "="*50)
        print("          CONFIRMAÇÃO DOS ARQUIVOS (PREVIEW)       ")
        print("="*50)
        
        print("\n--- Primeiras 5 linhas do Dataset ---\n")
        print(df.head())
        
        print("\n--- Últimas 5 linhas do Dataset ---\n")
        print(df.tail())
        
        print("\n" + "="*50)
        return df
        
    except Exception as e:
        print(f"[ERRO] Falha ao carregar o DataFrame: {e}")
        return None

# ==========================================
# 3. ETAPA DE ANÁLISE DE DADOS (Explore)
# ==========================================
def analisar_dados(df: pd.DataFrame):
    """Executa a lógica de análise de dados."""
    if df is None:
        print("[AVISO] DataFrame vazio. Pulando a análise.")
        return
        
    print("\n" + "#"*50)
    print("                ANÁLISE DE DADOS                  ")
    print("#"*50)
    
    
    # print(df.info())
    # print(df.describe())
    print("-> Pronto para iniciar as análises estatísticas e insights!")


# ==========================================
# EXECUÇÃO DA PIPELINE
# ==========================================
if __name__ == "__main__":
    DATASET = "abbas829/ecommerce-sales-dataset"

    # Executa os passos em sequência (Pipeline)
    caminho_csv = extrair_dados_kaggle(DATASET)
    df_sales = carregar_e_validar_dados(caminho_csv)
    analisar_dados(df_sales)

    
    caminho_real = extrair_dados_kaggle("abbas829/ecommerce-sales-dataset")
print("O CAMINHO CORRETO É:", caminho_real)
    
    
    
