# 👥 Employee Attrition Analysis (Python + SQL + Excel + Power BI)

## 📌 Project Overview
A complete end-to-end HR analytics project. Employee data (deliberately generated messy) is cleaned and explored in **Python**, queried in **SQL**, summarized in an **Excel** dashboard, and finally visualized in an interactive **Power BI** dashboard — identifying what actually drives employee attrition.

## 🎯 Objective
- Clean a realistically messy HR dataset (missing values, duplicates, inconsistent text, invalid values)
- Identify the strongest drivers of employee attrition (department, overtime, satisfaction, tenure, income)
- Flag high-risk employee segments for retention efforts

## 🛠️ Tools & Technologies
- **Python** (pandas) — data cleaning + exploratory data analysis (EDA)
- **SQL** (SQLite) — attrition-driver queries
- **Excel** (openpyxl) — KPI dashboard with charts
- **Power BI** — final interactive dashboard

## 📂 Project Structure
```
├── data/
│   ├── hr_employee_data_raw.csv       → Original messy dataset (410 rows)
│   └── hr_employee_data_cleaned.csv   → Cleaned data (401 rows, used for SQL/Excel/Power BI)
├── python/
│   └── clean_and_analyze.py           → Cleaning (Part A) + EDA (Part B) script
├── sql/
│   ├── hr_attrition.db                → SQLite database
│   └── sql_queries.sql                → 10 analytical queries
├── excel/
│   └── HR_Attrition_Report.xlsx       → KPI dashboard with charts
├── powerbi/
│   └── employees_dashboard.pbix       → Interactive Power BI dashboard
└── README.md
```

## 🔄 Pipeline
```
Raw CSV → Python (clean + EDA) → SQL (query + validate) → Excel (summary report) → Power BI (interactive dashboard)
```

## 🧹 Data Cleaning (`python/clean_and_analyze.py` — Part A)
The raw data was deliberately generated messy. The script:
- Removed 9 exact duplicate rows (410 → 401 rows)
- Standardized text columns (casing, whitespace) across gender, marital status, department, job role, overtime, business travel
- Fixed abbreviation edge cases that Title Case mishandles (e.g. "Hr" → "HR", "It" → "IT")
- Detected and nulled invalid values (ages outside 18–65, negative income)
- Filled missing numeric values with median, missing department with "Unknown"
- Corrected data types

## 🔎 Exploratory Data Analysis (Part B)
Initial pandas-based EDA surfaced the key patterns before deeper SQL analysis:
- Overall attrition rate, attrition by department and overtime status
- Average job satisfaction and income: stayed vs. left
- Correlation of numeric features with attrition

## 📊 Key Insights
| Metric | Value |
|---|---|
| Total Employees | 401 |
| Employees Left | 100 |
| Overall Attrition Rate | 24.94% |
| Attrition Rate (OverTime = Yes) | 41.59% |
| Attrition Rate (OverTime = No) | 18.40% |
| Average Income (Left) | ₹70,778 |
| High-Risk Group (≤2 yrs tenure + low satisfaction) | 41.67% attrition |

## 🗄️ SQL Analysis (`sql/sql_queries.sql`)
10 queries covering: overall summary, department-wise attrition, overtime impact, satisfaction-level attrition, income comparison, age-group attrition, top job roles by attrition, business travel impact, high-risk segment identification, and work-life balance impact.

## 📈 Excel Dashboard
KPI cards (Total Employees, Employees Left, Attrition Rate, Avg Income of Leavers) plus charts breaking down attrition by department, overtime, and job satisfaction.

## 📊 Power BI Dashboard
`powerbi/employees_dashboard.pbix` — an interactive dashboard built on the cleaned dataset, with KPI cards, department/overtime/satisfaction breakdowns, and slicers for drill-down analysis.

## 💡 Business Recommendations
- **Overtime is the single strongest driver** — attrition more than doubles (18.4% → 41.6%) when employees work overtime. Investigate workload distribution in high-overtime departments.
- Employees with **low job satisfaction AND short tenure (≤2 years)** are the highest-risk segment (41.67% attrition) — prioritize early-tenure engagement programs.
- Pay is a factor but not the dominant one — employees who left earned noticeably less on average (₹70,778), suggesting a compensation review for at-risk roles.

## 🚀 How to Reproduce
1. `python python/clean_and_analyze.py` → generates `data/hr_employee_data_cleaned.csv` and prints EDA
2. Load the cleaned CSV into SQLite and run `sql/sql_queries.sql`
3. Open `excel/HR_Attrition_Report.xlsx` to view the Excel dashboard
4. Open `powerbi/employees_dashboard.pbix` in Power BI Desktop to view/edit the interactive dashboard

---
**Author:** [Your Name] | Data Analyst Portfolio Project

**Disclaimer:** This dataset was synthetically generated for learning/portfolio purposes and does not represent real employee data.
