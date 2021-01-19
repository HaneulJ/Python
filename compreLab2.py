"""
함수명 : mydict
매개변수 : 가변 키워드형(키=값 형식으로 전달받을 수 있는 아규먼트 개수에 제한이 없다.)
리턴값 : 1개
기능 : funcLab11.py 에서 구현한 mydict() 라는 함수의 기능과 동일하게 구현하는데 이번에는 딕셔너리 컴프리핸션(지능형 딕셔너리) 구문을 사용해서 생성한다.
"""

def mycompredict(**p):
    mdict = { "my"+k:v for k,v in p.items() }
    return mdict

print(mycompredict())
print(mycompredict(a=1, b=3, c=5))
