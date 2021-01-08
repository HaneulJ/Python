"""구현해야 하는 함수 사양
   함수명 : expr
   매개변수 : 숫자 2개와 연산자 1개, 리턴값 : 연산 결과 또는  None
   기능 : 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
            연산자는 +, -, *, / 만 처리하며 그 외의 연산자는 연산을 하지 않고 None 을 리턴한다.
숫자 2개와 연산자 1개를 전달하여 expr() 이라는 함수를 호출한 다음 리턴 결과가 None 이면 수행 불가 를 출력하고 그렇지 않으면 연산결과 : XX 를 출력한다.
"""
def expr(n1, n2, a):
    if a == "+":
        anw = n1+n2
    elif a == "-":
        anw = n1-n2
    elif a == "*":
        anw = n1*n2
    elif a == "/":
        anw = n1/n2
    else: anw = None
    return anw

result = expr(4,5,"*")
if result != None:
    print("연산결과: ", result)
else:
    print("수행 불가")