n, q = [int(i) for i in input().split()]
data = [int(i) for i in input().split()]
lines = [[int(i) for i in input().split()] for i in range(q)]

table = [data[0]]
for i in range(1, n):
    table.append(table[-1] + data[i])

for i in lines:
    a, b = i
    if a == 1:
        print(table[b - 1])
    else:
        print(table[b - 1] - table[a - 2])

