import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV file read
df = pd.read_csv("student.csv")

# First 5 rows
print("\n First 5 Rows:")
print(df.head())

# Column info and data types
print("\n Dataset Info:")
print(df.info())

# Summary statistics
print("\n Summary Statistics:")
print(df.describe())

# Missing values check
print("\n Missing Values:")
print(df.isnull().sum())

# Grade-wise count
print("\nGrade Categories:")
print(df["Grade"].value_counts())

# Comment-wise count
print("\nComment Categories:")
print(df["Comment"].value_counts())

# School-wise average marks 
print("\n School-wise Average Marks:")
print(df.groupby("School Name")[["Math", "Physics", "Chemistry"]].mean())

# Boxplot - Math
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Math"])
plt.title("Math Marks Boxplot")
plt.show()

# Grade Comment bar chart
plt.figure(figsize=(6, 4))
sns.countplot(x=df["Grade"])
plt.title("Grade Count")
plt.xlabel("Grade")
plt.ylabel("No. of Students")
plt.show()
