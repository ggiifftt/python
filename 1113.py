# n = int(input())
#
# for i in range(n):
#     a = list(input())
#     cnt = 0
#     result = 0
#     for j in a:
#         if j == "O":
#             cnt += 1
#             result = result + cnt
#         else:
#             cnt = 0
# print(result)

#
# c = int(input())
# for _ in range(c):
#     scores = input().split()
#     for i in range(len(scores)):
#         scores[i] = int(scores[i])
#         average = sum(scores[1:]) / scores[0]
#         cnt = 0
#         for j in scores[1:0]:
#             if j > average:
#                 cnt += 1
# print("%.3f%%" %(cnt / scores[0] * 100))

n,k = input().split()
n = int(n)
k = int(k)
service = n // 10
result = n * 12000 + (k - service) * 2000
print("양꼬지: %d인분 / 음료수: 총 %d개 / 서비스 %d개 / 총 %d원" %(n,k,service,result))
print("양꼬지: {}인분 / 음료수: 총 {}개 / 서비스 {}개 / 총 {}원".format(n,k,service,result))
print("양꼬지: {0}인분 / 음료수: 총 {1}개 / 서비스 {2}개 / 총 {3}원".format(n,k,service,result))
print(f"양꼬지: {n}인분 / 음료수: 총 {k}개 / 서비스 {service}개 / 총 {result}원")