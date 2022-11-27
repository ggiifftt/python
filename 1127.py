def myreplace(string,old,new):
    result = ""
    for i in string:
        if i == old:
            result += new
        else:
            result += i
    return result
print(myreplace("Hello","H","D"))


def solution(num1, num2):
    answer = num1 * num2
    return answer
n1 = 3
n2 = 4
print(solution(n1,n2))


def solution(num1, num2):
    answer = num1 - num2
    return answer
n1 = 2
n2 = 3
print(solution(n1-n2))


def solution(num1, num2):
    answer = 0
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
print(solution())


def solution(sides):
    if sides[2] < sides[0] + sides[1]:
     return 1
    else:
     return 2
s = [1,2,3]
ss = [199, 72, 222]
print(solution(s))
print(solution(ss))
