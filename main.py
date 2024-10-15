def get_matrix(n, m, value):
 matrix = []
 for i in range(n):
 row = []
 for j in range(m):
 row.append(value)
 matrix.append(row)
 return matrix


result1 = get_matrix(n = 2, m = 5, value = 5)
result2 = get_matrix(n = 5, m = 8, value = 19)
result3 = get_matrix(n = 25, m = 4, value = 44)

print(result1)
print(result2)
print(result3)
