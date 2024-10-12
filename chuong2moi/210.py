import json

#1 read dât form json
with open('C:/laptrinhaaa/python học trên lớp/Python Kỳ 3/Btap/2.xml and json/nhanvien.json', 'r') as f:
    data = json.load(f)

# 2sumsố nhân viên
tong_nhan_vien = sum([donvi['so_nhan_vien'] for donvi in data])

# 3 print 
for donvi in data:
    ten_don_vi = donvi['ten_don_vi']
    so_nhan_vien = donvi['so_nhan_vien']
    ty_le = (so_nhan_vien / tong_nhan_vien) * 100
    print(f"Tên đơn vị: {ten_don_vi} - Số nhân viên: {so_nhan_vien} - Tỷ lệ: {ty_le:.2f}%")