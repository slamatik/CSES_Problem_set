n, x = [int(i) for i in input().split()]
weights = sorted(int(i) for i in input().split())

count, left, right = 0, 0, len(weights) - 1

while left <= right:
    if weights[left] + weights[right] > x:
        right -= 1
    else:
        left += 1
        right -= 1
    count += 1

print(count)
