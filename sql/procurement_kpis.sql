SELECT SUM(Amount) AS total_spend
FROM raw_procurement_data;

SELECT Supplier_Name, SUM(Amount) AS supplier_spend
FROM raw_procurement_data
GROUP BY Supplier_Name
ORDER BY supplier_spend DESC;

SELECT Category, SUM(Amount) AS category_spend
FROM raw_procurement_data
GROUP BY Category
ORDER BY category_spend DESC;

SELECT Department, SUM(Amount) AS department_spend
FROM raw_procurement_data
GROUP BY Department
ORDER BY department_spend DESC;
