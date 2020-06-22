n = int(input())
sol = f"{n}"
while n != 1:
    if n % 2 == 0:
        n //= 2
        sol += f" {n}"
    else:
        n = n * 3 + 1
        sol += f" {n}"
print(sol)