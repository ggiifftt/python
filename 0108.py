def binary(arr,n):
    newarr = []
    for i in arr:
        b = ''
        while i:
            b += str(i % 2)
            i //= 2
        b = b[::-1]
        while len(b) < n:
            b = '0' + b
        newarr.append(b)
    return newarr


def solution(n, arr1, arr2):
    arr1 = binary(arr1, n)      # ['01001','10100','11100','10010','01011']
    print(arr1)
    arr2 = binary(arr2, n)      # ['11110','00001','10101','10001','11100']
    print(arr2)

    answer = []                 # ['#####','# # #','### #','#  ##','#####"]
    for j in range(n):
        result = ''
        for k in range(n):
            if arr1[j][k] == '0' and arr2[j][k] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    return answer               # ['#####','#####','#####','#####','#####']
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))

def olution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1):
        cnt = food[i] // 2
        f = str(i) * cnt
        answer = f + answer + f

    return answer

fd1 = [1, 3, 4, 6] # "1223330333221"
fd2 = [1, 7, 1, 2] # "111303111"
print(olution(fd1))