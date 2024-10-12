import json
from datetime import datetime

# reg name file và format giao dịch
filename = 'giaodich.json'
transaction = {
    'thoi_gian': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'so_tien': input("Nhập số tiền: "),
}

# read data có từ tệp if yes
try:
    with open(filename, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

# add giao dịch vào list
data.append(transaction)

# w lại vào tệp jsson
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

print("Giao dịch đã được lưu thành công.")