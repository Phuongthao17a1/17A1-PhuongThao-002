class PS:
    def __init__(self):
        self.ts=0
        self.ms=0
    def inp(self):
        self.ts=float(input('nhập tử số : '))
        self.ms=float(input('nhập mẫu số : '))
    def check(self):
        if self.ms==0:
            print('ko hợp lệ')
        else:
            print('phân số bạn vừa nhập là : ',self.ts,'/',self.ms)


ts=PS()
ts.inp()
ts.check()