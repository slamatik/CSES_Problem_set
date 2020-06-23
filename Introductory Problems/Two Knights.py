n = int(input())
for i in range(1, n+1):
    s = i ** 2 * (i ** 2 - 1) - 8 - 24 - ((i - 4) * 16) - 16 - ((i - 4) * 24) - ((i - 4) ** 2 * 8)
    print(s // 2)
