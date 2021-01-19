m = int(input("숫자를 입력하시오:"))

while True:
    if m == 1 or m== 2 or m == 12:
        print(m,"월은 겨울", sep="")
    elif 3 <= m <= 5:
        print(m, "월은 봄", sep="")
    elif 6 <= m <= 8:
        print(m, "월은 여름", sep="")
    elif 9 <= m <= 11:
        print(m, "월은 가을", sep="")
    else:
        print("1~12사이의 값을 입력하세요!")
    break