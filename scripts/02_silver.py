import os
import pandas as pd

def processar_silver():
    # Ancorar os caminhos na raiz do projeto
    dir_script = os.path.dirname(os.path.abspath(__file__))
    dir_projeto = os.path.dirname(dir_script)
    
    caminho_raw = os.path.join(dir_projeto, "data", "raw")
    caminho_silver = os.path.join(dir_projeto, "data", "silver")
    
    os.makedirs(caminho_silver, exist_ok=True)
    
    tabelas_foco = [
        "olist_orders_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_products_dataset.csv",
        "olist_customers_dataset.csv",
        "olist_order_payments_dataset.csv"
    ]
    
    for arquivo in tabelas_foco:
        caminho_completo = os.path.join(caminho_raw, arquivo)
        df = pd.read_csv(caminho_completo)
        
        df = df.drop_duplicates()
        
        if arquivo == "olist_orders_dataset.csv":
            colunas_data = [
                "order_purchase_timestamp",
                "order_approved_at",
                "order_delivered_carrier_date",
                "order_delivered_customer_date",
                "order_estimated_delivery_date"
            ]
            for col in colunas_data:
                df[col] = pd.to_datetime(df[col])
            
            df = df.dropna(subset=["order_approved_at"])
        
        nome_parquet = arquivo.replace(".csv", ".parquet")
        caminho_saida = os.path.join(caminho_silver, nome_parquet)
        
        df.to_parquet(caminho_saida, index=False)
        print(f"Tratado e salvo: {nome_parquet}")

if __name__ == "__main__":
    processar_silver()