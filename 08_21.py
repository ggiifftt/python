name = '김민수'
age = 10

# % - formatting
print('이름: %s 나이: %d' %(name, age))
# 포멧 메소드
print('이름: {0} 나이: {1}'.format(name,age))
# f-string
print(f'이름: {name} 나이: {age}')

a = 'hello'
b = a.capitalize()  #capitalize = 0번째 인덱스의 문자를 대문자로 변경시킨다.
print(b)

file_name = '보고서.xlsx'
print(file_name.endswith('xlsx'))

file_name = '2020_보고서.xlsx'
print(file_name.startswith('2020'))

l = [] #l은 비어있는 리스트
a = [1,2,3] #a는 원소 1, 2, 3이 들어있는 리스트
b = ['A','B','C'] #b는 'A', 'B', 'C'가 들어있는 리스트
c = [1,2,'A','B'] #c는 1,2,'A','B'가 들어있는 리스트
d = [[1,2,3],[4,5,6]] #d는 [1,2,3], [4,5,6]이 들어간 리스트

print(a[0])
print(b[0])
print(d[0])
print(len(a)) #리스트의 길이 = 리스트가 가지고 있는 원소의 개수

A = [4,1,2,[5,8,[9,7],3],6]
print(A)          # [4,1,2,[5,8,[9,7],3],6]
print(A[3])       # [5, 8, [9, 7], 3]
print(A[3][2])    # [9, 7]
print(A[3][2][1]) # 7

a = [4,1,3,2]
b = [5,8,6]
#리스트의 원소(값) 수정
a[2] = 5 #리스트 a에서 2번째의 위치한 값을 5로 수정
print(a) #[4, 1, 3, 2] => [4, 1, 5, 2]

#리스트의 원소(값) 삭제
a = [4,1,3,2]
del a[2] #리스트 a에서 2번째의 위치한 값을 삭제
print(a) #[4, 1, 3, 2] => [4, 1, 2]

#리스트 끼리의 덧셈
a = [4,1,3,2]
print(a+b)   #[4,1,3,2]+[5,8,6]=[4, 1, 3, 2, 5, 8, 6]

#리스트 끼리의 곱셈
print(b * 3) #[5, 8, 6, 5, 8, 6, 5, 8, 6]

#원소 추가
a.append(5) #append(값) = 리스트의 마지막 인데스 번호에 값을 추가한다.
print(a)    #[4, 1, 3, 2, >>5<<]

#원소 삽입
a = [4,1,3,2]
a.insert(2,8) #insert(인덱스번호, 값) = 리스트의 해당 인덱스 위치에 값을 삽입한다.
print(a)      #[4, 1, 8, 3, 2]

#순서 반전
a = [4,1,3,2]
a.reverse() #reverse() = 리스트의 순서를 반전시킨다.
print(a)    #[2, 3, 1, 4]

#정렬
a.sort() #sort() = 리스트의 순서를 정렬한다. (정렬 기준은 크기, 기본은 오름차순)
print(a) #[1, 2, 3, 4]

a.sort(reverse = True) #sort(reverse = True) = 리스트의 순서를 '내림차순으로' 정렬한다.
print(a) # [4, 3, 2, 1]

#원소 추출
a = [4,1,3,2]
print(a.pop()) #pop() = 마지막 인덱스 번호에 위치한 값을 추출
               #pop(2) = 2번째 인덱스 번호에 위치한 값을 추출
               #[4, 1, 3]
print(a)       #3

#index
a = [4,1,3,2]
print(a.index(2)) #index(값) = 리스트 내에 해당한 값이 있는지 확인
                 #있을 경우 인덱스 번호를, 없을 경우 에러 반환

#원소 제거
a = [4,1,3,2]
a.remove(3) #remove(값) = 리스트 내에 해당 값을 삭제
            #없는 값을 삭제할 경우 에러 반환
print(a) #[4, 1, 2]

#리스트 확장
a = [4,1,3,2]
b = [7,8,9]
a.extend(b)    #extend(리스트, 튜플 등 순서사 있는 자료형) ==> 괄호 안에 적은 자료형의 길이만큼 확장
print(a)       #[4, 1, 3, 2, 7, 8, 9]

a = [4,1,3,2]
a.append(b)    #append(값/자료형) ==> 자료형의 길이와 상관없이 마지막 인덱스에 추가
print(a)       #[4, 1, 3, 2, [7, 8, 9]]


#51.
movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)

#52.
movie_rank.append('배트맨')
print(movie_rank)

#53.
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

#54.
del movie_rank[3]
print(movie_rank)

#55.
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#56.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs) #['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

#57.
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))  #min(값1,값2,값3,...) = 여러 값들 중 최소값을 반환
print(max(nums))  #max(값1,값2,값3,...) = 여러 값들 중 최대값을 반환

#58.
nums = [1, 2, 3, 4, 5]
print(sum(nums))  #sum(a) = a안에 있는 값들을 모두 더한 값을 반환,기본값이 0

#59.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60.
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))