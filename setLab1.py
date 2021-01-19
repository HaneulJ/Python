"""
비어있는 셋을 2개 만들고 각각 1~20 사이의 숫자 10개를 추출하여 저장한다.
생성된 2 개의 셋에 대하여 집합 연산을 수행하고 결과를 다음과 같이 출력한다.

	집합 1 : {x, x, x, x, x, x, x, x, x, x }
    집합 2 : {x, x, x, x, x, x, x, x, x, x }
    두 집합에 모두 있는 데이터 : {x, x, x, x, x, x, x }
	집합1 또는 집합2 에 있는 데이터 : {x, x, x, x, x, x, x }
	집합1에는 있고 집합2에는 없는 데이터 : {x, x, x, x, x, x, x }
	집합2에는 있고 집합1에는 없는 데이터 : {x, x, x, x, x, x, x }
	집합1과 집합 2가 각자 가지고 있는 데이터 : {x, x, x, x, x, x, x }
"""
import random
s1 = set()
s2 = set()

# while len(s1) == 10 and len(s2) == 10 이면 각 집합의 요소가 10가 됌
for i in range(10):
    n1 = random.randint(1,20)
    s1.add(n1)
    n2 = random.randint(1,20)
    s2.add(n2)
print("집합1:", s1)
print("집합2:", s2)
print("두 집합에 모두 있는 데이터:", s1 & s2)
print("집합1 또는 집합2에 있는 데이터:", s1 | s2)
print("집합1에는 있고 집합2에는 없는 데이터:", s1 - s2)
print("집합2에는 있고 집합1에는 없는 데이터:", s2 - s1)
print("집합1과 집합2가 각자 가지고 있는 데이터:", s1 ^ s2)
