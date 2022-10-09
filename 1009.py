total_cost =  int(input())
n = int(input())
real_cost = 0

for o in range(n):
    a,b = input().split()
    a: int = int(a)
    b = int(b)
    p = a * b
    real_cost += p

if total_cost == real_cost:
    print('Yes')
else:
    print('No')

n = int(input())
copy = n
c = 0

while True:
    c += 1
    t = (copy // 10) + (copy % 10)
    copy = copy % 10 * 10 + t % 10
    print(f"cycle = {c}, copy = {copy}, n = {n}")
    if n == copy:
        break
print(c)