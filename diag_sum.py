arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]

length = len(arr)

# 1st daigonal sum
j = i = 0
sum_1st = 0
for i in range(length):
    sum_1st += arr[i][j]
    j += 1
first_diag = sum_1st

# 2nd diagonal sum
sum_2nd = k = 0
l = length-1

for l in reversed(range(length)):
    sum_2nd += arr[k][l]
    k += 1
second_diag = sum_2nd

# Absolute Sum
Absolute_sum = abs(second_diag-first_diag)
print(Absolute_sum) 