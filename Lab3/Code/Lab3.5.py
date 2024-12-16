import pandas as pd
from Lab33 import stocks
#Tạo MultiIndex cho DataFrame stocks.csv bằng cách sử dụng cột date và symbol làm chỉ mục:
stocks.set_index(['date', 'symbol'], inplace=True)
# Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, cho mỗi mã chứng khoán:
gia_trung_binh = stocks.groupby(level=['date', 'symbol']).mean()
# Sắp xếp dữ liệu theo ngày và mã chứng khoán:
sap_xep = gia_trung_binh.sort_index(level=['date', 'symbol'])
# Hiển thị kết quả cho 5 ngày đầu tiên:
print(sap_xep.head(5))