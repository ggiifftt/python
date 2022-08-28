price = ['20180728', 100, 130, 140, 150, 160, 170]
print(61, price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(62, nums[1::2])

print(63, nums[::2])

nums = [1, 2, 3, 4, 5]
print(64, nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(65, interest[0], interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(66, ' '.join(interest))

print(67, '/'.join(interest))

print(68, '\n'.join(interest))

string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(69, interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(70, data)

t1 = ()  # 비어있는 튜플
t2 = (2)  # 값이 하나 있는 튜플 = 원소 뒤에 ','를 붙혀서 tuple로 인식시킨다.
print(type(t2))  # <class 'int'> (정수)

t3 = (1, 2, 3)  # 값이 여러개 있는 튜플
print(type(t3))  # <class 'tuple'>

l1 = [1, 2, 3, 4]
t4 = tuple(l1)
print(t4, type(t4))  # 리스트를 튜플로 만들기

# t5 = (1,2,3,4)
# l1 = [1,2,3,4]
# 리스트 수정
# l1[0] = 8
# print(l1) ==> [8, 2, 3, 4] 수정됨

# t5[0] = 8
# print(t5) ===> 에러 반환

# 리스트 삭제
# del l1[0]
# print(l1) ===> [2, 3, 4] 삭제됨

# del t5[0]
# print(t5) ===> 에러 반환

# 튜플은 수정,삭제가 안됨 = 튜플은 변하지 않음(리스트와 다른점)

# 리스트, 튜플의 공통점
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8)
# 1, 인덱싱, 슬라이싱
print(t1[3])  # 출력값 = 4
print(t1[1:3])  # 출력값 = (2, 3)

# 슬라이싱
# 변수 [x,y] ==> 변수의 x번째 index부터 y-1 index까지 범위를 잘라낸다.

# 2 덧셈 곱셈
t3 = t1 + t2
print(t3)  # 출력값 = (1, 2, 3, 4, 5, 6, 7, 8) = (1,2,3,4,5) + (6,7,8)

t4 = t2 * 3
print(t4)  # 출력값 = (6, 7, 8, 6, 7, 8, 6, 7, 8) = (6,7,8) 3번 반복

# 71.
my_variable = ()

# 72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73.
t1 = (1,)  # 튜플에 하나의 원소만 있을 경우 꼭 ','를 붙힌다.

# 74.
# t = (1, 2, 3)
# t[0] = 'a'
# print(t) 에러 반환 >>> 튜플은 변하지 않음

# 75.
t = 1, 2, 3, 4
print(type(t))  # 출력값 = <class 'tuple'>, 소괄호 없이도 원소를 ','로 나열하면 튜플로 인식

# 76.
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 77. 튜플을 리스트로(형변환)
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 78. 리스트를 튜플로(형변환)
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 79.(언팩킹:unpacking = 묶여있는 원소들을 풀어해친다.)
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print('a = %s, b = %s, c = %s' % (a, b, c))  # 언팩킹을 위해 원소를 받아줄 변수가 원소의 개수와 일치해야한다.

# 80. range 함수, range(시작인덱스,끝인덱스,step) ==> 함수사용방법은 슬라이싱과 유사함
t1 = tuple(range(2, 100, 2))
print(80, t1)

print('ㅡㅡㅡㅡ딕셔너리ㅡㅡㅡㅡ')

d1 = {'key': 'value'}
a = 'hello'
b = 'python'
d2 = dict(zip(a, b))
print(type(d1), type(d2))

# 딕셔너리 value의 수정
d1 = {'apple': '사과', 'banana': '바나나'}
d1['apple'] = '파인애플'
print(d1)

# 딕셔너리 key:value 삭제
del d1['banana']
print(d1)

# 딕셔너리 key:value 추가
d1['mango'] = '망고'
print(d1)

d1 = {'A': 1, 'A': 2}
print(d1['A'])  # key가 중복될 시, 가장 뒤에 value를 뽑아냄

d1 = {'A': 1, 'B': 2, 'C': 3}
keys = d1.keys()
print(keys)

d1 = {'A': 1, 'B': 2, 'C': 3}
values = d1.values()
print(values)

items = d1.items()
print(items)

print('A' in d1)  # ('key' in 'dict') ==> True ('dict' 내에 'key'가 있다.)
print('1' in d1)  # ==> false (key가 아닌 value를 입력)
