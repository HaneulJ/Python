"""
함수명 : createList
매개변수 : 가변 아규먼트를 받는 매개변수 1개, 기본값이 있는 매개변수 1개(매개변수 명은 type이며 기본값은 1이다.)
리턴값 : 1개
기능 :가변 아규먼트로 전달되는 값들을 가지고 정해진 규격의 리스트를 생성하여 리턴한다.
     가변 아규먼트가 전달되지 않은 경우에는 1부터 30의 값을 가지고 정해진 규격의
     리스트를 생성하여 리턴한다.
type 이 2이면 주어진 데이터 값들에서 짝수에 해당하는 데이터들만을 가지고 리스트 생성
type 이 3이면 주어진 데이터 값들에서 홀수에 해당하는 데이터들만을 가지고 리스트 생성
type 이 4이면 주어진 데이터 값들에서 10보다 큰 데이터들만을 가지고 리스트 생성
type 이 1이면 주어진 데이터 값들을 모두 가지고 리스트 생성
리스트 생성은 리스트 컴프리핸션(지능형 리스트) 구문을 사용한다.
"""
def createList(*p, type=1):
    if p:
        if type == 1 :
            cList = [i for i in p]
        elif type == 2:
            cList = [i for i in p if not i % 2]
        elif type == 3:
            cList = [i for i in p if i % 2]
        elif type == 4:
            cList = [i for i in p if i > 10]
    else:
        cList = [i for i in range(1,30)]
    return cList

print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=1))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=2))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=3))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=4))
print(createList( ))