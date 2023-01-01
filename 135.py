def binary(n,arr):
    na = []
    for i in arr:
        b = ''
        while i:
            b += str(i % 2)
            i //= 2
        b = b[::-1]
        while len(b) < n:
            b = '0' + b
        na.append(b)
    return na

def solution(n, arr1, arr2):
    arr1 = binary(n, arr1)      # ['01001','10100','11100','10010','01011']
    arr2 = binary(n, arr2)      # ['11110','00001','10101','10001','11100']
    answer = []                 # ['#####','# # #','### #','#  ##','#####"]
    for i in n:
        answer += str(int(arr1[i]) + int(arr2[i]))
    print(answer)


    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]



