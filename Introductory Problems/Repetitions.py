n = input()

cnt = 1
results = []

for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        cnt += 1
    else:
        results.append(cnt)
        cnt = 1
results.append(cnt)

print(max(results))
