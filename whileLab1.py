# 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력
import random

x = 1
y = random.randint(5,10)

while x <= y:
    print(x,"->",x ** 2)
    x += 1