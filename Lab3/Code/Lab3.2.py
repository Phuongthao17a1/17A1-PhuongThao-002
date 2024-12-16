import pandas as pd
#Kiểm tra xem trong stocks1.csv có dữ liệu Null nào không:
stocks1 = pd.read_csv('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab3/Data//stocks1.csv')
null_values = stocks1.isnull().sum()
print("Số lượng dữ liệu Null trong stocks1.csv:")
print(null_values)
# Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high':
trung_binh_cot_high = stocks1['high'].mean()
stocks1['high'].fillna(trung_binh_cot_high, inplace=True)
#Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low':
trung_binh_cot_low = stocks1['low'].mean()
stocks1['low'].fillna(trung_binh_cot_low, inplace=True)
#Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null:
print("Thông tin tổng quan sau khi thay thế dữ liệu Null:")
stocks1.info()