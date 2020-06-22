t = int(input())
y_x = [[int(i) for i in input().split()] for s in range(t)]

for i in range(t):
    y, x = y_x[i][0], y_x[i][1]

    if x > y:
        if x % 2 == 1:
            print(x * x - y + 1)
        else:
            x -= 1
            print(x * x + y)
    else:
        if y % 2 == 0:
            print(y * y - x + 1)
        else:
            y -= 1
            print(y * y + x)
