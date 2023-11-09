
SELECT
    YEAR(OrderDate) AS Year,
    MONTH(OrderDate) AS Month,
    SUM(TotalAmount) AS TotalSales,
    AVG(TotalAmount) OVER (
        ORDER BY YEAR(OrderDate), MONTH(OrderDate)
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS MovingAvgSales
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY Year, Month;
