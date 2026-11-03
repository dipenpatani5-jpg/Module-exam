
import numpy as np


# Q1. Create Array Using arange()
a = np.arange(10, 51, 5)

print(a)


# Q2. Create Zeros and Ones Arrays
zeros_array = np.zeros((3, 4))

ones_array = np.ones((2, 5), dtype=float)

print(zeros_array.shape, ones_array.shape, np.sum(ones_array))


# Q3. Create Identity Matrix and Multiply by 4
identity = np.eye(3)

print(identity * 4)


# Q4. Create Array Using linspace()
lin = np.linspace(0, 10, 50)

print(len(lin), round(float(lin[1]), 4), float(lin[-1]))


# Q5. Generate Random 4x4 Array
np.random.seed(7)

r = np.random.randint(1, 21, size=(4, 4))

print(r)


# Replace First Row with 100
r[0, :] = 100

print(r[0, :])


# Print Bottom-Right 2x2 Block
print(r[-2:, -2:])



# Q8. Boolean Masks, np.where() and Views

# 1. Boolean Masking
ages = np.array([25, 30, 18, 35, 22, 40, 17])

# Ages 18 or more
print(ages[ages >= 18])

# Ages strictly between 20 and 35
print(ages[(ages > 20) & (ages < 35)])

# Ages below 18 using NOT (~)
print(ages[~(ages >= 18)])


# 2. Using np.where()
scores = np.array([65, 80, 72, 90, 55, 78])

result = np.where(scores >= 75, "Pass", "Fail")

print(result)


# 3. Replace Temperatures Greater Than 30
temps = np.array([28, 32, 25, 35, 30, 22, 38])

mask = temps > 30

temps[mask] = 31

print(temps, int(mask.sum()))


# 4. Array Slicing
mat = np.arange(1, 26).reshape(5, 5)

print(mat[1:4, 2:5])


# 5. View vs Copy

# View shares the original array's data
view = mat[0]

view[0] = 99

print(mat[0, 0])


# Copy creates independent data
copy = mat[1].copy()

copy[0] = -1

print(mat[1, 0])

# View changes the original array, but copy does not.


# Q9. Array Maths and Statistics

# 1. Array Arithmetic Operations
A = np.arange(1, 10).reshape(3, 3)
B = np.arange(11, 20).reshape(3, 3)

# Element-wise multiplication
print(A * B)

# Element-wise division rounded to 2 decimals
print(np.round(A / B, 2))

# Matrix multiplication
print(A @ B)


# 2. Calculate Z-Score
arr = np.array([10, 20, 30, 40, 50], dtype=float)

mean = np.mean(arr)
std = np.std(arr)

z_score = (arr - mean) / std

print(np.round(z_score, 2), round(float(np.mean(z_score)), 6))


# 3. Euclidean Distance
p = np.array([0, 0, 0])
q = np.array([3, 4, 12])

distance = np.sqrt(np.sum((p - q) ** 2))

print(float(distance))


# 4. Array Statistics
v = np.array([4, 9, 2, 15, 7, 1])

print(
    np.argmax(v),
    np.argmin(v),
    np.max(v),
    np.min(v)
)

print(
    np.mean(v),
    np.median(v),
    round(float(np.var(v)), 2),
    round(float(np.std(v)), 2)
)


# 5. Sorting Arrays
m = np.array([
    [9, 3, 1],
    [6, 8, 2],
    [5, 7, 4]
])

# Sort column-wise
print(np.sort(m, axis=0))

# Sort row-wise
print(np.sort(m, axis=1))


# 6. Count Positive, Negative and Zero Values
n = np.array([-3, 0, 5, -1, 0, 8, 2, -7, 0])

positive = np.sum(n > 0)
negative = np.sum(n < 0)
zero = np.sum(n == 0)

print(positive, negative, zero)



# Q10. Reshape, Broadcasting and Splitting

# 1. Reshape and Flatten
vals = np.arange(1, 16)

print(vals.shape)

reshaped = vals.reshape(5, -1)
print(reshaped.reshape(3, 5).flatten().tolist() == vals.tolist())


# 2. Broadcasting
sales = np.array([[10, 20], [15, 25], [12, 18]])
bonus = np.array([2, 3, 1])[:, np.newaxis]

print(sales + bonus)

rates = np.array([0.1, 0.05])
print(np.round(sales * rates, 2))


# 3. Splitting Arrays
arr = np.arange(1, 11)

try:
    np.split(arr, 3)
except ValueError:
    print("ValueError")

parts = np.array_split(arr, 3)
print([part.tolist() for part in parts])
