WITH sal_max_tb AS (
    SELECT Emp.id, MAX(Emp.sal) AS sal_max
    FROM Emp
    GROUP BY Emp.depid
)

SELECT Emp.name, Dep.name, sal_max_tb.sal_max
FROM Emp
JOIN Dep ON Dep.id = Emp.depid
JOIN sal_max_tb ON sal_max_tb.id = Emp.id
WHERE Emp.sal = sal_max_tb.sal_max 
AND Emp.id = sal_max_tb.id
