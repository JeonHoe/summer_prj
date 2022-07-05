# 연습문제
from re import L


a = [[[0 for i in range(3)] for j in range(4)] for k in range(2)]
print(a)

print() # 줄 바꿈을 위한 코드

# 심사문제
row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
arr = [[0 for i in range(row+2)] for j in range(col+2)]
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            arr[i][j] += 1
            arr[i][j+1] += 1
            arr[i][j+2] += 1
            arr[i+1][j] += 1
            arr[i+1][j+2] += 1
            arr[i+2][j] += 1
            arr[i+2][j+1] += 1
            arr[i+2][j+2] += 1
        else:
            continue
for i in range(row):
    for j in range(col):
        if matrix[i][j] != '*':
            matrix[i][j] = str(arr[i+1][j+1])
        else:
            continue
print('\n')
for i in range(row):
    s = ''
    for j in range(col):
        s += matrix[i][j]
    print(s)
