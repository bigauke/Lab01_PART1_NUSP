# Análise Exploratória - Camada Silver

## Estatísticas Descritivas (Pagamentos)
```text
       payment_sequential  payment_installments  payment_value
count       103886.000000         103886.000000  103886.000000
mean             1.092679              2.853349     154.100380
std              0.706584              2.687051     217.494064
min              1.000000              0.000000       0.000000
25%              1.000000              1.000000      56.790000
50%              1.000000              1.000000     100.000000
75%              1.000000              4.000000     171.837500
max             29.000000             24.000000   13664.080000
```

## Contagem de Valores Nulos (Pedidos)
```text
order_id                            0
customer_id                         0
order_status                        0
order_purchase_timestamp            0
order_approved_at                   0
order_delivered_carrier_date     1637
order_delivered_customer_date    2819
order_estimated_delivery_date       0
```

## 1. Volume de Pedidos por Status
![Status](grafico1_status.png)

## 2. Métodos de Pagamento
![Pagamentos](grafico2_pagamentos.png)

## 3. Evolução de Vendas ao Longo do Tempo
![Evolução](grafico3_evolucao.png)

## 4. Quantidade de Parcelas Escolhidas
![Parcelas](grafico4_parcelas.png)

## 5. Histograma de Valores de Pagamento
![Valores](grafico5_valores.png)

