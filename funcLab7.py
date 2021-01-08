"""함수명 : differtwovalue, 매개변수 :  2개
   리턴값 : 연산 결과, 기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴 두 값이 동일하면 0 을 리턴한다.
1부터 30 사이의 난수 2 개를 추출하여 2번에서 구현된 함수를 호출하고 결과를 다음 형식으로 출력한다.
"X 와 Y 의 차는 W 입니다."

"""

def differtwovalue(x,y):
    w = abs(x-y)
    return w

import random
for i in range(1,6):
    x = random.randint(1,30)
    y = random.randint(1,30)
    print(x,"와",y,"의 차는",differtwovalue(x,y),"입니다.")