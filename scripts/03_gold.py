import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def carregar_gold():
    dir_script = os.path.dirname(os.path.abspath(__file__))
    dir_projeto = os.path.dirname(dir_script)
    caminho_silver = os.path.join(dir_projeto, "data", "silver")

    load_dotenv(os.path.join(dir_projeto, ".env"))
    
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")

    string_conexao = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
    engine = create_engine(string_conexao)

    print("Carregando Dimensao Cliente...")
    df_clientes = pd.read_parquet(os.path.join(caminho_silver, "olist_customers_dataset.parquet"))
    df_clientes.to_sql("dim_cliente", con=engine, if_exists="append", index=False)

    print("Carregando Dimensao Produto...")
    df_produtos = pd.read_parquet(os.path.join(caminho_silver, "olist_products_dataset.parquet"))
    colunas_produto = [
        "product_id", "product_category_name", "product_weight_g", 
        "product_length_cm", "product_height_cm", "product_width_cm"
    ]
    df_produtos = df_produtos[colunas_produto]
    df_produtos.to_sql("dim_produto", con=engine, if_exists="append", index=False)

    print("Preparando e Carregando Tabela Fato de Vendas...")
    df_orders = pd.read_parquet(os.path.join(caminho_silver, "olist_orders_dataset.parquet"))
    df_items = pd.read_parquet(os.path.join(caminho_silver, "olist_order_items_dataset.parquet"))

    df_fato = pd.merge(df_orders, df_items, on="order_id", how="inner")
    colunas_fato = [
        "order_id", "order_item_id", "product_id", "customer_id", 
        "seller_id", "price", "freight_value", "order_purchase_timestamp", "order_status"
    ]
    df_fato = df_fato[colunas_fato]
    
    df_fato.to_sql("fato_vendas", con=engine, if_exists="append", index=False, chunksize=10000)

    print("Carga Gold concluida com sucesso.")

if __name__ == "__main__":
    carregar_gold()