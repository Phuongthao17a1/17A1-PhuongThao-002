class Stack:
    def __init__(self, capacity):
        
        self.capacity = capacity  
        self.stack = []  

    def push(self, item):
        
        if self.isFull():
            raise Exception("Ngăn xếp đã đầy, không thể thêm phần tử.")
        self.stack.append(item)

    def pop(self):
        
        if self.isEmpty():
            raise Exception("Ngăn xếp trống, không thể lấy phần tử.")
        return self.stack.pop()

    def isEmpty(self):
        
        return len(self.stack) == 0

    def isFull(self):
        
        return len(self.stack) >= self.capacity

    def count(self):
        
        return len(self.stack)

    def print_stack(self):
        
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung của ngăn xếp:")
            for item in reversed(self.stack):  
                print(item)


if __name__ == "__main__":
    stack = Stack(5)  

    
    try:
        stack.push(10)
        stack.push(20)
        stack.push(30)
        
        
        stack.print_stack()
        
        print(f"Số phần tử trong ngăn xếp: {stack.count()}")

        
        popped_item = stack.pop()
        print(f"Lấy phần tử ra: {popped_item}")

        
        stack.print_stack()
        print(f"Số phần tử trong ngăn xếp: {stack.count()}")

    except Exception as e:
        print(e)
