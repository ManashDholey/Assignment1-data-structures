import pandas as pd
import matplotlib.pyplot as plt
print("Start of the Task 1: Pandas Series Operations")
marks = [78, 85, 90, 66, 72]
marks_series = pd.Series(marks)
print(marks_series)
print("Data type of marks_series:", marks_series.dtype)
print("Index of marks_series:", marks_series.index)
# Accessing elements of the Series
print("Element at index 2:", marks_series[2])
print("Element at index 4:", marks_series[4])
print("Accessing fast elements", marks_series.head(1))
print("Accessing last two elements", marks_series.tail(2))

# Slicing the Series
print("Elements from index 1 to 3:", marks_series[1:4])
print("Elements from index 1 to 3 type:", type(marks_series[1:4]))

# Accessing multiple elements using a list of indices
print("Elements at indices 0, 2, 4:", marks_series[[0, 2, 4]])
print("Elements at indices 0, 2, 4 type:", type(marks_series[[0, 2, 4]]))

# Accessing elements using a boolean condition
print("Elements greater than 70:", marks_series[marks_series > 70])
print("Elements greater than 70 type:", type(marks_series[marks_series > 70]))
# Accessing elements using the index attribute
print("Element at index 2 using index attribute:", marks_series.loc[2])
print("Element at index 4 using index attribute:", marks_series.loc[4])
print("Element at index 2 using index attribute type:", type(marks_series.loc[2]))
print("Element at index 4 using index attribute type:", type(marks_series.loc[4]))

# Accessing elements using the iloc attribute
print("Element at index 2 using iloc attribute:", marks_series.iloc[2])
print("Element at index 4 using iloc attribute:", marks_series.iloc[4])
print("Element at index 2 using iloc attribute type:", type(marks_series.iloc[2]))
print("Element at index 4 using iloc attribute type:", type(marks_series.iloc[4]))

# Accessing elements using a boolean condition with iloc
print("Elements greater than 70 using iloc:", marks_series.iloc[(marks_series > 70).values])
print("Elements greater than 70 using iloc type:", type(marks_series.iloc[(marks_series > 70).values]))
print("End of the Task 1: Pandas Series Operations")
print("Start of the Task 2: Mathematical Operations on Series")
marks_series = marks_series.add(5)
print("After adding 5:", marks_series)

marks_series = marks_series.sub(2)
print("After subtracting 2:", marks_series)

marks_series = marks_series.mul(1.05)
print("After multiplying by 1.05:", marks_series)

marks_series = marks_series.div(2)
print("After dividing by 2:", marks_series)

print("End of the Task 2: Mathematical Operations on Series")
print("Start of the Task 3: python functionalities on Series")
marks = [78, 85, 90, 66, 72]
marks_series = pd.Series(marks)
find_miximum_marks = marks_series.max()
print("Maximum marks:", find_miximum_marks)

find_minimum_marks = marks_series.min()
print("Minimum marks:", find_minimum_marks)

find_sum_marks = marks_series.sum()
print("Sum of marks:", find_sum_marks)

find_mean_marks = marks_series.mean()
print("Mean of marks:", find_mean_marks)

find_median_marks = marks_series.median()
print("Median of marks:", find_median_marks)

find_standard_deviation_marks = marks_series.std()
print("Standard deviation of marks:", find_standard_deviation_marks)

find_variance_marks = marks_series.var()
print("Variance of marks:", find_variance_marks)

find_count_marks = marks_series.count()
print("Count of marks:", find_count_marks)

find_unique_marks = marks_series.nunique()
print("Unique marks:", find_unique_marks)

find_value_counts_marks = marks_series.value_counts()
print("Value counts of marks:", find_value_counts_marks)
check_if_all_above_70 = lambda x: (x > 70)
for mark in marks_series:
    student_above_70 = check_if_all_above_70(mark)
    print("Is mark above 70:", student_above_70)
print("Student above 70:", len(marks_series[marks_series > 70]))

print("End of the Task 3: python functionalities on Series")
print("Start of the Task 4 & 5 & 6")
student ={
    "Name": ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    "Marks": [78, 85, 90, 66, 72],
    "Subject": ["Math", "Math","Science","Science", "Math"]
}
student_df = pd.DataFrame(student)
print("Print first 3 rows of the student DataFrame:")
print(student_df.head(3))

print ("Print last 2 rows of the student DataFrame:")
print(student_df.tail(2))
    
print("Print shape of the student DataFrame:", student_df.shape)
print("Print columns of the student DataFrame:", student_df.columns)
print("Print index of the student DataFrame:", student_df.index)
print("Print info of the student DataFrame:", student_df.info())
print("Print description of the student DataFrame:", student_df.describe())
print("Print first row of the student DataFrame:", student_df.iloc[0])
print("Print last row of the student DataFrame:", student_df.iloc[-1])
print("Print specific column 'Name' of the student DataFrame:", student_df["Name"])
print("Print specific column 'Marks' of the student DataFrame:", student_df["Marks"])
print("Print specific column 'Subject' of the student DataFrame:", student_df["Subject"])
print("Print rows where Marks are greater than 80:", student_df[student_df["Marks"] > 80])
print("Print rows where Marks are greater than 75:", student_df[student_df["Marks"] > 75])
print("Print rows where Subject is 'Math':", student_df[student_df["Subject"] == "Math"])
average_marks = student_df['Marks'].mean()
print("Average marks:", average_marks)
print("Print rows where Marks are greater than average marks:", student_df[student_df["Marks"] > average_marks])
print("Print rows where Marks are less than 70:", student_df[student_df["Marks"] < 70])
print("Print rows where Subject is 'Science':", student_df[student_df["Subject"] == "Science"])
print("Print student DataFrame sorted by Marks in descending order:")
df_sorted = student_df.sort_values(by='Marks', ascending=False)
print(df_sorted)
print("Reset index of the sorted student DataFrame:")
df_sorted_reset = df_sorted.reset_index(drop=True)
print(df_sorted_reset)

print("End of the Task 4 & 5 & 6")
print("Start of the Task 7")
print("Average marks by subject:")
print(student_df.groupby("Subject")["Marks"].mean())
print("Maximum marks by subject:")
print(student_df.groupby("Subject")["Marks"].max())
print("Minimum marks by subject:")
print(student_df.groupby("Subject")["Marks"].min())
print("Count of students by subject:")
print(student_df.groupby("Subject")["Marks"].count())
print("Sum of marks by subject:")
print(student_df.groupby("Subject")["Marks"].sum())
print("End of the Task 7")



print("End of the Task 8")

student_df.plot(kind='bar', x='Name', y='Marks')
plt.show()
line_marks = student_df["Marks"]
line_marks_series = pd.Series(line_marks)
line_marks_series.plot(kind='line')
plt.show()
histogram_marks = student_df["Marks"]
histogram_marks_series = pd.Series(histogram_marks)
histogram_marks_series.plot(kind='hist', bins=4, edgecolor="black")
plt.show()

print("Start of the Task 8")

print("Start of the Task 9")
sales = {
'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
'Revenue': [1200, 1500, 900, 2000, 1800]
}
sales_df = pd.DataFrame(sales)
print("Sales DataFrame:")
print(sales_df)
total_revenue = sales_df["Revenue"].sum()
print("Total revenue:", total_revenue)
average_daily_revenue = sales_df["Revenue"].mean()
print("Average daily revenue:", average_daily_revenue)
day_with_height_revenue = sales_df.loc[sales_df["Revenue"].idxmax(), "Day"]
print("Day with highest revenue:", day_with_height_revenue)
day_with_lowest_revenue = sales_df.loc[sales_df["Revenue"].idxmin(), "Day"]
print("Day with lowest revenue:", day_with_lowest_revenue)
# 1. Calculate the overall average revenue
avg_revenue = sales_df["Revenue"].mean()
print(f"Average Revenue: {avg_revenue}\n")

# 2. Filter for rows where Revenue is greater than the average
above_average_days = sales_df[sales_df["Revenue"] > avg_revenue]

print("Days with above-average revenue:")
print(above_average_days)
sales_df.plot(kind='bar', x='Day', y='Revenue')
plt.show()
print("End of the Task 9")




