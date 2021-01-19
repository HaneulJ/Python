"""
Member클래스에는 아규먼트를 받지 않는 __init__(self) 한 개만을 구현하고
이 안에서는 생성된 객체안에 name, account, passwd, birthtyear변수를 만들고 값을 None으로 대입한다.
다른 멤버는 더 이상 구현하지 않는다.

Member 클래스의 인스턴스(객체)를 3개 생성하고 생성된 객체의 각 멤버 변수에 임의의 정보를 각각 저장한다.
객체에 저장된 각 정보를 추출하여 다음 형식으로 출력
회원1 : 이름(계정,암호,생년)
회원2 : 이름(계정,암호,생년)
회원3 : 이름(계정,암호,생년)
rint("%s의 잔액은 %s원입니다." % (name, format(balancedooly, ',')))

"""
class Member:
    def __init__(self):
        self.name=None
        self.account=None
        self.passwd=None
        self.birthyear=None

m1 = Member()
m2 = Member()
m3 = Member()

m1.name = "정하늘"
m1.account = "abc"
m1.passwd = 123
m1.birthyear = 1997

m2.name = "정다솜"
m2.account = "def"
m2.passwd = 456
m2.birthyear = 1995

m3.name = "정아름"
m3.account = "ghi"
m3.passwd = 789
m3.birthyear = 1993

print(f"회원1:{m1.name},{m1.account},{m1.passwd},{m1.birthyear}")
print(f"회원2:{m2.name},{m2.account},{m2.passwd},{m2.birthyear}")
print(f"회원3:{m3.name},{m3.account},{m3.passwd},{m3.birthyear}")