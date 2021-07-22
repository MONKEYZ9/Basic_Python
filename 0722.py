i = 0
# while i < 10:
#     # print(i)
#     i += 1

#     # if i >= 3:
#     #     print('반복문 종료')
#     #     break

#     if i % 2 == 0:
#         continue
#     print(i)
# for i in range(3, 31, 3):
#     print(i)

# result = 1
# for i in range(1, 101):
#     result *= i
# print(result)

# for i in range(5):
#     print('')
#     for i2 in range(5):
#         print('*', end='')
# count = 1

# for i in range(5):
#     print('')
#     for i2 in range(count):
#         print('*', end='')
#     count += 1

# x = int(input())

# for i in range(x, 0, -1):
#     print(f'x={i}')

# for i in range(1, x+1):
#     if i % 10 == 0:
#         print(i, '\n')
#     else:
#         print(i, end=' ')

# import random


# n = int(input())

# lottoNumberList = []
# for i in range(n):
#     lottoNumber = random.sample(range(1,46), 6)
#     lottoNumber.sort(reverse=False)
#     lottoNumberList.append(lottoNumber)
# lottoNumberList.sort(reverse=False)

# print(lottoNumberList)


# for i in range(5):
#     print('*' * 5)

# for i in range(5):
#     print('*' * int(i+1))

import random

n = int(input())
for i in range(n):
    lottoNumber = random.sample(range(1,46), 6)
    lottoNumber.sort(reverse=False)
    print(lottoNumber)