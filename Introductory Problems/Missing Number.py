n = int(input())
numbers_list = [int(i) for i in input().split()]

sum_full = sum(range(1, n+1))
sum_nums = sum(numbers_list)

print(sum_full-sum_nums)
