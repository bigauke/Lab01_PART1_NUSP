"""
Script responsável por validar os dados da camada raw (bronze).
Lê os arquivos CSV da pasta 'data/raw/' e exibe a quantidade de linhas e colunas.
"""

import os
import pandas as pd

def validar_bronze():
    # Caminho absoluto para a pasta raiz (voltando um nível a partir de /scripts)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_raw = os.path.join(script_dir, "..", "data", "raw")
    
    if not os.path.exists(caminho_raw):
        print(f"Erro: O diretório '{caminho_raw}' não foi encontrado.")
        return

    arquivos = os.listdir(caminho_raw)
    
    for arquivo in arquivos:
        if arquivo.endswith(".csv"):
            caminho_completo = os.path.join(caminho_raw, arquivo)
            df = pd.read_csv(caminho_completo)
            linhas, colunas = df.shape
            print(f"Arquivo: {arquivo} | Linhas: {linhas} | Colunas: {colunas}")

if __name__ == "__main__":
    validar_bronze()