"""
(1) s1 = "pythonjavascript" 에서 의 길이를 출력한다.
(2) s2 = "010-7777-9999" 에서 01077779999 을 출력한다.
(3) s3 = "PYTHON" 에서 NOHTYP 를 출력한다.
(4) s4 = "Python" 에서 python 을 출력한다.
(5) s5 = "https://www.python.org/" 에서 www.python.org 만을 뽑아서 출력한다.
(6) 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별한다. (1,3 : 남자, 2,4 : 여자)

s6 = '891022-2473837'
(7) s7 = '100' 에서 s7 값을 정수형 숫자로 그리고 실수형 숫자로 변환하여 출력한다.
(8) s8 = ' The Zen of Python' 에서 ' n' 문자가 몇 개인지 출력한다.
(9) s8 에서 ' Z'  의 위치를 출력한다.
(10) s8 에서 모두 대문자로 변환한 후 공백단위로 분리해서 리스트로 만들어 출력한다.
"""
s1 = print(len("pythonjavascript"))

s2 = "010-7777-9999".split("-")
for x in s2:
    print(x, end = "",)

s3 = "PYTHON"
print("\n","".join(reversed(s3)))

s4 = "Python"
print(s4.lower())

s5 = "https://www.python.org/"
print(s5[8:22])
i = s5.split("/")
print(i[2])

s6 = ('891022-2473837')
if s6[7] == "1" or s6[7] == "3":
    print("남성")
elif s6[7] == "2" or s6[7] == "4":
    print("여성")

s7 = "100"
print(int(s7))
print(float(s7))

s8 = 'The Zen of Python'
print(s8.count("n"))
print(s8.find("Z"))
print(s8.upper().split(" "))

