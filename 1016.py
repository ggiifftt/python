N = int(input())
for i in range (N):
    i += 1
    print('*' * i)


N = int(input())
for i in range (N):
    i += 1
    print(' ' * (N-i) + '*' * i)


N,X = input().split()
N = int(N)
X = int(X)
A = input().split()
for i in range(N):
    A[i] = int(A[i])

for i in A:
    if i < X:
        print(i)

A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

print(A // (C-B) + 1)

l = 1 # (층)
r = 1 # (방)
# l층까지 건너는 방 수:1+6(l-1)
n = int(input())
while r < n:
    l += 1
    r += 6 * (l-1)
print(l)