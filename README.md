# HR People Analytics — Employee Attrition Analysis

An end-to-end data analytics project analyzing employee attrition patterns using MySQL, Python, and Looker Studio. Built as part of a data analyst portfolio to demonstrate SQL proficiency, data quality practices, exploratory data analysis, and business intelligence dashboard development.

---

## Live Dashboard

[View HR Attrition Dashboard on Looker Studio](https://lookerstudio.google.com/reporting/8bbcbd77-d7c5-4005-b396-5d2cd52b7c80)

---

## Project Overview

**Domain:** HR / People Analytics  
**Dataset:** IBM HR Analytics Employee Attrition Dataset (Kaggle)  
**Records:** 1,470 employees | 35 columns  
**Tools:** MySQL · Python (Pandas, Matplotlib, Seaborn) · Looker Studio  

The business problem: *Why are employees leaving, and who is most at risk?*

This project follows a full analyst workflow — raw data ingestion, SQL exploration, data quality validation, Python EDA, and an interactive BI dashboard for HR leadership.

---

## Business Questions

1. What is the overall attrition rate in the company?
2. Which departments and job roles have the highest attrition?
3. Does overtime drive attrition?
4. Do lower paid employees leave more?
5. What does the high risk employee profile look like?

---

## Key Findings

| Driver | Finding |
|---|---|
| Overall Attrition | 16.12% of employees left (237 out of 1,470) |
| Department | Sales (20.63%) and HR (19.05%) have the highest attrition |
| Job Role | Sales Representatives at 39.76% — nearly 1 in 2 leaving |
| Overtime | Employees working overtime have 3x higher attrition (30.53% vs 10.44%) |
| Income | Employees who left earned 30% less on average (₹4,787 vs ₹6,832) |
| Tenure | Leavers averaged 8.24 years vs 11.86 years for those who stayed |
| Work Life Balance | Employees rating WLB as "Bad" have 31.25% attrition |

**High Risk Profile:** A Sales Representative or Laboratory Technician, working overtime, with low monthly income and poor work-life balance — is the most likely employee to leave.

---

## Project Structure

```
hr-people-analytics/
│
├── data/
│   ├── raw/
│   │   └── hr_attrition.csv          # Original IBM HR dataset
│   └── cleaned/
│       └── hr_attrition_cleaned.csv  # Cleaned dataset (3 constant columns removed)
│
├── charts/
│   ├── bq1_attrition_rate.png
│   ├── bq2_attrition_by_department.png
│   ├── bq2_attrition_by_jobrole.png
│   ├── bq3_attrition_by_overtime.png
│   ├── bq4_income_vs_attrition.png
│   └── bq5_high_risk_profile.png
│
├── hr_attrition.sql                  # SQL exploration & data quality checks
├── hr_eda.ipynb                      # Python EDA notebook
└── README.md
```

---

## Workflow

### Phase 1 — SQL Exploration (MySQL)
- 8 sections covering attrition distribution, department breakdown, job role analysis, overtime impact, income vs attrition, tenure analysis, and work-life balance
- Structured SQL file with section headers, objectives, and business questions per query

### Phase 2 — Data Quality Checks (MySQL)
- Null and missing value checks across all key columns
- Out-of-range value validation (age, income, work-life balance ratings)
- Logical consistency checks (years at company vs total working years)
- Constant column identification — EmployeeCount, Over18, StandardHours flagged for removal

### Phase 3 — EDA & Visualization (Python)
- Loaded cleaned dataset into Pandas
- Dropped 3 constant columns (32 columns retained)
- Built 5 charts answering each business question using Matplotlib and Seaborn

### Phase 4 — BI Dashboard (Looker Studio)
- Connected cleaned CSV via Google Sheets
- Built interactive dashboard with 6 charts and a Department filter
- Created calculated field for Attrition Rate %
- Dashboard is publicly accessible via shareable link

---

## Data Quality Summary

| Check | Result |
|---|---|
| Null values | Zero nulls across all key columns |
| Duplicate records | None found |
| Out-of-range values | All numeric fields within valid ranges |
| Constant columns | 3 identified and removed (EmployeeCount, Over18, StandardHours) |

---

## Dataset

Source: [IBM HR Analytics Employee Attrition Dataset — Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## Other Portfolio Projects

| Project | Tools | Link |
|---|---|---|
| Superstore Global Sales EDA | MySQL · Excel | [GitHub](https://github.com/Star-P1atinum/SUPERSTORE-GLOBAL-SALES---EXPLORATORY-DATA-ANALYSIS) |
| Credit Risk Analysis | MySQL · Excel · Power BI | [GitHub](https://github.com/Star-P1atinum/CREDIT-RISK-ANALYSIS-END-TO-END) |
| HR People Analytics | MySQL · Python · Looker Studio | Current Repo |
