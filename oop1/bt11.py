import math

class Triangle:
    def __init__(self, a, b, c):
        """Khởi tạo lớp Tam giác với ba cạnh a, b, c."""
        self.a = a  # Cạnh a
        self.b = b  # Cạnh b
        self.c = c  # Cạnh c

    def perimeter(self):
        """Tính chu vi của tam giác."""
        return self.a + self.b + self.c

    def area(self):
        """Tính diện tích của tam giác bằng công thức Heron."""
        s = self.perimeter() / 2  # Bán chu vi
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def display(self):
        """Hiển thị thông tin về tam giác."""
        return f"Tam giác với các cạnh a = {self.a}, b = {self.b}, c = {self.c}, chu vi = {self.perimeter()}, diện tích = {self.area()}"

class RightTriangle(Triangle):
    def __init__(self, a, b):
        """Khởi tạo lớp Tam giác vuông với hai cạnh góc vuông a và b."""
        super().__init__(a, b, math.sqrt(a**2 + b**2))  # Cạnh c được tính theo định lý Pythagoras

    def display(self):
        """Hiển thị thông tin về tam giác vuông."""
        return f"Tam giác vuông với hai cạnh góc vuông a = {self.a}, b = {self.b}, c = {self.c:.2f}, chu vi = {self.perimeter()}, diện tích = {self.area()}"

class IsoscelesTriangle(Triangle):
    def __init__(self, base, side):
        """Khởi tạo lớp Tam giác cân với đáy base và hai cạnh bên side."""
        super().__init__(base, side, side)

    def display(self):
        """Hiển thị thông tin về tam giác cân."""
        return f"Tam giác cân với đáy = {self.a}, hai cạnh bên = {self.b}, chu vi = {self.perimeter()}, diện tích = {self.area()}"

class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        """Khởi tạo lớp Tam giác đều với cạnh bên là side."""
        super().__init__(side, side)

    def display(self):
        """Hiển thị thông tin về tam giác đều."""
        return f"Tam giác đều với cạnh = {self.a}, chu vi = {self.perimeter()}, diện tích = {self.area()}"

# Ví dụ sử dụng
if __name__ == "__main__":
    # Nhập thông tin cho Tam giác
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    triangle = Triangle(a, b, c)
    print(triangle.display())

    # Nhập thông tin cho Tam giác vuông
    a = float(input("\nNhập cạnh góc vuông a của tam giác vuông: "))
    b = float(input("Nhập cạnh góc vuông b của tam giác vuông: "))
    right_triangle = RightTriangle(a, b)
    print(right_triangle.display())

    # Nhập thông tin cho Tam giác cân
    base = float(input("\nNhập đáy của tam giác cân: "))
    side = float(input("Nhập cạnh bên của tam giác cân: "))
    isosceles_triangle = IsoscelesTriangle(base, side)
    print(isosceles_triangle.display())

    # Nhập thông tin cho Tam giác đều
    side = float(input("\nNhập cạnh của tam giác đều: "))
    equilateral_triangle = EquilateralTriangle(side)
    print(equilateral_triangle.display())
