n = int(input())
x = [int(i) for i in input().split()]


def max_sum(data, m):
    cache = [data[0]]

    for i in range(1, m):
        cache.append(max(data[i], cache[-1] + data[i]))
    return max(cache)


print(max_sum(x, n))
