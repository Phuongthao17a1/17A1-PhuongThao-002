import numpy as np
import csv

# 1. Đọc dữ liệu từ file CSV
file_path = 'C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab2/Data/diem_hoc_phan.csv'
data = []

with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Bỏ qua header
    for row in reader:
        data.append([row[0], row[1]] + list(map(float, row[2:])))

# Chuyển dữ liệu thành mảng NumPy
du_lieu_mang = np.array(data, dtype=object)

# 2. Quy đổi điểm số sang điểm chữ
def quy_doi_diem(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem < 8.5:
        return 'B+'
    elif 7.0 <= diem < 8.0:
        return 'B'
    elif 6.5 <= diem < 7.0:
        return 'C+'
    elif 5.5 <= diem < 6.5:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng quy đổi điểm chữ
diem_chu = np.vectorize(quy_doi_diem)
mang_diem_chu = diem_chu(du_lieu_mang[:, 2:].astype(float))

# 3. Chia tách dữ liệu theo học phần
hp1 = du_lieu_mang[:, 2].astype(float)
hp2 = du_lieu_mang[:, 3].astype(float)
hp3 = du_lieu_mang[:, 4].astype(float)

# 4. Phân tích dữ liệu từng học phần
def phan_tich(subject_diems, subject_name):
    total = np.sum(subject_diems)
    average = np.mean(subject_diems)
    std_dev = np.std(subject_diems)
    print(f"Học phần {subject_name}:\n  Tổng điểm: {total}\n  Điểm trung bình: {average:.2f}\n  Độ lệch chuẩn: {std_dev:.2f}\n")

print("Phân tích từng học phần:\n")
phan_tich(hp1, "HP1")
phan_tich(hp2, "HP2")
phan_tich(hp3, "HP3")

# 5. Phân tích điểm tổng hợp
def phan_tich(grades):
    unique, counts = np.unique(grades, return_counts=True)
    phan_phoi_lop = dict(zip(unique, counts))
    print("Phân bố điểm chữ:")
    for grade, count in phan_phoi_lop.items():
        print(f"  {grade}: {count} sinh viên")

all_grades = mang_diem_chu.flatten()
print("Phân tích điểm tổng hợp:\n")
phan_tich(all_grades)

# Fancy Indexing - Lấy điểm các sinh viên theo một số điều kiện
print("\nĐiểm các sinh viên có điểm HP1 trên trung bình:")
print(du_lieu_mang[hp1 > np.mean(hp1)])

print("\nĐiểm các sinh viên có điểm HP2 dưới 5:")
print(du_lieu_mang[hp2 < 5])
