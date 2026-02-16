#📊 Dirty Cafe Sales Analysis — From Messy Data to Business Insights**

This project presents an end-to-end data analysis case study on a synthetic 10,000-row “Dirty Cafe Sales” dataset, focusing on transforming corrupted transactional data into actionable business intelligence.

The dataset contained:

•	Type mismatches (numeric fields stored as text with "ERROR" values)
•	Missing categorical and numerical values
•	Logical inconsistencies (negative prices, invalid totals)

Instead of discarding corrupted rows, this project emphasizes data recovery, statistical imputation, and logical inference to preserve business value.

**🔍 Project Objectives**

•	Clean and standardize inconsistent transactional data
•	Apply statistically sound imputation techniques (Mode imputation)
•	Implement logical inference to reconstruct missing financial values
•	Perform Exploratory Data Analysis (EDA)
•	Extract business-level insights for operational and revenue optimization

**🛠 Technical Approach**

1️⃣ Data Cleaning & Type Enforcement

•	Converted corrupted numeric columns using pd.to_numeric(errors="coerce")
•	Parsed datetime columns with pd.to_datetime()
•	Identified and handled null patterns systematically

2️⃣ Missing Data Strategy

•	Mode imputation for categorical variables (Item, Location, Payment Method)
•	Preserved statistical distribution of high-frequency retail transactions

3️⃣ Logical Revenue Reconstruction

Implemented rule-based inference:

_Total Spent = Quantity × Price_

Recovered hundreds of incomplete transactions without data leakage.

4️⃣ Exploratory Data Analysis

Generated business-focused visualizations:

•	Sales volume by product
•	Revenue by service type (Takeaway vs In-store)
•	Monthly revenue trend analysis

**📈 Key Business Insights**

•	Juice significantly outperforms other products in volume → inventory & product expansion opportunity
•	Takeaway drives nearly 2× revenue vs in-store → operational optimization priority
•	Seasonal peaks in June & October; dip in February → predictive staffing & promotional strategy opportunity

**🎯 Business Impact**

This project demonstrates how disciplined data preprocessing directly influences strategic decisions:

•	Inventory optimization
•	Revenue stream prioritization
•	Operational planning
•	Seasonal forecasting

**🧰 Tech Stack**

•	Python
•	Pandas
•	NumPy
•	Matplotlib / Seaborn
•	Jupyter Notebook

**👩‍💻 About**

I’m a Software Engineering graduate specializing in Artificial Intelligence and Machine Learning, focused on building interpretable, data-driven systems that connect analytics with real-world decision-making.

If you're hiring for AI/ML or Data roles, I’d be glad to connect.
