n, m = input().split()
n = int(n)  # 3
m = int(m)  # 3
A = []
B = []

for _ in range(n):
    x = input().split()
    A.append(x)
for _ in range(n):
    x = input().split()
    B.append(x)
for x in range(n):
    for y in range(m):
        print(int(A[x][y]) + int(B[x][y]), end=' ')
    print()