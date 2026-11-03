import pandas as pd

# Load the employee dataset
df = pd.read_csv('employees.csv')

# Clean column whitespace if present in headers
df.columns = df.columns.str.strip()

# Load department heads dataset
heads_df = pd.read_csv('heads.csv')
heads_df.columns = heads_df.columns.str.strip()

# Display initial data layout
print("Initial Employees DataFrame:")
print(df)

import pandas as pd

# ==========================================
# Q11. Series, DataFrame and exploring a CSV
# ==========================================

# 1. Create a Series and print specified elements on one line
s = pd.Series(["Employee_1", "Employee_2", "Employee_3"], index=["a", "b", "c"])
print(s["b"], s.iloc[2], len(s))

# 2. Create a DataFrame from a list of dictionaries and print it
data = [
    {"item": "pen", "qty": 10},
    {"item": "book", "qty": 4},
    {"item": "bag", "qty": 2}
]
df_items = pd.DataFrame(data)
print(df_items)

# 3. Read employees.csv into df, print first 3 rows, shape and column names on one line
df = pd.read_csv('employees.csv', skipinitialspace=True)
print(df.head(3))
print(df.shape, list(df.columns))

# 4. Print number of duplicate rows and missing values in every column
print(df.duplicated().sum())
print(df.isna().sum())

# ==========================================
# Q12. Clean and convert
# ==========================================

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Convert Bonus ('Bonun') to numeric, fill missing/invalid with 0, and convert to int
df['Bonun'] = pd.to_numeric(df['Bonun'], errors='coerce').fillna(0).astype(int)

# 3. Calculate mean salary (rounded to a whole number) and fill missing salary
fill_val = int(round(pd.to_numeric(df['Salary'], errors='coerce').mean()))
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce').fillna(fill_val).astype(int)

# 4. Convert JoinDate to datetime and add Year, Weekday, and Years columns
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
df['Year'] = df['JoinDate'].dt.year
df['Weekday'] = df['JoinDate'].dt.day_name()
df['Years'] = (pd.Timestamp("2026-01-01") - df['JoinDate']).dt.days // 365

# 5. Print the fill value, shape, and dtypes of Salary and Bonus on one line, then first 4 rows
print(fill_val, df.shape, df['Salary'].dtype, df['Bonun'].dtype)
print(df[['EmpID', 'Year', 'Weekday', 'Years']].head(4))

# ======================================================
# Q13. New column, filtering, indexing and categories
# ======================================================

# 1. Add the column Net = Salary + Bonus
df['Net'] = df['Salary'] + df['Bonun']

# 2. Print EmpID, Name and Net where Department is IT and Net > 50000
print(df.loc[(df['Department'] == 'IT') & (df['Net'] > 50000), ['EmpID', 'Name', 'Net']])

# 3. Print type names of df["Name"] and df[["Name"]] on one line, then df.loc[0, "Name"] and df.iloc[1, 1]
print(type(df['Name']).__name__, type(df[['Name']]).__name__)
print(df.loc[0, 'Name'], df.iloc[1, 1])

# 4. Define band(n) function, add Band column with apply, and convert to ordered Categorical
def band(n):
    if n >= 65000:
        return "High"
    elif n >= 50000:
        return "Mid"
    else:
        return "Low"

df['Band'] = df['Net'].apply(band)
df['Band'] = pd.Categorical(df['Band'], categories=["Low", "Mid", "High"], ordered=True)

# 5. Sort by Band (highest first) then EmpID (ascending), print first 4 rows of EmpID and Band, then value_counts()
df_sorted = df.sort_values(by=['Band', 'EmpID'], ascending=[False, True])
print(df_sorted[['EmpID', 'Band']].head(4))
print(df['Band'].value_counts().sort_index())

# ==========================================
# Q14. Grouping and pivot table
# ==========================================

# 1. Group by Department, aggregate mean, max, and count of salary, rounded to 1 decimal, sorted by mean descending
agg_df = df.groupby('Department')['Salary'].agg(['mean', 'max', 'count']).round(1)
agg_df = agg_df.sort_values(by='mean', ascending=False)
print(agg_df)

# 2. Add PctOfGroup = Salary as a percentage of its group's total, rounded to 1 decimal
df['PctOfGroup'] = round((df['Salary'] / df.groupby('Department')['Salary'].transform('sum')) * 100, 1)
print(df[['EmpID', 'Department', 'PctOfGroup']].head(4))

# 3. Create a pivot table with Department as rows, City as columns, sum of salary as values, 0 for empty cells
pivot_df = df.pivot_table(index='Department', columns='City', values='Salary', aggfunc='sum', fill_value=0)
print(pivot_df)

# ==========================================
# Q15. Merge, index and JSON
# ==========================================

# Load department heads dataset
heads_df = pd.read_csv('heads.csv', skipinitialspace=True)

# 1. Merge heads_df with df using left join; print number of missing Head values and shape on one line
merged_left = pd.merge(df, heads_df, on='Department', how='left')
print(merged_left['Head'].isna().sum(), merged_left.shape)

# 2. Perform inner and outer merges, print row counts of each on one line
merged_inner = pd.merge(df, heads_df, on='Department', how='inner')
merged_outer = pd.merge(df, heads_df, on='Department', how='outer')
print(len(merged_inner), len(merged_outer))

# 3. Set EmpID as index, print name of employee with EmpID 106 using loc. 
#    Then reset index, rename 'Salary' to 'Monthly Salary', and print first 6 column names.
emp_indexed = df.set_index('EmpID')
print(emp_indexed.loc[106, 'Name'])

emp_reset = emp_indexed.reset_index()
emp_reset = emp_reset.rename(columns={'Salary': 'Monthly Salary'})
print(list(emp_reset.columns)[:6])

# 4. Save EmpID and Name to names.json with orient="records", read it back, and print its shape
df[['EmpID', 'Name']].to_json('names.json', orient='records')
json_df = pd.read_json('names.json')
print(json_df.shape)