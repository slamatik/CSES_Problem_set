from sys import maxsize as inf

dp = {0: 0}


# def remove_digits(n):
#     for i in range(1, n+1):
#         temp = i
#         min_steps = inf
#         while temp != 0:
#             di = temp % 10
#             temp //= 10
#             if di == 0: continue
#             min_steps = min(min_steps, 1 + dp[i - di])
#         dp[i] = min_steps
#     print(dp)
#
# remove_digits(123)
n = int(input())
count = 0
while n > 9:
    num = max([int(i) for i in str(n)])
    n -= num
    count += 1
print(count + 1)
