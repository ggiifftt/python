# 반복문
# while문 : 조건에 충족되는 동안 반복함

# while 조건:       조건이 참이 되는 동안 실행
#     실행문

a = 3
while a:      # a가 0이 될 때까지 == a가 0이 되면 반복을 종료
    print(a)  # a가 0이 아닌동안 실행
    a -= 1    # a = a - 1

a = 3
while True:   # 무한루프
    print(a)
    a -= 1
    if a == 0:
        break #반복문 탈출코드
print('끝')

a = 0
while a < 100:
    if a == 10:
        break
    a += 1
    if a % 2 == 0:
        continue # 다음 코드를 건너뛰고 그 다음 코드 실행
    print(a)

# for문 : 반복 횟수가 주어졌을 경우 사용됨

# for 변수 in range(), "문자열", ['리스트'], ('튜플'), {'딕셔':'너리'}:
#     실행문

s = '문자열'
l = ['리','스','트']
t = ('튜','플')
d = {'딕':'셔', '너':'리'}

for i in s:
    print(i)

n = 5
r = range(n)    # n = 정수, range = 0부터 n-1까지의 범위를 만들어 준다.
print(list(r))

for i in range(10,0,-1):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,6):             #i = 1~3
    for j in range(6,11):        #j = 4~6
        for k in range(11,16):   #k = 7~9
            print(f"i = {i}, j = {j}, k = {k}")