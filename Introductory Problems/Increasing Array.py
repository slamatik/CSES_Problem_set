n = int(input())
nums = [int(i) for i in input().split()]

cnt = 0

for i in range(1, n):
    if nums[i] < nums[i-1]:
        cnt += (nums[i-1]-nums[i])
        nums[i] = nums[i-1]

print(cnt)