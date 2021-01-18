"""
컴프리핸션 구문을 사용해서 다음에 제시된 데이터들로 구성되는 자료구조를 생성한다.
(1)난수 추출 함수를 사용하여 0 부터 100 사이의 값 10개로 구성되는 리스트를 하나 생성한다.
(2) 위에서 생성된 리스트를 이용하여 다음과 같이 구성되는 딕셔너리를 생성한다.(추출된 점수가 60점 이상이면 pass, 60점 미만이면 nopass 로 처리한다.)
"""

import random

# _는 구문적으로 변수는 와야하나 사용은 안한다는 뜻
list1 = [ random.randint(0,100) for _ in range(10)]
print(list1)

dict1 = { (list1.index(i)+1): "pass" if i > 60 else "nopass" for i in list1}
print(dict1)
