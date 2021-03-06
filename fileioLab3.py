"""
제공된 yesterday.txt 파일을 읽고 이 문서에 "Yesterday" 가 몇 개 들어 있는지 개수를 세어서 출력한다. (이 때 대소문자는 구분하지 않는다.)
FileNotFoundError 발생시 파일을 읽을 수 없어요 를 출력하고 종료한다.
에러가 발생하지 않으면 	Number of a Word 'Yesterday' X 를 출력하고 종료한다.
(참고 : X는 9인걸루 예측됨)
에러 발생 여부와 관계없이 수행완료!! 를 출력하고 종료한다.
(try-except-else-finally 를 모두 사용해서 해결한다.)
"""
f =  None # 필수적으로 f를 정의해야 함
try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    text = f.read().lower()
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    print("Number of a Word 'Yesterday':",text.count("yesterday"))
finally:
    print("수행완료!!")
    if f:
        f.close()