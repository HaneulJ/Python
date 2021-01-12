"""
다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
     'B', 'C', 'A', 'A'
     'C', 'C', 'B', 'B'
     'D', 'A', 'A', 'D'
다음 내용으로 구성되는 리스트를 하나 생성한다.
    첫 번째 원소에는 'A' 문자의 개수
    두 번째 원소에는 'B' 문자의 개수
    세 번째 원소에는 'C' 문자의 개수
    네 번째 원소에는 'D' 문자의 개수
다음과 형식으로 출력한다.
    A 는 x개 입니다.
    B 는 x개 입니다.
    C 는 x개 입니다.
    D 는 x개 입니다.
"""
data = [['B','C','A','A'],
        ['C','C','B','B'],
        ['D','A','A','D']]
count1, count2, count3, count4 = 0,0,0,0

for i in data:
        for g in i:
                if g == "A":
                        count1 += 1
                elif g == "B":
                        count2 += 1
                elif g == "C":
                        count3 += 1
                else:
                        count4 += 1

result = [count1, count2, count3, count4]

for n in range(4):
        print(chr(65+i),"는", result[i], "개 입니다.", sep="")

# 수정하기