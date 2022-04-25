# class1.py
#1) 클래스를 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "이정은"
    def print(self):
        print("내 이름은 {0}".format(self.name))

#2) 인스턴스 생성
p1 = Person()

#3) 메서드 호출
p1.print()

p2 = Person()
#멤버 변수
p2.name = "이정남"
#멤버 메서드 호출
p2.print()

#런타임(실행중) - 디자인타임(코딩중)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

