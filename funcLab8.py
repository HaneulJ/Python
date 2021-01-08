"""구현해야 하는 함수 사양
   함수명 : print_triangle_withdeco
   매개변수 : 2개
            숫자와 데코문자
            여기에서 데코문자는 기본값을 갖는다. 기본값은 ‘%’로 정한다.
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         숫자 2 만 전달시
           %
         %%
         숫자 5 와 데코문자 ‘*’ 전달시
             *
            **
           ***
          ****
         *****
        전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는
        처리하지 않는다.
"""

def print_triangle_withdeco(n,d="%"):
    for n in range (1,n+1):
        for i in range(10-n):
            print(" ", end="")
        for i in range(n):
            print(d, end="")
        print()



print_triangle_withdeco(6,)
print_triangle_withdeco(5, "*")