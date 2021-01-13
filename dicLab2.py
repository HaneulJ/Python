"""
구성되는 딕셔너리를 하나 생성한다.
키 : 한 글자 요일명(‘월”, ‘화’ …’일’)
값 : 아래 URL 을 참고하여 오늘부터 일요일까지의 날씨정보를 추출하고 최저온도와 최고온도를 튜플로 생성하여 사용한다.
사용자에게 “요일명을 한글로 입력하세요 :”를 출력하면서 칼라명 한 개를 입력받고 미리 생성한 딕셔너리에서 그 칼라에 해당하는 최저온도와 최고온도의 튜플을 추출해서
“x요일의 최저온도는 x 이고 최고 온도는 x입니다” 를 출력하며 딕셔너리에 없는 요일명이 입력된 경우에는 “x요일의 정보를 찾을 수 없습니다”
"""
dic ={'월':(-3,-12), '화':(2,-5),'수':(8,-9),'목':(6,-3),'금':(8,-8),'토':(-3,-13),'일':(-2,-6)}
date = input("요일명을 한글로 입력하세요:")
if date in dic.keys():
    print(date,"의 최저 온도는",dic[date][1],"이고 최고 온도는 ",dic[date][0],"입니다.")
else:
    print(date,"요일의 정보를 찾을 수 없습니다.")


