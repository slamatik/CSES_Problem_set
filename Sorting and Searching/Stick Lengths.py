n = int(input())
nums = sorted(int(i) for i in input().split())

if n % 2 == 0:
    print(sum(nums[n // 2:]) - sum(nums[:n // 2]))
else:
    print(sum(nums[n // 2:]) - sum(nums[:n // 2 + 1]))
