""" 비어있는 리스트를 하나 생성하여 listnum 이라는 변수에 저장한다.
1~50 사이의 난수를 10개 추출하여 listnum 에 추출 순서대로 저장한다. (for문 사용)
listnum의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
"""
import random
listnum = []

for i in range(10):
    listnum.append(random.randint(1,50))
print(listnum)

# 리스트에서 10보다 작은 값들은 100으로 변경한다. (for문 사용)
# listnum의 모든 값들을 출력한다.(이 때 반복문을 사용하지 않아도 된다.)
for n in range(10):
    if listnum[n] < 10:
        listnum[n] = 100
print(listnum)

# 인덱싱 방법으로 첫번째 데이터 출력
print(listnum[0])

# 인덱싱 방법으로 마지막 데이터 출력: -1
print(listnum[-1])  # listnum[len(listnum)-1]

# 슬라이싱 방법으로 listnum의 두번째 데이터부터 여섯번째 데이터만 출력
print(listnum[1:6])

# 슬라이싱 방법으로 listnum의 데이터를 역순으로 출력
print(listnum[::-1])

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력
print(listnum[:])

# 인덱싱 방법으로 5번째 데이터를 삭제
del listnum[4]

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력
print(listnum[:])

# 슬라이싱 방법으로 2~3번째 데이터를 삭제
listnum[1:3]=[]

# 슬라이싱 방법으로 listnum의 데이터를 모두 출력
print(listnum[:])
