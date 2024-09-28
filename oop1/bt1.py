class HinhChuNhat:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def cv(self):
        CV =  (self.height+self.width)*2
        return CV
    def dienTich(self):
        DT = self.height*self.width
        return DT
    def info(self):
        print('chiều dài của hình chữ nhật là ',self.height)
        print('chiều rộng của hình chữ nhật là',self.width)
        print('Diện tích hình chữ nhật là:', self.dienTich())
        print('Chu vi hình chữ nhật là:',self.cv())
    

obj1 = HinhChuNhat(20,30)
obj1.info()
# obj1.dienTich()
# obj1.cv()