import pandas as pd
#Đọc file stocks1.csv vào DataFrame stocks1:
stocks1 = pd.read_csv('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab3/Data//stocks1.csv')
#Hiển thị 5 dòng đầu tiên của stocks1:
print(stocks1.head())
#Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1:
print(stocks1.dtypes)
#Xem thông tin tổng quan (info) của stocks1:
stocks1.info()