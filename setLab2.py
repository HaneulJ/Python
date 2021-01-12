"""
비어있는 셋을 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데
당연히 여기서도 동일한 숫자가 중복하여 저장되지 않게 한다.
수행 결과 >> 행운의 로또번호  : X, X, X, X, X, X

"""
import random
s = set()
while True:
    s.add(random.randint(1,45))
    if len(s) == 6:
        break
print("행운의 로또번호:",s)