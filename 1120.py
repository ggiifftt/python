#피자1
n = int(input())
m = str(n/7)
M = int(m.split(".")[0])
print(M + n%7)

n = int(input())
if n % 7 == 0:
    result = n // 7
else:
    result = n // 7 + 1
print(result)


#피자2
n = int(input())
result = 0
while True:
    result += 1
    if result*6%n == 0:
        break
print(result)


#피자3
slice = int(input())
n = int(input())
if n % slice == 0:
    result = n // slice
else:
    result = n // slice + 1
print(result)


#영싫
numbers = input()
str_nums = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4",
            "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
for s in str_nums:
    if s in numbers:
        numbers = numbers.replace(s,str_nums[s])
        print(numbers)
numbers = int(numbers)


#모음제거
my_string = input()
ct = ['a','e','i','o','u']
for s in ct:
    if s in my_string:
        my_string = my_string.replace(s,"")
        print(my_string)

my_string = input()
ct = ['a','e','i','o','u']
result = ''
for s in my_string:
    print(result,s)
    if s in ct:
        continue
    result += s