n = int(input())
nums = [int(i) for i in input().split()]
nums.sort()

cnt = 0
temp = 0

for i in nums:
    if temp == i:
        None
    else:
        cnt += 1
        temp = i
print(cnt)