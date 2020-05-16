# class Rectangle:
# #     count = 0  # 클래스 변수
# #
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #         Rectangle.count += 1
# #
# #     # 인스턴스 메서드
# #     def calcArea(self):
# #         area = self.width * self.height
# #         return area
# #
# #     # 정적 메서드
# #     @staticmethod
# #     def isSquare(rectWidth, rectHeight):
# #         return rectWidth == rectHeight
# #
# #         # 클래스 메서드
# #
# #     @classmethod
# #     def printCount(cls):
# #         print(cls.count)
# #
# #     # 테스트
# #
# #
# # square = Rectangle.isSquare(5, 5)
# # print(square)  # True
# #
# # rect1 = Rectangle(5, 5)
# # rect2 = Rectangle(2, 5)
# # rect1.printCount()  # 2
# #
# # # 인스턴스 생성
# # r = Rectangle(2, 3)
# #
# # # 메서드 호출
# # area = r.calcArea()
# # print("area = ", area)
# #
# # # 인스턴스 변수 엑세스
# # r.width = 10
# # print("width = ", r.width)
# #
# # # 클래스 변수 엑세스
# # print(Rectangle.count)
# # print(r.count)

class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("bark")
class Duck(Animal):
    def speak(self):
        print("quack")

dog = Dog("doggy") # 부모클래스의 생성자
n = dog.name # 부모클래스의 인스턴스변수
dog.move()   # 부모클래스의 메서드
dog.speak()  # 파생클래스의 멤버