from itertools import permutations

n = input()

permuted = list(set(permutations(n)))
permuted_list = [''.join(i) for i in permuted]


print(len(permuted_list))

for i in sorted(permuted_list):
    print(i)