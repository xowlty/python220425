# Person.py
class Person:
    def __init__(self): #__init__ 초기화 self 내가 초기화 시킨 변수, 나라는 것을 지정하려는 변수
        self.name = "default name" #나 지정
    def print(self):
        print("My name is {0}".format(self.name)) # {0}: 프린트함수가 포맷 데이터 인수를 {0}자리로 치환함

p1 = Person() #p1인스턴스 객체변수는 퍼슨 함수로 매핑됨
p1.print()

