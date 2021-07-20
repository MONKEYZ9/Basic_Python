import numpy as np
# food1 = int(input('내가 먹은 음식의 가격 : '))
# food2 = int(input('나가 먹은 음식의 가격 : '))

# print(food1 + food2)

# 사칙연산
# print(10+20)
# print(10-20)
# print(10/20)
# print(10*20)


# 월세 = int(input('월세는 :'))
# 관리비 = int(input('관리비 :'))

# print(월세 + 관리비)
# print(월세 - 관리비)
# print((월세 + 관리비)*12)

# orders = ['짜장', '짬뽕', '탕수육']
# 리스트안에 있는 것을 elements라고 함
# 각각의 것으로 index로 0 1 2 로 정해진다.
# print(orders[2])


# numbers = [1,2,3,4,5,6,7]
# print(numbers)


# orders = ['짜장', '짬뽕', '탕수육']

# orders.append('냉면')
# orders.insert(3, '비빔냉면')
# orders.insert(9, '양장피123')

# del orders[-1]
# orders.remove('짜장')
# # orders.remove('짬뽕')
# del orders[0]

# print(orders)


# print(len(orders))

# name = '안녕하세요 이상민입니다.'
# print(len(name))

# num = [20,30,40,50,10, 12, 123]
# # print(num)

# # print(sum(num))

# print(sum(num)/len(num))
# print(np.average(num))

# print(max(num))
# print(min(num))

# menu = {'짜장' : 4000, '짬뽕' : 9000, '탕수육': 12000}

# menu['냉면'] = 7000
# menu['중국식 냉면'] = 9000
# menu['탕수육'] = 8500
# menu['짜장'] = 4500

# del menu['짜장']
# del menu['짬뽕']
# del menu['탕수육']
# print(menu)

# myGrade = int(input('학번을 입력하시기 바랍니다 : '))
# yourGrade = int(input('학번을 입력하시기 바랍니다 : '))

# print(myGrade == yourGrade)
# print(myGrade != yourGrade)
# print(myGrade >= yourGrade)
# print(myGrade <= yourGrade)
# print(myGrade > yourGrade)
# print(myGrade < yourGrade)


# if myGrade == yourGrade:
#     print('같네')

# elif myGrade > yourGrade:
#     print('후배님')
# elif myGrade < yourGrade:
#     print('선배님')
# else:
#     print('who??')

# orders = ['짜장', '짬뽕', '탕수육']

# food = input('what do u wanna eat? ')

# if food in orders:
#     print('u can order now')
# else:
#     print('u cant order now')

# menu = {'짜장' : 4000, '짬뽕' : 9000, '탕수육': 12000}
# food = input('what do u wanna eat? ')

# if food in menu:
#     print(menu[food], 'won')
# else:
#     print('u cant order now')

# while 10 < 90:
#     print('멈추지 않는 와일문')
# i =  6
# while i > 0:
#     print(i)
#     i -= 1
