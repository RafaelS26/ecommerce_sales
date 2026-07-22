use ecommerce_sales;


--- Faturamento Total e Volume de Vendas
SELECT 
    COUNT(*) AS total_pedidos,
    SUM(quantity) AS total_itens_vendidos,
    ROUND(SUM(revenue), 2) AS faturamento_total,
    ROUND(AVG(revenue), 2) AS ticket_medio
FROM vendas_ecommerce;

--- Desempenho por Categoria de Produto
SELECT 
    COUNT(*) AS total_pedidos,
    SUM(quantity) AS total_itens_vendidos,
    ROUND(SUM(revenue), 2) AS faturamento_total,
    ROUND(AVG(revenue), 2) AS ticket_medio
FROM vendas_ecommerce;


--- Análise de Vendas por Região 
SELECT 
    product_category,
    COUNT(*) AS quantidade_pedidos,
    SUM(quantity) AS itens_vendidos,
    ROUND(SUM(revenue), 2) AS faturamento_categoria,
    ROUND((SUM(revenue) / (SELECT SUM(revenue) FROM vendas_ecommerce)) * 100, 2) AS percentual_do_faturamento
FROM vendas_ecommerce
GROUP BY product_category
ORDER BY faturamento_categoria DESC;



--- Preferência de Métodos de Pagamento 
SELECT 
    region,
    COUNT(*) AS total_pedidos,
    ROUND(SUM(revenue), 2) AS faturamento_regional,
    ROUND(AVG(delivery_days), 1) AS media_dias_entrega
FROM vendas_ecommerce
GROUP BY region
ORDER BY faturamento_regional DESC;

--- Preferência de Métodos de Pagamento /2 
SELECT 
    payment_method,
    COUNT(*) AS total_utilizacoes,
    ROUND(SUM(revenue), 2) AS faturamento_total,
    ROUND(AVG(revenue), 2) AS valor_medio_por_pedido
FROM vendas_ecommerce
GROUP BY payment_method
ORDER BY total_utilizacoes DESC;

--- Comportamento Temporal (Vendas por Mês/Ano)

SELECT 
    YEAR(TRY_CONVERT(DATE, order_date, 101)) AS ano,
    MONTH(TRY_CONVERT(DATE, order_date, 101)) AS mes,
    COUNT(*) AS total_pedidos,
    ROUND(SUM(revenue), 2) AS faturamento_mensal
FROM vendas_ecommerce
GROUP BY 
    YEAR(TRY_CONVERT(DATE, order_date, 101)), 
    MONTH(TRY_CONVERT(DATE, order_date, 101))
ORDER BY 
    ano DESC, 
    mes DESC;