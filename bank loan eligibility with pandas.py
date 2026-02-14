import pandas as pd
from functools import reduce

data = {
    "Name": ["Arun", "Bala", "Chitra", "Divya", "Eshan"],
    "Age": [25, 19, 35, 42, 28],
    "Monthly_Income": [40000, 22000, 60000, 80000, 35000],
    "Credit_Score": [720, 640, 690, 750, 610],
    "Existing_Loans": [1, 0, 3, 1, 2],
    "Monthly_Debt": [12000, 8000, 30000, 20000, 18000]
}

df = pd.DataFrame(data)

df["Credit_Category"] = df["Credit_Score"].map(
    lambda x: "Good" if x >= 700 else "Average" if x >= 650 else "Poor"
)

df["DTI_Ratio"] = df.apply(
    lambda row: (row["Monthly_Debt"] / row["Monthly_Income"]) * 100,
    axis=1
)

df["Loan_Status"] = df.apply(
    lambda row: "Eligible" if (
        row["Age"] >= 21 and
        row["Monthly_Income"] >= 30000 and
        row["Credit_Score"] >= 650 and
        row["Existing_Loans"] <= 2 and
        row["DTI_Ratio"] <= 40
    ) else "Not Eligible",
    axis=1
)

eligible_list = list(filter(lambda x: x == "Eligible", df["Loan_Status"]))

total_eligible = reduce(lambda x, y: x + y, [1 for _ in eligible_list], 0)

print(df)
print("Total Eligible Customers:", total_eligible)
