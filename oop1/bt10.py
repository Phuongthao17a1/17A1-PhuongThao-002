import math

class Point:
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def display(self):
        
        return f"Điểm có tọa độ: ({self.x}, {self.y})"

class Ellipse(Point):
    def __init__(self, x, y, a, b):
        
        super().__init__(x, y)  
        self.a = a  
        self.b = b  

    def area(self):
        
        return math.pi * self.a * self.b

    def display(self):
        
        return f"Elip có tâm tại {super().display()}, bán trục lớn: {self.a}, bán trục nhỏ: {self.b}, diện tích: {self.area()}"

class Circle(Ellipse):
    def __init__(self, x, y, radius):
        
        super().__init__(x, y, radius, radius)  

    def area(self):
        
        return math.pi * self.a**2  

    def display(self):
        
        return f"Đường tròn có tâm tại {super().display()}, diện tích: {self.area()}"


if __name__ == "__main__":
    
    x = float(input("Nhập hoành độ của tâm elip: "))
    y = float(input("Nhập tung độ của tâm elip: "))
    a = float(input("Nhập bán trục lớn của elip: "))
    b = float(input("Nhập bán trục nhỏ của elip: "))
    ellipse = Ellipse(x, y, a, b)
    print(ellipse.display())

    
    x = float(input("\nNhập hoành độ của tâm đường tròn: "))
    y = float(input("Nhập tung độ của tâm đường tròn: "))
    radius = float(input("Nhập bán kính của đường tròn: "))
    circle = Circle(x, y, radius)
    print(circle.display())
