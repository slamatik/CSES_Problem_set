string = input()
n = len(string)

data = sorted(set(string))

half_res = ""
middle = ""
counter = 0

for i in data:
    count = string.count(i)
    if count % 2 == 0:
        half_res += i * (count // 2)
    elif counter == 1:
        print("NO SOLUTION")
        break
    else:
        counter = 1
        middle += i * count

print(half_res + middle + half_res[::-1])

# Dont know why it doesnt work
# string = "CBPPBFCFAA"
# string = "AAAACACBA"
# n = len(string)


# data = {}
# for i in string:
#     data[i] = data.get(i, 0) + 1
#
# if len(data) == 1:
#     print(string)
#     quit()
#
# result = ""
#
# # print(data)
#
# odd_cnt = 0
#
# for key, val in data.items():
#     if val % 2 != 0:
#         odd_cnt += 1
#         if odd_cnt > 1:
#             print("NO SOLUTION")
#             quit()
#     result += key*ceil(val/2)
# if n % 2 != 0:
#     # print(result + result[-2::-1])
#     print(result + result[::-1][1:])
# else:
#     print(result + result[::-1])
