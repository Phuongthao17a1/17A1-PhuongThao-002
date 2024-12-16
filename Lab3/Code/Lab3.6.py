import pandas as pd
from Lab33 import stocks
# Tạo Pivot Table từ DataFrame stocks:
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')
#Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol):
pivot_table['total_volume'] = stocks.groupby('symbol')['volume'].sum()
#Sắp xếp Pivot Table dựa trên tổng volume giao dịch từ cao xuống thấp:
sorted_pivot_table = pivot_table.sort_values(by='total_volume', ascending=False)
#Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất:
top_5_symbols = sorted_pivot_table['total_volume'].head(5)
print(top_5_symbols)