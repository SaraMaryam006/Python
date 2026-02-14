import pandas as pd

data = {
    "EmpID": [101, 102, 103, 104, 105, 106],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [28, 34, 29, 41, 25, 38],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 70000, 65000, 85000, 48000, 90000],
    "City": ["New York", "Chicago", "Boston", "New York", "Chicago", "New York"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

it_employees = df[df["Department"] == "IT"]
print("\nIT Department Employees")
print(it_employees)

high_salary = df[df["Salary"] > 70000]
print("\nEmployees with Salary > 70000")
print(high_salary)

ny_high_salary = df[(df["City"] == "New York") & (df["Salary"] > 80000)]
print("\nNew York Employees with Salary > 80000")
print(ny_high_salary)

selected_data = df.loc[df["Age"] > 30, ["Name", "Department", "Salary"]]
print("\nEmployees Older Than 30 (Selected Columns)")
print(selected_data)
