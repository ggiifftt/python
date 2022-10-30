S = input()
A = "abcdefghijklmnopqrstuvwqxyz"

for i in A:
    if i in S:
        print(S.index(i), end = "   ")
    else:
        print(-1, end = "   ")


A,B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)


A = input()
B = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in A:
    for j in B:
        if i in j:
            time += B.index(j) + 3
print(time)


string = input()
cnt = len(string)
ct = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj' 's=', 'z=']

for i in ct:
    cnt -= string.count(i)
print(cnt)


n = int(input())
cnt = n
for _ in range(n):
    string = input()
    for i in range(len(string)-1):
        if string[1] == string[i+1]:
            continue
        elif string[1] in string[i+1:]:
            cnt -= 1
            break
print(cnt)