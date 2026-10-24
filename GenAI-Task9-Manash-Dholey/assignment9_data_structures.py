import numpy as np
print("NumPy version:", np.__version__)
print("NumPy is imported successfully.")
print("Start of the Task one: NumPy Array Operations")
np_D1_array = np.array([1, 2, 3, 4, 5,6,7,8,9,10])    
print(np_D1_array)
print(np_D1_array.shape)
print(type(np_D1_array))
np_D2_array = np.array([[1, 2, 3],
                        [6,7,8],
                        [9,10,11]])
print(np_D2_array)
print(np_D2_array.shape)
print(type(np_D2_array))
# Create a specific 3x3 matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
print(matrix.shape)
print(type(matrix))
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

# Converting a tuple to a NumPy array
tuple_to_np_array = (60, 70, 80, 90, 100)
np_array_from_tuple = np.array(tuple_to_np_array)
print(np_array_from_tuple)
print(np_array_from_tuple.shape)
print(type(np_array_from_tuple))

# Converting a list of lists to a NumPy array
list_of_lists_to_np_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_array_from_list_of_lists = np.array(list_of_lists_to_np_array)
print(np_array_from_list_of_lists)
print(np_array_from_list_of_lists.shape)
print(type(np_array_from_list_of_lists))
# Converting a tuple of tuples to a NumPy array 
tuple_of_tuples_to_np_array = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
np_array_from_tuple_of_tuples = np.array(tuple_of_tuples_to_np_array)
print(np_array_from_tuple_of_tuples)
print(np_array_from_tuple_of_tuples.shape)
print(type(np_array_from_tuple_of_tuples))
print("End of the Task one: NumPy Array Operations")
print("Start of the Task two: NumPy Array Arithmetic Operations")

A = np.array([[10,20,30,40]])
B = np.array([[1,2,3,4]])

result_addition = A + B
print(result_addition)
result_subtraction = A - B
print(result_subtraction)
result_multiplication = A * B
print(result_multiplication)
result_division = A / B
print(result_division)
result_exponentiation = A ** B
print(result_exponentiation)
result_modulus = A % B
print(result_modulus)
result_floor_division = A // B
print(result_floor_division)
result_negation = -A
print(result_negation)
result_absolute = np.abs(A)
print(result_absolute)
result_square_root = np.sqrt(A)
print(result_square_root)
result_power = np.power(A, 2)
print(result_power)
result_logarithm = np.log(A)
print(result_logarithm)
result_sine = np.sin(A)
print(result_sine)
result_cosine = np.cos(A)
print(result_cosine)
result_tangent = np.tan(A)
print(result_tangent)
result_arcsine = np.arcsin(A/40)  # Normalizing to keep within [-1, 1] for arcsin
print(result_arcsine)
result_arccosine = np.arccos(A/40)  # Normalizing to keep within [-1, 1] for arccos
print(result_arccosine)
result_arctangent = np.arctan(A)
print(result_arctangent)
result_hyperbolic_sine = np.sinh(A)
print(result_hyperbolic_sine)
result_hyperbolic_cosine = np.cosh(A)
print(result_hyperbolic_cosine)
result_hyperbolic_tangent = np.tanh(A)
print(result_hyperbolic_tangent)
result_degrees = np.degrees(A)
print(result_degrees)
result_radians = np.radians(A)
print(result_radians)
print("End of the Task two: NumPy Array Arithmetic Operations")

print("Start of the Task three: NumPy Array Aggregation Operations")
values = np.array([[2, 4, 6, 8,10]])
## Arithmetic Operations on the values array.  This includes square root, exponentiation, and logarithm.
result_square_root = np.sqrt(values) ## Square root of each element
print(result_square_root)
result_exponentiation = np.power(values, 2) ## Each element raised to the power of 2
print(result_exponentiation)
result_logarithm = np.log(values) ## Natural logarithm of each element
print(result_logarithm)

result_sum = np.sum(values) ## Sum of all elements
print(result_sum)
result_cumulative_sum = np.cumsum(values) ## Cumulative sum of elements
print(result_cumulative_sum)
result_variance = np.var(values) ## Variance of elements
print(result_variance)
result_mean = np.mean(values) ## Mean of elements
print(result_mean)
result_median = np.median(values) ## Median of elements
print(result_median)
result_max = np.max(values) ## Maximum element
print(result_max)
result_min = np.min(values) ## Minimum element
print(result_min)
result_standard_deviation = np.std(values) ## Standard deviation of elements
print(result_standard_deviation)
result_minimum_index = np.argmin(values) ## Index of minimum element
print(result_minimum_index)
result_maximum_index = np.argmax(values) ## Index of maximum element
print(result_maximum_index)
result_shape = np.shape(values) ## Shape of the array
print(result_shape)
result_dimensions = np.ndim(values) ## Number of dimensions of the array
print(result_dimensions)
result_size = np.size(values) ## Total number of elements in the array
print(result_size)
result_transpose = np.transpose(values) ## Transpose of the array
print(result_transpose)
result_flatten = np.ravel(values) ## Flattened array
print(result_flatten)
# result_reshape = np.reshape(values, (5, 2)) ## Reshaped array to 5x2
# print(result_reshape)
result_diagonal = np.diagonal(values) ## Diagonal elements of the array
print(result_diagonal)
result_trace = np.trace(values) ## Trace of the array (sum of diagonal elements)
print(result_trace)
# result_diagonal_sum = np.trace(np.diagonal(values)) ## Sum of diagonal elements
# print(result_diagonal_sum)
result_nonzero_indices = np.nonzero(values) ## Indices of non-zero elements
print(result_nonzero_indices)
result_unique = np.unique(values) ## Unique elements of the array
print(result_unique)
result_sort = np.sort(values) ## Sorted array
print(result_sort)

print("End of the Task three: NumPy Array Aggregation Operations")

print("Start of the Task four: NumPy Array Statistical Operations")

data = np.array([[10,20,30],[40,50,60],[70,80,90]]) ## Sample 3x3 array for statistical operations
result_of_row_sum = np.sum(data, axis=1) ## Sum of elements along each row
print("row-wise sum-",result_of_row_sum)
result_of_column_sum = np.sum(data, axis=0) ## Sum of elements along each column
print("column-wise sum-",result_of_column_sum)
result_of_minimum = np.min(data, axis=1) ## Minimum element along each row
print("row-wise minimum-",result_of_minimum)
result_of_column_minimum = np.min(data, axis=0) ## Minimum element along each column
print("column-wise minimum-",result_of_column_minimum)
result_of_maximum = np.max(data, axis=1) ## Maximum element along each row
print("row-wise maximum-",result_of_maximum)
result_of_column_maximum = np.max(data, axis=0) ## Maximum element along each column
print("column-wise maximum-",result_of_column_maximum)
result_of_overall_mean = np.mean(data) ## Overall mean of the array
print("overall mean-",result_of_overall_mean)
print("End of the Task four: NumPy Array Statistical Operations")

print("Start of the Task five: NumPy Array Linear Algebra Operations")
marks = np.array([78,85,90,66,72,88,95,60])
result_of_mean_marks = np.mean(marks) ## Mean of the marks
print("mean of marks-",result_of_mean_marks)
result_of_median_marks = np.median(marks) ## Median of the marks
print("median of marks-",result_of_median_marks)
result_of_variance_marks = np.var(marks) ## Variance of the marks
print("variance of marks-",result_of_variance_marks)
result_of_standard_deviation_marks = np.std(marks) ## Standard deviation of the marks
print("standard deviation of marks-",result_of_standard_deviation_marks)
result_of_minimum_and_maximum_marks = np.min(marks), np.max(marks) ## Minimum and maximum of the marks
print("minimum and maximum of marks-",result_of_minimum_and_maximum_marks)
result_of_range_marks = np.ptp(marks) ## Range(max - min) of the marks
print("range of marks-",result_of_range_marks)
result_of_range_marks_one = np.max(marks) - np.min(marks)
print("range of marks (using max-min)-",result_of_range_marks_one)


print("End of the Task five: NumPy Array Linear Algebra Operations")


print("Start of the Task six: NumPy Array Fourier Transform Operations")
result_short_of_marks = np.sort(marks) ## Sorted array of marks
print("sorted marks-",result_short_of_marks)
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
print(f"   - Number of students above average: {students_above_average}")
print("End of the Task six: NumPy Array Fourier Transform Operations")

print("Start of the Task seven: NumPy Array Random Operations")

print("End of the Task seven: NumPy Array Random Operations")