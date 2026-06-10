SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;
SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC;
SELECT
fund_house,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY fund_house
ORDER BY total_funds DESC;