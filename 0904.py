# 71번
# my_variable = ()
# print(type(my_variable))

# 72번
# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73번
# t1 = (1,)

# 74번
# t = (1, 2, 3)
# t[0] = 'a'

# 75번
# t = 1, 2, 3, 4
# print(type(t))

# 76번
# t = ('a', 'b', 'c')
# t = ('A', 'b', 'c')
# print(t)

# 77번
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = list(interest)
# print(type(interest))

# 78번
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest = tuple(interest)
# print(type(interest))

# 79번
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# 80번
# t2 = tuple(range(2,100,2))
# print(t2)

# 81번
# a, b, *c = (0, 1, 2, 3, 4, 5)
# print(a)   출력값 = 0
# print(b)   출력값 = 1
# print(c)   출력값 = [2, 3, 4, 5]

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score,a,b = scores
# print(valid_score)  출력값 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
# a,b 두 값을 제외한 좌측의 8개의 값 출력

# 82번
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*valid_score = scores
# print(valid_score)  출력값 = [8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b 두 값을 제외한 우측의 8개의 값 출력

# 83번
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,*valid_score,b = scores
# print(valid_score)  출력값 = [8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]
# a,b 두 값을 제외한 가운데 8개의 값 출력

# 84번
# temp = {}
# print(type(temp))

# 85번
# ice_creams = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}

# 86번
# ice_creams = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
# ice_creams['죠스바'] = 1200
# ice_creams['월드콘'] = 1500
# print(ice_creams)

# 87번
# ice_creams = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# print('메로나 가격:',ice_creams['메로나'])

# 88번
# ice_creams = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# ice_creams['메로나'] = 1300
# print(ice_creams)

# 89번
# ice_creams = {'메로나': 1300, '폴라포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# del ice_creams['메로나']
# print(ice_creams)

# 90번
# 누가바가 해당 딕셔너리에 있지 않아서

# a = ['hello']
# b = ['python']
# d1 = dict(zip(a,b))
# print(d1)  {'hello': 'python'}
print('hello, world!')

# set 집합 (순서가 없고 중복되는 문자,숫자는 삭제됨)
s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5])

# 합집합 | (겹치는 부분까지)
print(s1 | s2)  # 출력값 = {1, 2, 3, 4, 5}
# 교집합 & (겹치는 부분만)
print(s1 & s2)  # 출력값 = {3, 4}
# 차집합 - (겹치는 부분 빼고)
print(s1 - s2)  # 출력값 = {1, 2}
print(s2 - s1)  # 출력값 = {5}

# 91번
# inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
# print('91번', inventory)
#
# 92번
# print('92번', inventory['메로나'][0], '원')
#
# 93번
# print('93번', inventory['메로나'][1], '개')
#
# 94번
# inventory['월드콘'] = [500, 7]
# print('94번', inventory)
#
# 95번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice_keys = list(icecream.keys())
# print('95번', ice_keys)
#
# 96번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice_values = list(icecream.values())
# print('96번', ice_values)
#
# 97번
# print('97번', sum(ice_values))
#
# 98번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수': 2700, '아맛나': 1000}
# icecream.update(new_product)
# print('98번', icecream)
#
# 99번
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print('99번', result)
#
# 100번
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print('100번', close_table)
