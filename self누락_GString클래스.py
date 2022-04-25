#전역변수 초기화
str = "Not Class Member"
#클래스 정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 수정
        print(self.str)

#인스턴스
g = GString()
g.set("First Message")
g.print()
