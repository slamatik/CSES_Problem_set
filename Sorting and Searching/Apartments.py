n, m, k = [int(i) for i in input().split()]
a = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])

app_n, size_n, count = 0, 0, 0

while app_n < n and size_n < m:
    if a[app_n] + k < b[size_n]:
        app_n += 1
    elif a[app_n] - k > b[size_n]:
        size_n += 1
    else:
        app_n += 1
        size_n += 1
        count += 1
print(count)
