n, x = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]

data = {}


def sum_two(numbers, num):
    for i in range(n):
        d = numbers[i]
        if num - d in data:
            return f"{i + 1} {data[num - d] + 1}"
        else:
            data[d] = i
    return "IMPOSSIBLE"


print(sum_two(array, x))
