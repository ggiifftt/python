def average(n,*scores):
    print(f"n = {n}, *scores = {scores}")
    total = 0
    for s in scores:
        total += s
    return total / n
과목수 = 5
국어 = 95
수학 = 90
영어 = 80
과학 = 85
사회 = 75
평균 = average(과목수, 국어, 수학, 영어, 과학, 사회)
print(평균)



def testkwargs(**kwargs):
    print(kwargs)
ka = "에이"
a = 3
kb = "비"
b = 5
result = testkwargs(ka = a, kb = b)



def introduce_myself(name, age, job = "학생"):
    print(f"제 이름은 {name}이고, 나이는 {age}살 이며, 직업은 {job}입니다.")
ㅇ = "이병권"
ㅂ = 14
ㄱ = "학생"
print(introduce_myself(ㅇ,ㅂ))



def mypop(_list, index = -1):
    # 매개변수 index에 값이 들어오지 않을 경우 가장 마지막 값을 추출한다.
    if index == -1:
        return _list[:index],_list[index]
    # 그게 아니면 index에 들어온 정수번째 값을 추출한다.
    else:
        newlist = []
        for i in range(len(_list)):
            if i != index:
                newlist.append(_list[i])
        return newlist, _list[index]
a = [4,6,25,31]
print(mypop(a))   # ([4,6,25],31)
print(mypop(a,0)) # ([6,25,31],4)



def test(a,b):
    return a+b,a*b,a-b,a/b
a = 3
b = 4
print(test(a,b))



a = 5
def function(a):
    a = 6
function(a)
print(a)



def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4



def olution(before,after):
        for i in before:
            if before.count(i) != after.count(i):
                return 0
        return 1
print(olution("olleh", "hello"))



def solution(emergency):