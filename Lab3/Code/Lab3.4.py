import pandas as pd
from Lab33 import stocks
#Đọc file companies.csv vào DataFrame companies:
companies = pd.read_csv('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab3/Data//companies.csv')
#Hiển thị 5 dòng đầu tiên của DataFrame companies:
print(companies.head())
# Kết hợp DataFrame stocks và companies dựa trên cột chung là symbol:
#Lỗi KeyError: 'symbol' xuất hiện vì DataFrame companies không chứa cột 'symbol' để kết hợp dữ liệu.
ket_hop = pd.merge(stocks, companies, on='symbol')
#Tính giá đóng cửa (close) trung bình cho mỗi công ty:
trung_binh_gia_dong_cua = ket_hop.groupby('company_name')['close'].mean()
# Hiển thị kết quả cho 5 công ty đầu tiên:
print(trung_binh_gia_dong_cua.head())
