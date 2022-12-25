def solution(numlist, n):
    answer = []
    for i in range(len(numlist)):
        d = n - numlist[i]
        if d < 0:
            d = -d
        numlist[i] = [d, numlist[i]]
    numlist.sort()
    print(numlist)
    for i in range(len(numlist)):
        if numlist[i - 1][0] == numlist[i][0] and numlist[i - 1][1] < numlist[i][1]:
            answer.insert(i - 1, numlist[i][1])
        else:
            answer.append(numlist[i][1])

    return answer


nl = [1, 2, 3, 4, 5, 6]
n = 4
print(solution(nl, n))


def solution(polynomial):
    notx = []
    inx = []
    ps = polynomial.split(' + ')
    for i in range(len(ps)):
        if ps[i].isdigit():
            notx += ps[i]
            print(notx)
        else:
            if ps[i] == 'x':
                inx += '1x'
            else:
                inx += ps[i]
        for i in range(len(inx)):
            if inx[i] == 'x':
                inx.pop(i)


print(solution("3x + 7 + x"))