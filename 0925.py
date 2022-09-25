# 문자열 (str)
# a = "Hello World"

# 인덱싱, 슬라이싱 = 인덱스 번호를 사용해서 하나 또는 범위를 집어내는 행위
# print(a[0])  # H
# print(a[2:5])  # llo

# 문자열 연산 (+,*)
# b = "Hello"
# c = "Python"
# print(b + " " + c)
# print(b * 3)

# 문자열 특징 = immutable (변하지 않는다.)

# 리스트 (lsit)
# l1 = [1, 2, 3, 'a', 'b', 'c', [1, 2, 3, 4]]

# 삭제
# l2 = [1,2,3,4]
# del l2[3]
# print(l2)
# 덧셈은 리스트끼리, 곱셈은 정수끼리

# 튜플 (tuple)
# t1 = (1, 2, 3, 4)
# t2 = 1, 2, 3, 4
# t3 = (1,)  # 콤마를 붙히지 않으면 정수로 인식

# 딕셔너리 (dictionary)
# d = {'key': 'value'}  # key 값이 중복될 경우 맨 뒤의 value 출력
# print(d['key'])
# 추가 삭제 수정
# 추가, apple : 사과
# d['apple'] = '사과'
# print(d)

# 수정, apple : 파인애플
# d['apple'] = '파인애플'
# print(d)

# 삭제, apple
# del d['apple']
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# 집합 (set)
# s1 = {1,2,3.4}
# s2 = set()  #비어있는 집합
# print(type(s2))

# 집합의 특징
# 1. 중복된 값을 제거한다
# 2. 순서가 없다 = 인덱스 번호를 사용할 수 없다
a = True
b = False
print(type(a))
print(type(b))

# 자료형들의 참과 거짓                  값이 있으면 참, 없으면 거짓
# print(bool('python'), bool(''))   문자열
# print(bool([1, 2, 3]), bool([]))  리스트
# print(bool((1, 2, 3)), bool(()))  튜플
# print(bool({'a': 1}), bool({}))   딕셔너리
# print(bool(3), bool(0))           정수 (0을 제외한 모든 숫자는 참)
# print(bool(None))                 None (그냥 없다)

a = 3

if a == 3:
    print('a')
else:
    print('b')

a = 5
if a > 4:
    print('a')
elif a < 4:
    print('b')
else:
    print('c')

# 비교 연산자 (A 비교연산자 B)
# A > B => A가 B보다 크다
# A < B => A가 B보다 작다
# A == B => A와 B는 같다
# A != B => A와 B는 다르다

# A >= B => A는 B보다 크거나 같다
# A <= B => A는 B보다 작거나 같다

# 논리 연산자 (and그리고, or또는, not부정)
a, b, c, d = [3, 4, 5, 3]
if a == d and b < c:
    print(True)
else:
    print(False)

if a == d or b > c:
    print(True)
else:
    print(False)

if not a:
    print(True)
else:
    print(False)

# in ~안에 있는
l1 = ['a', 'b', 'c', 'd']
var = 'a'
if var in l1:
    print(True)
else:
    print(False)

# 111
# s = input()
# print(s * 2)

# 112
# i = int(input('숫자를 입력하세요:':))
# print(i + 10)

# 113
# i = int(input('숫자를 입력하세요:'))
# if i % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 114
# i = int(input('입력값: '))
# i += 20
# if i > 255:
#     print('출력값: 255')
# else:
#     print('출력값:', i)
#
# 115
# i = int(input('입력값: '))
# i -= 20
# if i > 255:
#     print('출력값: 255')
# elif i < 0:
#     print('출력값: 0')
# else:
#     print('출력값:', i)

# 116
# time = input('현재시각:')
# if time.split(':')[1] == "00":
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다')

# 117
# fruit = ["사과", "포도", "홍시"]
# f = input('과일을 입력하세요: ')
# if f in fruit:
#     print('정답입니다')
# else:
#     print('오답입니다')

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
s = input('제가 좋아하는 계절은:')
if s in fruit:
    print('정답입니다')
else:
    print('오답입니다')

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
s = input('좋아하는 과일은:')
if s in fruit.values:
    print('정답입니다')
else:
    print('오답입니다')