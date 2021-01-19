"""
3가지 아규먼트를 전달받아 각 변수에 초기화하는 객체 초기화 메서드
getBookInfo() -> str
Book 클래스의 인스턴스(객체)를 5개 생성하는데 인스턴스를 생성하면서 각각의 객체 생성 함수 호출시 책 정보를 전달한다.
전달되는 책 정보는 우리 파이썬 교재는 필수로 하며 다른 것들은 임의로 정한다.
객체를 모두 생성한 후에 getBookInfo() 를 호출하고 리턴 결과를 다음과 같이 출력
책이름
저자
가격
---------
"""
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def getBookInfo(self):
        print("{}\n{}\n{}".format(self.title, self.author, self.price))
        print("-"*10)

b1 = Book("파이썬 정복","김상형",22000)
b2 = Book("이것이 MariaDB이다","우재남",30000)
b3 = Book("맛있는 MangoDB","정승호",28000)
b4 = Book("파이썬 웹 프로그래밍","김석훈",22000)
b5 = Book("생활코딩! HTML+CSS+자바스크립트","이고잉",27000)

b1.getBookInfo()
b2.getBookInfo()
b3.getBookInfo()
b4.getBookInfo()
b5.getBookInfo()