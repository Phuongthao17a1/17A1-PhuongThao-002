import numpy as np

#Đọc dữ liệu từ tập tin efficiency.txt và shifts.txt vào 2 list là efficiency và shifts:
with open('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab2/Data//efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

with open('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab2/Data//shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

#Tạo numpy array np_shifts từ list shifts và kiểm tra kiểu dữ liệu:
np_shifts = np.array(shifts)
print("Kiểu dữ liệu của np_shifts:", type(np_shifts))
#Tạo numpy array np_efficiency từ list efficiency và kiểm tra kiểu dữ liệu:
np_efficiency = np.array(efficiency)
print("Kiểu dữ liệu của np_efficiency:", type(np_efficiency))
#Tính hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning':
trung_binh_hieu_qua_buoi_sang = np_efficiency[np_shifts == 'Morning'].mean()
print("Hiệu suất sản xuất trung bình của nhân viên làm ca Morning:", trung_binh_hieu_qua_buoi_sang)
# Tạo mảng dữ liệu có cấu trúc (Structure Array) workers:
workers = np.array(list(zip(shifts, efficiency)), dtype=[('shift', 'U10'), ('efficiency', float)])
#Sắp xếp mảng workers theo efficiency và xác định ca làm việc có hiệu suất cao nhất và thấp nhất:
sorted_workers = np.sort(workers, order='efficiency')
highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']

print("Ca làm việc có hiệu suất cao nhất là:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất là:", lowest_efficiency_shift)