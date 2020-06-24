n = int(input())
coins = [[int(i) for i in input().split()] for s in range(n)]

for i in coins:
    a, b = i[0], i[1]
    if (2 * a - b) >= 0 and (2 * a - b) % 3 == 0 and (2 * b - a) >= 0 and (2 * b - a) % 3 == 0:
        print("YES")
    else:
        print("NO")
