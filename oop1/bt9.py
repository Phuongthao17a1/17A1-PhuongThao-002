class Polygon:
    def __init__(self):
        
        pass

    def perimeter(self):
        
        raise NotImplementedError("Phương thức này chưa được định nghĩa.")

    def area(self):
        
        raise NotImplementedError("Phương thức này chưa được định nghĩa.")

class Parallelogram(Polygon):
    def __init__(self, base, height):
        
        self.base = base
        self.height = height

    def perimeter(self):
        
        return 2 * (self.base + self.height)

    def area(self):
        
        return self.base * self.height

class Rectangle(Parallelogram):
    def __init__(self, length, width):
        
        super().__init__(length, width)  
        self.length = length
        self.width = width

    def perimeter(self):
        
        return 2 * (self.length + self.width)

    def area(self):
        
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        
        super().__init__(side, side)  


if __name__ == "__main__":
    
    base = float(input("Nhập cơ sở của hình bình hành: "))
    height = float(input("Nhập chiều cao của hình bình hành: "))
    parallelogram = Parallelogram(base, height)
    print(f"Chu vi hình bình hành: {parallelogram.perimeter()}")
    print(f"Diện tích hình bình hành: {parallelogram.area()}")

    
    length = float(input("Nhập chiều dài của hình chữ nhật: "))
    width = float(input("Nhập chiều rộng của hình chữ nhật: "))
    rectangle = Rectangle(length, width)
    print(f"Chu vi hình chữ nhật: {rectangle.perimeter()}")
    print(f"Diện tích hình chữ nhật: {rectangle.area()}")

    
    side = float(input("Nhập độ dài cạnh của hình vuông: "))
    square = Square(side)
    print(f"Chu vi hình vuông: {square.perimeter()}")
    print(f"Diện tích hình vuông: {square.area()}")
