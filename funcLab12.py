"""
함수명 : myprint
   매개변수 : 가변 아규먼트1개, 가변 키워드 아규먼트 1개
   리턴값 : 없음
   기능 : 전달되는 아규먼트의 개수에는 제한이 없다.
         호출시 전달되는 아규먼트의 데이터 타입에도 제한이 없다.
         아규먼트가 전달되지 않으면 “Hello Python”을 출력한다.
         화면 출력은 print() 함수를 사용하며 개행 처리는 기본이며 변경 불가로 정한다.
"""
def myprint(*p, **k):
    deco = k.get('deco', "**")
    s = k.get('sep', ",")

    result = ''
    if len(p) == 0:
        print("Hello Python")
    else:
        result += deco
        for i in range(len(p)):
            result += str(p[i])
            if i < (len(p)-1):
                result += s
        result += deco
        print(result)

myprint(10,20,30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")


# 꼭 다시해보기
