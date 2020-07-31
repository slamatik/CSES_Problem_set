n = int(input())
c = 0
while n:
    n -= max([int(i) for i in str(n)])
    c += 1
print(c)