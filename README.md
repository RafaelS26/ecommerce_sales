📊 Análise RFM & Segmentação de CRM para E-commerce

Este projeto aplica a metodologia de segmentação RFM (Recência, Frequência e Valor Monetário) em uma base de dados de e-commerce utilizando *SQL Server avançado. O objetivo principal é transformar dados brutos de transações em inteligência acionável de * CRM & Growth para estratégias de retenção e fidelização de clientes.

🛠️ Arquitetura e Engenharia de Dados (SQL)
A consulta foi desenvolvida utilizando conceitos avançados de engenharia de consultas para garantir desempenho, modularidade e tratamento de abordagens:

Tratamento e Sanitização de Dados:

Aplicação defensiva de COALESCE combinada com TRY_CONVERT para padronizar múltiplos formatos de dados heterogêneos (AAAA-MM-DD, DD/MM/AAAA, MM/DD/AAAA), eliminando inconsistências e valores nulos na base.
Modelagem Modular com CTEs (Common Table Expressions):

rfm_base: Agregação primária por cliente (GROUP BY customer_id), calculando os dados da última compra (MAX), o total de pedidos únicos (COUNT DISTINCT) e o faturamento total gerado (SUM).
rfm_calculado: Cálculo da recência em dias via DATEDIFF comparando a última compra com a data máxima registrada no banco de dados.
rfm_scores: Distribuição estatística por quintis utilizando a função de janela NTILE(5) OVER(...) para definir notas de 1 a 5 para os pilares de Recência, Frequência e Valor Monetário.
Regras de Negócio e Categorização de CRM:

Criação da coluna rfm_score via CONCAT (ex: 555, 521, 111).
Classificação condicional (CASE WHEN) para definir segmentos estratégicos de CRM:
Campeões (VIP): R >= 4, F >= 4, M >= 4
Clientes Leais: R >= 3, F >= 3
Novos Promessas: R >= 4, F <= 2
Em Risco (Alto Valor): R <= 2, F >= 4
Perdidos / Churn: R <= 2, F <= 2
📁 Estrutura do Repositório
.
├── dashboard/      # Arquivos e relatórios do Power BI (.pbix)
├── data/           # Conjunto de dados e bases de apoio (.csv)
├── img/            # Capturas de tela e evidências dos resultados
├── sql/            # Scripts SQL de tratamento e modelagem RFM
├── .gitignore      # Arquivos ignorados pelo controle de versão
└── README.md       # Documentação oficial do projeto
