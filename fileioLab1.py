"""
다음 내용을 생성해서 c:/iotest/today.txt 라는 파일에 저장한다.
c:/iotest 디렉토리의 존재여부를 채크하고 존재하지 않으면 새로이 생성한다.
출력 내용은 다음과 같습니다. (XXX는 본인의 별명(^^))

오늘은 2021년 01월 18일입니다.
오늘은 월요일입니다.
나는 X요일에 태어났습니다.

파일에 위의 내용을 저장한 다음에 화면에는“저장이 완료되었습니다.”를 출력한다.
"""
import os
import time
import calendar

now = time.localtime()
week = ['월','화','수','목','금','토','일']

if not os.path.isdir("c:\\iotest"):
    os.makedir("c:\\iotest")

f = open("c:\\iotest\\today.txt", "wt", encoding="UTF-8")
f.write(f"""오늘은 {now.tm_year}년 {now.tm_mon:02d}월 {now.tm_mday:02d}일입니다.
오늘은 {week[calendar.weekday(now.tm_year, now.tm_mon, now.tm_mday)]}요일입니다.
나는 {week[calendar.weekday(1997,5,10)]}요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")

# f.write(f"""~~~""")로 f를 먼저 써줘야 문자열안에 있는 {}들이 실행된다.
