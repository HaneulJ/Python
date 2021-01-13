"""함수명 : print_gugudan, 매개변수 : 1개
   리턴값 : 없음, 기능 : 전달된 숫자의 구구단을 출력한다.
- 전달된 아규먼트가 int 타입인지  체크하고 int 타입이 아니면 그냥 리턴한다.
- 전달된 아규먼트가 1~9 사이인지 체크하고 아니면 그냥 리턴한다.
- 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다
"""
def print_gugudan(n):
    if type(n) == int :
        if 1 <= n <= 9:
            for hang in range(1,10):
                print(n,"*", hang, "=", n*hang)

# if - else: pass 가능

print_gugudan(3)
print_gugudan(7)