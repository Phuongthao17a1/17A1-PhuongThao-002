import pandas as pd
# Đọc file stocks2.csv vào DataFrame stocks2:
stocks2 = pd.read_csv('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab3/Data//stocks2.csv')
#Gộp stocks1.csv và stocks2.csv thành DataFrame mới tên là stocks:
stocks1 = pd.read_csv('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab3/Data//stocks1.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
#Tính giá trung bình (open, high, low, close) cho mỗi ngày:
stocks['average_price'] = (stocks['open'] + stocks['high'] + stocks['low'] + stocks['close']) / 4
#Hiển thị 5 dòng đầu tiên của kết quả:
print(stocks.head())