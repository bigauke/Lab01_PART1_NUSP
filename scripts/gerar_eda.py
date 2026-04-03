import os
import pandas as pd
import matplotlib.pyplot as plt

def gerar_eda():
    dir_script = os.path.dirname(os.path.abspath(__file__))
    dir_projeto = os.path.dirname(dir_script)
    
    caminho_silver = os.path.join(dir_projeto, "data", "silver")
    caminho_notebooks = os.path.join(dir_projeto, "notebooks")
    os.makedirs(caminho_notebooks, exist_ok=True)

    df_orders = pd.read_parquet(os.path.join(caminho_silver, "olist_orders_dataset.parquet"))
    df_payments = pd.read_parquet(os.path.join(caminho_silver, "olist_order_payments_dataset.parquet"))

    md_linhas = ["# Análise Exploratória - Camada Silver\n\n"]

    md_linhas.append("## Estatísticas Descritivas (Pagamentos)\n")
    md_linhas.append("```text\n" + df_payments.describe().to_string() + "\n```\n\n")
    md_linhas.append("## Contagem de Valores Nulos (Pedidos)\n")
    md_linhas.append("```text\n" + df_orders.isnull().sum().to_string() + "\n```\n\n")

    # 1. Status
    plt.figure(figsize=(8, 4))
    df_orders['order_status'].value_counts().plot(kind='bar', color='steelblue')
    plt.title('Pedidos por Status')
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_notebooks, 'grafico1_status.png'))
    plt.close()
    md_linhas.append("## 1. Volume de Pedidos por Status\n![Status](grafico1_status.png)\n\n")

    # 2. Pagamentos
    plt.figure(figsize=(8, 4))
    df_payments['payment_type'].value_counts().plot(kind='bar', color='darkorange')
    plt.title('Tipos de Pagamento')
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_notebooks, 'grafico2_pagamentos.png'))
    plt.close()
    md_linhas.append("## 2. Métodos de Pagamento\n![Pagamentos](grafico2_pagamentos.png)\n\n")

    # 3. Evolução temporal
    df_orders['ano_mes'] = df_orders['order_purchase_timestamp'].dt.to_period('M')
    vendas_mes = df_orders.groupby('ano_mes').size()
    plt.figure(figsize=(10, 4))
    vendas_mes.plot(color='green', marker='o')
    plt.title('Evolução de Vendas')
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_notebooks, 'grafico3_evolucao.png'))
    plt.close()
    md_linhas.append("## 3. Evolução de Vendas ao Longo do Tempo\n![Evolução](grafico3_evolucao.png)\n\n")

    # 4. Parcelas
    plt.figure(figsize=(8, 4))
    df_payments['payment_installments'].value_counts().sort_index().plot(kind='bar', color='purple')
    plt.title('Distribuição de Parcelas')
    plt.xlim(0, 12)
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_notebooks, 'grafico4_parcelas.png'))
    plt.close()
    md_linhas.append("## 4. Quantidade de Parcelas Escolhidas\n![Parcelas](grafico4_parcelas.png)\n\n")

    # 5. Valor dos pagamentos
    plt.figure(figsize=(8, 4))
    df_payments[df_payments['payment_value'] < 500]['payment_value'].plot(kind='hist', bins=30, color='firebrick')
    plt.title('Distribuição de Valores (Até R$ 500)')
    plt.tight_layout()
    plt.savefig(os.path.join(caminho_notebooks, 'grafico5_valores.png'))
    plt.close()
    md_linhas.append("## 5. Histograma de Valores de Pagamento\n![Valores](grafico5_valores.png)\n\n")

    caminho_md = os.path.join(caminho_notebooks, "eda_silver.md")
    with open(caminho_md, "w", encoding="utf-8") as f:
        f.writelines(md_linhas)
    
    print("Análise Exploratória concluída. Verifique a pasta notebooks.")

if __name__ == "__main__":
    gerar_eda()