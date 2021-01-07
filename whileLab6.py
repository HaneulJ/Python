"""숫자를 하나 입력받는다.
- 입력된 숫자가 0 이면 “종료”라는 메시지를 출력하고 수행을 종료한다.
- 입력된 숫자가 -10 보다 작거나 10보다 크면 입력 받는 것부터 다시 시작한다.
- 입력된 숫자가 양수이면 “입력값 : x” 행을 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한
  결과를 출력한다.
- 입력된 숫자가 음수이면 양수로 변경하여 “입력값(부호변경) : x” 를 출력한 다음 행에 1부터 입력된
  숫자 값까지의 곱한 결과를 출력한다.
"""

while True:
    i = int(input("숫자를 입력하세요:"))
    if i == 0:
        print("종료")
        break
    elif i < -10 or i > 10:
        continue
    elif i > 0:
        mul = 1
        for data in range(1,i+1):
            mul *= data
    else:
        i *= -1
        print("입력값(부호변경)",i)
        mul = 1
        for data in range(1, i+1):
            mul *= data
    print(mul)