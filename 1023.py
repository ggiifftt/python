h,m = input().split()
h = int(h)
m = int(m)
if m < 45:
    if (h != 0):
        print(h-1, m+15)
    else:
        print(23, m+15)
elif m >= 45:
    print(h, m-45)


a,b = input().split()
a = int(a)
b = int(b)
c = int(input())
if b+c < 60:
    print(a, b + c)
elif b+c >= 60:
    if a + ((b + c)//60) >= 24:
        print((a+(b+c)//60) - 24, (b+c)%60)
    elif a + ((b + c)//60) < 24:
        print(a+(b+c)//60, (b+c)%60)


a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
p = 0
if a == b == c:          # 3 같은눈
    p = 10000 + a * 1000
elif a == b and b != c:  # 2 같은눈
    p = 1000 + a * 100
elif a == c and b != c:
    p = 1000 + c * 100
elif b == c and b != a:
    p = 1000 + b * 100
else:                    # 다 다른눈
    p = max(a,b,c) * 100
print(p)


n = int(input())
for _ in range(n):
    num, string = input().split()
    num = int(num)
    output = ''
    for s in string:
        output += s * num
    print(f"output = {output}, s = {s}, num = {num}")


string = input().upper()
string_s = list(set(string))
cnts = []
for s in string_s:
    cnts.append(string.count(s))
print(string_s, cnts)
m_num = max(cnts)

if cnts.count(m_num) >= 2:
    print("?")
else:
    idx = cnts.index(m_num)
    print(string_s[idx])