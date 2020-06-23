n = int(input())
nums = list(range(1, n + 1))

if n == 1:
    print("1")

if n == 2 or n == 3:
    print("NO SOLUTION")

odd = [str(i) for i in range(1, n + 1) if i % 2 != 0]
even = [str(i) for i in range(1, n + 1) if i % 2 == 0]

print(" ".join((even + odd)))
