n = int(input())
k = [int(i) for i in input().split()]

data = set()


def playlist(array):
    del_id, count = 0, 0
    for i in range(n):
        while array[i] in data:
            data.remove(k[del_id])
            del_id += 1
        data.add(array[i])
        count = max(count, len(data))
    return count


print(playlist(k))
