# 1부터 6사이의 두 개 난수를 추출하여 pairNum1,2에 저장하고 추출한 값을 비교한다.

import random

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    if pairNum1 != pairNum2:
        if pairNum1 > pairNum2:
            print("pairNum1이 pairNum2보다 크다.")
        else:
            print("pairNum1이 pairNum2보다 작다.")
    else:
        print("게임 끝")
        break