"""
함수명 : myemail_info
매개변수 : 이메일 주소 문자열 1개
리턴값 : 2개의 원소를 갖는 튜플
기능 : 전달된 이메일 주소 문자열에서 @ 를 기준으로 쪼개서 튜플을 만들어 리턴한다.
      단, 전달된 문자열에 @가 없으면 None을 리턴한다.
"""
def myemail_info(address):
    if "@" in address:
        ad = tuple(address.split("@"))
        return ad
    else:
        return None


print(myemail_info("gksmfdl0510@naver.com"))
print(myemail_info("haneulj@gmail.com"))
print(myemail_info("HaneulJ"))