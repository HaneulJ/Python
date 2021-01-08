# 0부터 30사이의 난수를 추출한다.
# 추출된 숫자가 1이면 'A', 2 이면 'B', ... 26이면 'Z' 를 출력하는데
# 계속 난수 추출과 출력을 반복하다가 난수가 0이 추출되거나
# 27~30이 추출되면 반복을 끝낸다.
# 마지막에는 "수행횟수는 x 번입니다"를 출력하고 종료한다. 수행 횟수는 출력을 기준으로 계산한다.
# 참고: print(ord("A")), print(chr(65))

import random
count = 0

while True:
    alp = random.randint(0, 30)
    if 1 <= alp <= 26:
        count += 1
        print(chr(alp+64),"(",alp,")")
    else:
        break

print("수행횟수는",count,"번입니다.")
