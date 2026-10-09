/* =====================================================
   EMPLOYEE ATTRITION ANALYSIS - SQL QUERIES (STEP 2 of 4)
   Database: hr_attrition.db (SQLite)
   Table: employees
   Pipeline: Python -> SQL (yeh file) -> Excel -> Power BI
   ===================================================== */


/* Q1: Overall Headcount and Attrition Summary */
SELECT
    COUNT(*) AS total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees;


/* Q2: Attrition Rate by Department */
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY department
ORDER BY attrition_rate_pct DESC;


/* Q3: Attrition Rate by OverTime Status
   (Kya overtime karne wale employees zyada chhodte hain?) */
SELECT
    over_time,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY over_time;


/* Q4: Attrition Rate by Job Satisfaction Level */
SELECT
    job_satisfaction,
    COUNT(*) AS total_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY job_satisfaction
ORDER BY job_satisfaction;


/* Q5: Average Monthly Income - Stayed vs Left */
SELECT
    attrition,
    ROUND(AVG(monthly_income), 0) AS avg_monthly_income,
    ROUND(AVG(years_at_company), 1) AS avg_years_at_company
FROM employees
GROUP BY attrition;


/* Q6: Attrition by Age Group */
SELECT
    CASE
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 40 THEN '30-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        ELSE '50+'
    END AS age_group,
    COUNT(*) AS total_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY age_group
ORDER BY age_group;


/* Q7: Top 5 Job Roles by Attrition Rate (minimum 10 employees) */
SELECT
    job_role,
    COUNT(*) AS total_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY job_role
HAVING COUNT(*) >= 10
ORDER BY attrition_rate_pct DESC
LIMIT 5;


/* Q8: Attrition by Business Travel Frequency */
SELECT
    business_travel,
    COUNT(*) AS total_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY business_travel
ORDER BY attrition_rate_pct DESC;


/* Q9: Employees with Short Tenure AND Low Satisfaction (high-risk group) */
SELECT
    COUNT(*) AS high_risk_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
WHERE years_at_company <= 2 AND job_satisfaction <= 2;


/* Q10: Work-Life Balance vs Attrition */
SELECT
    work_life_balance,
    COUNT(*) AS total_employees,
    ROUND(SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate_pct
FROM employees
GROUP BY work_life_balance
ORDER BY work_life_balance;
