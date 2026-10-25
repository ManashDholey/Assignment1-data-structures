import pandas as pd
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





