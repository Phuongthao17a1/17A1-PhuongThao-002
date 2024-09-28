class Stack:
    def __init__(self, capacity=10):
        
        self.capacity = capacity  
        self.stack = []  
        self.top = -1  

    def isEmpty(self):
        
        return self.top == -1

    def isFull(self):
        
        return self.top >= self.capacity - 1

    def push(self, item):
        
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử:", item)
            return
        self.stack.append(item)  
        self.top += 1  

    def pop(self):
        
        if self.isEmpty():
            print("Ngăn xếp đã trống, không thể lấy phần tử.")
            return None
        item = self.stack.pop()  
        self.top -= 1  
        return item

    def peek(self):
        
        if self.isEmpty():
            print("Ngăn xếp đã trống, không có phần tử để xem.")
            return None
        return self.stack[self.top]

    def display(self):
        
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)



if __name__ == "__main__":
    stack = Stack(5)  

    
    stack.push(1.1)
    stack.push(2.2)
    stack.push(3.3)
    stack.push(4.4)
    stack.push(5.5)
    stack.push(6.6)  

    
    stack.display()

    
    print("Lấy ra phần tử:", stack.pop())
    print("Lấy ra phần tử:", stack.pop())

    
    stack.display()

    
    print("Phần tử trên cùng là:", stack.peek())

    
    print("Ngăn xếp có trống không?", stack.isEmpty())
    print("Ngăn xếp có đầy không?", stack.isFull())
