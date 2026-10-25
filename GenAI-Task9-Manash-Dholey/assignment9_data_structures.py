import numpy as np
print("NumPy version:", np.__version__)
print("NumPy is imported successfully.")
print("Start of the Task one: NumPy Array Operations")
np_D1_array = np.array([1, 2, 3, 4, 5,6,7,8,9,10])    
print(np_D1_array)
print(np_D1_array.shape)
print(type(np_D1_array))
print("Data type of np_D1_array:", np_D1_array.dtype)
np_D2_array = np.array([[1, 2, 3],
                        [6,7,8],
                        [9,10,11]])
print(np_D2_array)
print(np_D2_array.shape)
print(type(np_D2_array))
print("Data type of np_D2_array:", np_D2_array.dtype)

# Create a specific 3x3 matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
print(matrix.shape)
print(type(matrix))
print("Data type of matrix:", matrix.dtype)

# Accessing elements of the matrix
print("Element at row 1, column 2:", matrix[0, 1])
print("Element at row 3, column 3:", matrix[2, 2])

# Accessing a whole row
print("Row 2:", matrix[1, :])
print("Row 2 type:", type(matrix[1, :]))

# Accessing a whole column
print("Column 3:", matrix[:, 2])
print("Column 3 type:", type(matrix[:, 2]))

# Slicing a submatrix
print("Submatrix (rows 1-2, columns 2-3):", matrix[0:2, 1:3])
print("Submatrix type:", type(matrix[0:2, 1:3]))
list_to_np_array = [10, 20, 30, 40, 50]
np_array_from_list = np.array(list_to_np_array)
print(np_array_from_list)
print(np_array_from_list.shape)
print(type(np_array_from_list))
print("Data type of np_array_from_list:", np_array_from_list.dtype)

# Converting a tuple to a NumPy array
tuple_to_np_array = (60, 70, 80, 90, 100)
np_array_from_tuple = np.array(tuple_to_np_array)
print(np_array_from_tuple)
print(np_array_from_tuple.shape)
print(type(np_array_from_tuple))
print("Data type of np_array_from_tuple:", np_array_from_tuple.dtype)

# Converting a list of lists to a NumPy array
list_of_lists_to_np_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_array_from_list_of_lists = np.array(list_of_lists_to_np_array)
print(np_array_from_list_of_lists)
print(np_array_from_list_of_lists.shape)
print(type(np_array_from_list_of_lists))
print("Data type of np_array_from_list_of_lists:", np_array_from_list_of_lists.dtype)
# Converting a tuple of tuples to a NumPy array 
tuple_of_tuples_to_np_array = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
np_array_from_tuple_of_tuples = np.array(tuple_of_tuples_to_np_array)
print(np_array_from_tuple_of_tuples)
print(np_array_from_tuple_of_tuples.shape)
print(type(np_array_from_tuple_of_tuples))
print("Data type of np_array_from_tuple_of_tuples:", np_array_from_tuple_of_tuples.dtype)
print("End of the Task one: NumPy Array Operations")
print("Start of the Task two: NumPy Array Arithmetic Operations")

A = np.array([[10,20,30,40]])
B = np.array([[1,2,3,4]])

result_addition = A + B
print(result_addition)
print("Data type of result_addition:", result_addition.dtype)

result_subtraction = A - B
print(result_subtraction)
print("Data type of result_subtraction:", result_subtraction.dtype)
result_multiplication = A * B
print(result_multiplication)
print("Data type of result_multiplication:", result_multiplication.dtype)
result_division = A / B
print(result_division)
print("Data type of result_division:", result_division.dtype)
result_exponentiation = A ** B
print(result_exponentiation)
print("Data type of result_exponentiation:", result_exponentiation.dtype)
result_modulus = A % B
print(result_modulus)
print("Data type of result_modulus:", result_modulus.dtype)
result_floor_division = A // B
print(result_floor_division)
print("Data type of result_floor_division:", result_floor_division.dtype)
result_negation = -A
print(result_negation)
print("Data type of result_negation:", result_negation.dtype)
result_absolute = np.abs(A)
print(result_absolute)
print("Data type of result_absolute:", result_absolute.dtype)
result_square_root = np.sqrt(A)
print(result_square_root)
print("Data type of result_square_root:", result_square_root.dtype)
result_power = np.power(A, 2)
print(result_power)
print("Data type of result_power:", result_power.dtype)
result_exponential = np.exp(A)
print(result_exponential)
print("Data type of result_exponential:", result_exponential.dtype)
result_logarithm = np.log(A)
print(result_logarithm)
print("Data type of result_logarithm:", result_logarithm.dtype)
result_sine = np.sin(A)
print(result_sine)
print("Data type of result_sine:", result_sine.dtype)
result_cosine = np.cos(A)
print(result_cosine)
print("Data type of result_cosine:", result_cosine.dtype)
result_tangent = np.tan(A)
print(result_tangent)
print("Data type of result_tangent:", result_tangent.dtype)
result_arcsine = np.arcsin(A/40)  # Normalizing to keep within [-1, 1] for arcsin
print(result_arcsine)
print("Data type of result_arcsine:", result_arcsine.dtype)
result_arccosine = np.arccos(A/40)  # Normalizing to keep within [-1, 1] for arccos
print(result_arccosine)
print("Data type of result_arccosine:", result_arccosine.dtype)
result_arctangent = np.arctan(A)
print(result_arctangent)
print("Data type of result_arctangent:", result_arctangent.dtype)
result_hyperbolic_sine = np.sinh(A)
print(result_hyperbolic_sine)
print("Data type of result_hyperbolic_sine:", result_hyperbolic_sine.dtype)
result_hyperbolic_cosine = np.cosh(A)
print(result_hyperbolic_cosine)
print("Data type of result_hyperbolic_cosine:", result_hyperbolic_cosine.dtype)
result_hyperbolic_tangent = np.tanh(A)
print(result_hyperbolic_tangent)
print("Data type of result_hyperbolic_tangent:", result_hyperbolic_tangent.dtype)
result_degrees = np.degrees(A)
print(result_degrees)
print("Data type of result_degrees:", result_degrees.dtype)
result_radians = np.radians(A)
print(result_radians)
print("Data type of result_radians:", result_radians.dtype) 
print("End of the Task two: NumPy Array Arithmetic Operations")

print("Start of the Task three: NumPy Array Aggregation Operations")
values = np.array([[2, 4, 6, 8,10]])
## Arithmetic Operations on the values array.  This includes square root, exponentiation, and logarithm.
result_square_root = np.sqrt(values) ## Square root of each element
print(result_square_root)
print("Data type of result_square_root:", result_square_root.dtype)
result_exponentiation = np.power(values, 2) ## Each element raised to the power of 2
print(result_exponentiation)
print("Data type of result_exponentiation:", result_exponentiation.dtype)
result_logarithm = np.log(values) ## Natural logarithm of each element
print(result_logarithm)
print("Data type of result_logarithm:", result_logarithm.dtype)

result_sum = np.sum(values) ## Sum of all elements
print(result_sum)
print("Data type of result_sum:", type(result_sum))
result_cumulative_sum = np.cumsum(values) ## Cumulative sum of elements
print(result_cumulative_sum)
print("Data type of result_cumulative_sum:", result_cumulative_sum.dtype)
result_variance = np.var(values) ## Variance of elements
print(result_variance)
print("Data type of result_variance:", result_variance.dtype)
result_mean = np.mean(values) ## Mean of elements
print(result_mean)
print("Data type of result_mean:", result_mean.dtype)
result_median = np.median(values) ## Median of elements
print(result_median)
print("Data type of result_median:", result_median.dtype)
result_max = np.max(values) ## Maximum element
print(result_max)
print("Data type of result_max:", result_max.dtype)
result_min = np.min(values) ## Minimum element
print(result_min)
print("Data type of result_min:", result_min.dtype)
result_standard_deviation = np.std(values) ## Standard deviation of elements
print(result_standard_deviation)
print("Data type of result_standard_deviation:", result_standard_deviation.dtype)
result_minimum_index = np.argmin(values) ## Index of minimum element
print(result_minimum_index)
print("Data type of result_minimum_index:", type(result_minimum_index))
result_maximum_index = np.argmax(values) ## Index of maximum element
print(result_maximum_index)
print("Data type of result_maximum_index:", type(result_maximum_index))
result_shape = np.shape(values) ## Shape of the array
print(result_shape)
print("Data type of result_shape:", type(result_shape))
result_dimensions = np.ndim(values) ## Number of dimensions of the array
print(result_dimensions)
print("Data type of result_dimensions:", type(result_dimensions))
result_size = np.size(values) ## Total number of elements in the array
print(result_size)
print("Data type of result_size:", type(result_size))
result_transpose = np.transpose(values) ## Transpose of the array
print(result_transpose)
print("Data type of result_transpose:", result_transpose.dtype)
result_flatten = np.ravel(values) ## Flattened array
print(result_flatten)
print("Data type of result_flatten:", result_flatten.dtype)
# result_reshape = np.reshape(values, (5, 2)) ## Reshaped array to 5x2
# print(result_reshape)
result_diagonal = np.diagonal(values) ## Diagonal elements of the array
print(result_diagonal)
print("Data type of result_diagonal:", result_diagonal.dtype)
result_trace = np.trace(values) ## Trace of the array (sum of diagonal elements)
print(result_trace)
print("Data type of result_trace:", result_trace.dtype)
# result_diagonal_sum = np.trace(np.diagonal(values)) ## Sum of diagonal elements
# print(result_diagonal_sum)
result_nonzero_indices = np.nonzero(values) ## Indices of non-zero elements
print(result_nonzero_indices)
print("Data type of result_nonzero_indices:", type(result_nonzero_indices))
result_unique = np.unique(values) ## Unique elements of the array
print(result_unique)
print("Data type of result_unique:", result_unique.dtype)
result_sort = np.sort(values) ## Sorted array
print(result_sort)
print("Data type of result_sort:", result_sort.dtype)

print("End of the Task three: NumPy Array Aggregation Operations")

print("Start of the Task four: NumPy Array Statistical Operations")

data = np.array([[10,20,30],[40,50,60],[70,80,90]]) ## Sample 3x3 array for statistical operations
result_of_row_sum = np.sum(data, axis=1) ## Sum of elements along each row
print("row-wise sum-",result_of_row_sum)
print("Data type of result_of_row_sum:", result_of_row_sum.dtype)
result_of_column_sum = np.sum(data, axis=0) ## Sum of elements along each column
print("column-wise sum-",result_of_column_sum)
print("Data type of result_of_column_sum:", result_of_column_sum.dtype)
result_of_minimum = np.min(data, axis=1) ## Minimum element along each row
print("row-wise minimum-",result_of_minimum)
print("Data type of result_of_minimum:", result_of_minimum.dtype)
result_of_column_minimum = np.min(data, axis=0) ## Minimum element along each column
print("column-wise minimum-",result_of_column_minimum)
print("Data type of result_of_column_minimum:", result_of_column_minimum.dtype)
result_of_maximum = np.max(data, axis=1) ## Maximum element along each row
print("row-wise maximum-",result_of_maximum)
print("Data type of result_of_maximum:", result_of_maximum.dtype)
result_of_column_maximum = np.max(data, axis=0) ## Maximum element along each column
print("column-wise maximum-",result_of_column_maximum)
print("Data type of result_of_column_maximum:", result_of_column_maximum.dtype)
result_of_overall_mean = np.mean(data) ## Overall mean of the array
print("overall mean-",result_of_overall_mean)
print("Data type of result_of_overall_mean:", type(result_of_overall_mean))
print("End of the Task four: NumPy Array Statistical Operations")

print("Start of the Task five: NumPy Array Linear Algebra Operations")
marks = np.array([78,85,90,66,72,88,95,60])
result_of_mean_marks = np.mean(marks) ## Mean of the marks
print("mean of marks-",result_of_mean_marks)
print("Data type of result_of_mean_marks:", type(result_of_mean_marks))
result_of_median_marks = np.median(marks) ## Median of the marks
print("median of marks-",result_of_median_marks)
print("Data type of result_of_median_marks:", type(result_of_median_marks))
result_of_variance_marks = np.var(marks) ## Variance of the marks
print("variance of marks-",result_of_variance_marks)
print("Data type of result_of_variance_marks:", type(result_of_variance_marks))
result_of_standard_deviation_marks = np.std(marks) ## Standard deviation of the marks
print("standard deviation of marks-",result_of_standard_deviation_marks)
print("Data type of result_of_standard_deviation_marks:", type(result_of_standard_deviation_marks))
result_of_minimum_and_maximum_marks = np.min(marks), np.max(marks) ## Minimum and maximum of the marks
print("minimum and maximum of marks-",result_of_minimum_and_maximum_marks)
print("Data type of result_of_minimum_and_maximum_marks:", type(result_of_minimum_and_maximum_marks))
result_of_range_marks = np.ptp(marks) ## Range(max - min) of the marks
print("range of marks-",result_of_range_marks)
print("Data type of result_of_range_marks:", type(result_of_range_marks))
result_of_range_marks_one = np.max(marks) - np.min(marks)
print("range of marks (using max-min)-",result_of_range_marks_one)
print("Data type of result_of_range_marks_one:", type(result_of_range_marks_one))


print("End of the Task five: NumPy Array Linear Algebra Operations")


print("Start of the Task six: NumPy Array Fourier Transform Operations")
result_short_of_marks = np.sort(marks) ## Sorted array of marks
print("sorted marks-",result_short_of_marks)
print("Data type of result_short_of_marks:", result_short_of_marks.dtype)
# 2. Find Percentiles
p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)  # This is also the Median
p75 = np.percentile(marks, 75)

print(f"2. Percentiles:")
print(f"   - 25th percentile: {p25}")
print(f"   - 50th percentile: {p50}")
print(f"   - 75th percentile: {p75}")

# 3. Count students scoring above the average marks
average_marks = np.mean(marks)
# Creates a boolean array (True/False) and counts the True values
students_above_average = np.sum(marks > average_marks) 

print(f"3. Average Mark: {average_marks}")
print("Data type of average_marks:", type(average_marks))
print(f"   - Number of students above average: {students_above_average}")
print("Data type of students_above_average:", type(students_above_average))
print("End of the Task six: NumPy Array Fourier Transform Operations")

print("Start of the Task seven: NumPy Array Random Operations")

# Given daily sales data (assuming index 0 = Day 1, index 1 = Day 2, etc.)
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# 1. Total weekly sales
total_sales = np.sum(sales)

# 2. Average daily sales
avg_sales = np.mean(sales)

# 3. Highest and lowest sales day (using 1-based indexing for cleaner readability)
highest_day = np.argmax(sales) + 1
lowest_day = np.argmin(sales) + 1

# 4. Standard deviation of sales
std_sales = np.std(sales)

# 5. Identify days where sales were above average
# This creates a boolean mask and finds the indices (adding 1 for Day numbers)
above_avg_days = np.where(sales > avg_sales)[0] + 1

# Print Results
print(f"1. Total weekly sales: {total_sales}")
print("Data type of total_sales:", type(total_sales))
print(f"2. Average daily sales: {avg_sales:.2f}")
print("Data type of avg_sales:", type(avg_sales))
print(f"3. Highest sales day: Day {highest_day} ({np.max(sales)})")
print("Data type of highest_day:", type(highest_day))
print(f"   Lowest sales day: Day {lowest_day} ({np.min(sales)})")
print("Data type of lowest_day:", type(lowest_day))
print(f"4. Standard deviation of sales: {std_sales:.2f}")
print("Data type of std_sales:", type(std_sales))
print(f"5. Days with sales above average: Days {above_avg_days.tolist()}")
print("Data type of above_avg_days:", type(above_avg_days))

print("End of the Task seven: NumPy Array Random Operations")