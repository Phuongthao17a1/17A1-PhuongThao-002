class TS:
    def __init__(self):
        self.name= ''
        self.pointMath=0
        self.pointPhysics=0
        self.pointChemistry=0
    def inputInfo(self):
        self.name= input('nhập tên sinh viên : ')
        self.pointMath=float(input('nhập điểm Toán : '))
        self.pointPhysics=float(input('nhập điểm Lý : '))
        self.pointChemistry=float(input('nhập điểm Hóa : '))
    def outInfo(self):
        print('tên của thí sinh là :',self.name)
        print('điểm Toán của thí sinh là : ',self.pointMath)
        print('điểm Lý của thí sinh là : ',self.pointPhysics)
        print('điểm Hóa của thí sinh là : ',self.pointChemistry)
    def sumPoint(self):
        return self.pointMath + self.pointPhysics + self.pointChemistry    
class manageTS:
    def __init__(self):
        self.listTs=[]
        self.listTrung_Tuyen=[]

    def inputListTS(self):
        listTSCount = int(input('Nhấp số lượng học sinh : '))
        for i  in range(listTSCount):
            print('nhập info thí sinh thứ ',i+1)
            thiSinh=TS()
            thiSinh.inputInfo()
            self.listTs.append(thiSinh)
    def listTrungTuyen(self):
        for i    in self.listTs:
            if i.sumPoint()>=20:
                self.listTrung_Tuyen.append(i)
    def sortDanhSachTrungTuyen(self):
        
        self.listTrung_Tuyen.sort(key=lambda ts: ts.sumPoint(), reverse=True)
    def printDanhSachTrungTuyen(self):
        print("\nDanh sách thí sinh trúng tuyển:")
        if len(self.listTrung_Tuyen) == 0:
            print("Không có thí sinh nào trúng tuyển.")
        else:
            for ts in self.listTrung_Tuyen:
                ts.outInfo()

ms=manageTS()
ms.inputListTS()
ms.listTrungTuyen()
ms.sortDanhSachTrungTuyen()
ms.printDanhSachTrungTuyen()