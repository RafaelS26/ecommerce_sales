use ecommerce_sales;

select table_schema, table_name from information_schema.tables
where table_type ='base table';


exec sp_columns vendas_ecommerce;



WITH rfm_base AS (
    SELECT 
        customer_id,
        MAX(
            COALESCE(
                TRY_CONVERT(DATE, order_date, 120),
                TRY_CONVERT(DATE, order_date, 103),
                TRY_CONVERT(DATE, order_date, 101)
            )
        ) AS ultima_compra,
        COUNT(DISTINCT order_id) AS frequencia,
        SUM(revenue) AS valor_monetario
    FROM vendas_ecommerce
    GROUP BY customer_id
),
rfm_calculado AS (
    SELECT 
        customer_id,
        ultima_compra,
        DATEDIFF(DAY, ultima_compra, (SELECT MAX(ultima_compra) FROM rfm_base)) AS recencia_dias,
        frequencia,
        valor_monetario
    FROM rfm_base
),
rfm_scores AS (
    SELECT 
        customer_id,
        recencia_dias,
        frequencia,
        valor_monetario,
        NTILE(5) OVER (ORDER BY recencia_dias DESC) AS R,
        NTILE(5) OVER (ORDER BY frequencia ASC) AS F,
        NTILE(5) OVER (ORDER BY valor_monetario ASC) AS M
    FROM rfm_calculado
)
SELECT 
    customer_id,
    recencia_dias,
    frequencia,
    valor_monetario,
    R, F, M,
    -- Concatena as notas para fácil leitura (ex: '555', '111')
    CONCAT(R, F, M) AS rfm_score,
    -- Regra de Negócio para CRM & Growth
    CASE 
        WHEN R >= 4 AND F >= 4 AND M >= 4 THEN 'Campeões (VIP)'
        WHEN R >= 3 AND F >= 3 THEN 'Clientes Leais'
        WHEN R >= 4 AND F <= 2 THEN 'Novos Promissores'
        WHEN R <= 2 AND F >= 4 THEN 'Em Risco (Alto Valor)'
        WHEN R <= 2 AND F <= 2 THEN 'Perdidos / Churn'
        ELSE 'Atenção / Acompanhamento'
    END AS segmento_crm
FROM rfm_scores
ORDER BY recencia_dias ASC;