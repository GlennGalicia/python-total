# 📘 Day 14

## Numpy, Pandas

## Table of Contents

1. [What are NumPy and Pandas](#what-are-numpy-and-pandas)
2. [Installation](#installation)
3. [NumPy Basics](#numpy-basics)
4. [Pandas Basics](#pandas-basics)
5. [Common Operations Cheat Sheet](#common-operations-cheat-sheet)
6. [Additional Resources](#additional-resources)

---

## What are NumPy and Pandas?

**NumPy** (Numerical Python) is a library for working with arrays and numerical computations. It's fast and efficient for mathematical operations.

**Pandas** is built on top of NumPy and provides data structures (DataFrames and Series) for working with tabular data, similar to Excel spreadsheets.

**Use cases:**

- Data analysis and manipulation
- Scientific computing
- Financial analysis
- Machine learning preprocessing
- Statistical analysis
- CSV/Excel file processing

---

## Installation

### With UV (recommended)

```bash
# Create project
uv init data-analysis
cd data-analysis

# Add NumPy and Pandas
uv add numpy pandas

# Optional: Add visualization libraries
uv add matplotlib seaborn

# Optional: Add Excel support
uv add openpyxl xlrd
```

### Project Structure

```
data-analysis/
├── .venv/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── analysis.py
│   └── visualize.py
├── data/
│   ├── input.csv
│   └── output.csv
└── README.md
```

---

# NumPy Basics

## 1. Creating Arrays

```python
import numpy as np

# From list
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
# [[1 2 3]
#  [4 5 6]]

# Array of zeros
zeros = np.zeros(5)
print(zeros)  # [0. 0. 0. 0. 0.]

# Array of ones
ones = np.ones((3, 3))
print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# Range of numbers
range_arr = np.arange(0, 10, 2)  # Start, stop, step
print(range_arr)  # [0 2 4 6 8]

# Evenly spaced numbers
linspace = np.linspace(0, 1, 5)  # Start, stop, count
print(linspace)  # [0.   0.25 0.5  0.75 1.  ]
```

## 2. Array Properties

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # (2, 3) - 2 rows, 3 columns
print(arr.size)  # 6 - total elements
print(arr.ndim)  # 2 - number of dimensions
print(arr.dtype)  # int64 - data type
```

## 3. Array Operations

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Basic math
print(arr + 10)  # [11 12 13 14 15]
print(arr * 2)  # [ 2  4  6  8 10]
print(arr ** 2)  # [ 1  4  9 16 25]

# Array with array
arr2 = np.array([5, 4, 3, 2, 1])
print(arr + arr2)  # [6 6 6 6 6]
print(arr * arr2)  # [5 8 9 8 5]

# Math functions
print(np.sqrt(arr))  # Square root
print(np.mean(arr))  # Average: 3.0
print(np.sum(arr))  # Sum: 15
print(np.max(arr))  # Maximum: 5
print(np.min(arr))  # Minimum: 1
print(np.std(arr))  # Standard deviation
```

## 4. Array Indexing and Slicing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr[0])  # 10 - first element
print(arr[-1])  # 50 - last element

# Slicing
print(arr[1:4])  # [20 30 40]
print(arr[:3])  # [10 20 30]
print(arr[2:])  # [30 40 50]

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # 1 - first row, first column
print(arr2d[1, 2])  # 6 - second row, third column
print(arr2d[0, :])  # [1 2 3] - entire first row
print(arr2d[:, 0])  # [1 4 7] - entire first column
```

# Pandas Basics

## 1. Series (1D Data)

```python
import pandas as pd

# Create Series from list
s = pd.Series([10, 20, 30, 40, 50])
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50

# Series with custom index
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s2)
# a    10
# b    20
# c    30

# Access elements
print(s2['a'])  # 10
print(s2.iloc[0])  # 10 (by position)
```

## 2. DataFrame (2D Data)

```python
import pandas as pd

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30     Paris
# 2  Charlie   35    London
# 3    David   28     Tokyo
```

## 3. Reading Data from Files

```python
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Read Excel
df = pd.read_excel('data.xlsx')

# Read with specific parameters
df = pd.read_csv('data.csv',
                 sep=',',  # Separator
                 header=0,  # First row as header
                 encoding='utf-8')  # Encoding
```

## 4. Basic DataFrame Operations

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

# View first rows
print(df.head())  # First 5 rows
print(df.head(2))  # First 2 rows

# View last rows
print(df.tail())  # Last 5 rows

# Basic info
print(df.info())  # Data types and non-null counts
print(df.describe())  # Statistical summary
print(df.shape)  # (4, 3) - rows, columns
print(df.columns)  # Column names
```

## 5. Selecting Data

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

# Select single column
print(df['Name'])
# 0      Alice
# 1        Bob
# 2    Charlie

# Select multiple columns
print(df[['Name', 'Age']])
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35

# Select rows by position
print(df.iloc[0])  # First row
print(df.iloc[0:2])  # First 2 rows

# Select rows by condition
print(df[df['Age'] > 25])
#       Name  Age    City
# 1      Bob   30   Paris
# 2  Charlie   35  London

# Select specific cell
print(df.loc[0, 'Name'])  # 'Alice'
```

## 6. Adding and Removing Columns

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Add new column
df['City'] = ['New York', 'Paris', 'London']
print(df)

# Add calculated column
df['Age_in_10_years'] = df['Age'] + 10
print(df)

# Remove column
df = df.drop('Age_in_10_years', axis=1)
# Or
df = df.drop(columns=['Age_in_10_years'])
```

## 7. Filtering Data

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Paris']
}

df = pd.DataFrame(data)

# Filter by single condition
young_people = df[df['Age'] < 30]
print(young_people)

# Filter by multiple conditions
paris_young = df[(df['City'] == 'Paris') & (df['Age'] < 35)]
print(paris_young)

# Filter with OR
condition = df[(df['Age'] > 30) | (df['City'] == 'Tokyo')]
print(condition)

# Filter by values in list
cities = ['Paris', 'Tokyo']
filtered = df[df['City'].isin(cities)]
print(filtered)
```

## 8. Sorting Data

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000]
}

df = pd.DataFrame(data)

# Sort by Age (ascending)
sorted_df = df.sort_values('Age')
print(sorted_df)

# Sort by Age (descending)
sorted_df = df.sort_values('Age', ascending=False)
print(sorted_df)

# Sort by multiple columns
sorted_df = df.sort_values(['Age', 'Salary'])
print(sorted_df)
```

## 9. Grouping and Aggregation

```python
import pandas as pd

data = {
    'City': ['New York', 'Paris', 'New York', 'Paris', 'London'],
    'Sales': [100, 200, 150, 250, 300],
    'Quantity': [5, 10, 7, 12, 15]
}

df = pd.DataFrame(data)

# Group by City and sum
grouped = df.groupby('City')['Sales'].sum()
print(grouped)
# City
# London      300
# New York    250
# Paris       450

# Multiple aggregations
grouped = df.groupby('City').agg({
    'Sales': 'sum',
    'Quantity': 'mean'
})
print(grouped)
```

## 10. Saving Data

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('output.csv', index=False)

# Save to Excel
df.to_excel('output.xlsx', index=False)

# Save to JSON
df.to_json('output.json')
```

## Common Operations Cheat Sheet

```python
import pandas as pd
import numpy as np

# Reading
df = pd.read_csv('file.csv')

# Viewing
df.head()  # First 5 rows
df.tail()  # Last 5 rows
df.info()  # Data types
df.describe()  # Statistics
df.shape  # Dimensions

# Selecting
df['column']  # Single column
df[['col1', 'col2']]  # Multiple columns
df.iloc[0]  # Row by position
df.loc[0, 'col']  # Cell by label

# Filtering
df[df['age'] > 25]  # Condition
df[df['city'].isin(['NY', 'LA'])]  # Multiple values

# Sorting
df.sort_values('age')  # Ascending
df.sort_values('age', ascending=False)  # Descending

# Grouping
df.groupby('city')['sales'].sum()

# Missing data
df.isnull()  # Check for NaN
df.dropna()  # Remove NaN
df.fillna(0)  # Fill NaN

# Adding columns
df['new'] = df['a'] + df['b']

# Saving
df.to_csv('file.csv', index=False)
df.to_excel('file.xlsx', index=False)
```

## Additional Resources

### Official Documentation

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Learning Resources

- [NumPy Tutorial](https://numpy.org/devdocs/user/quickstart.html)
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### Related Libraries

- `matplotlib` - Data visualization
- `seaborn` - Statistical visualization
- `scipy` - Scientific computing
- `scikit-learn` - Machine learning

[<< Day 13](../day_13/day_13.md) | [Day 15 >>](../mysite/day_15.md)