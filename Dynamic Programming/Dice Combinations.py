n = int(input())

mod = 10 ** 9 + 7


def dice(n):
    start = [1, 1, 2, 4, 8, 16]
    a, b, c, d, e, f = start
    if n <= 5:
        return start[n]
    else:
        for i in range(6, n + 1):
            g = (a + b + c + d + e + f) % mod
            a, b, c, d, e, f = b, c, d, e, f, g
    return g


# -=-=-=-=-Bottom-up-=-=-=-=-
# def dice(n):
#     table = [0 for i in range(n + 1)]
#     table[0] = 1
#     for i in range(1, n + 1):
#         for j in range(1,7):
#             if j <= i:
#                 table[i] += (table[i-j])
#             table[i] %= mod
#     return table[-1]

# -=-=-=-=-Recursion-=-=-=-=-
# memo = {0: 1}
# def dice(n):
#     if n in memo:
#         return memo[n]
#     else:
#         temp = 0
#         for i in range(1, 7):
#             if i <= n:
#                 temp += dice(n - i) % mod
#                 memo[n] = temp % mod
#         return memo[n]


print(dice(n))
