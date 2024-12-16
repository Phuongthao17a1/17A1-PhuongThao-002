import numpy as np
#2.1.1
# Mảng NumPy mô phỏng dữ liệu nhiệt độ hàng ngày trong một tháng
du_lieu_nhiet_do = np.array([25.12, 28.45, 30.70, 32.15, 26.80, 29.33, 31.90, 27.65, 33.25, 29.80,
                             24.90, 26.55, 28.10, 31.40, 32.80, 29.20, 30.60, 27.75, 26.30, 28.90,
                             31.70, 29.10, 27.40, 30.30, 32.60, 28.50, 26.20, 30.00, 31.80, 29.60])

du_lieu_nhiet_do = np.random.uniform(low=20.0, high=35.0, size=30)  # Dữ liệu nhiệt độ từ 20.0 đến 35.0

# Làm tròn dữ liệu đến 2 chữ số sau dấu phẩy
du_lieu_nhiet_do_rounded = np.round(du_lieu_nhiet_do, 2)

# Tính nhiệt độ trung bình trong tháng
nhiet_do_trung_binh = np.mean(du_lieu_nhiet_do_rounded)

print("Dữ liệu nhiệt độ hàng ngày trong tháng:")
print(du_lieu_nhiet_do_rounded)
print("Nhiệt độ trung bình trong tháng là: {:.2f}".format(nhiet_do_trung_binh))

#2.1.2
# Xác định ngày có nhiệt độ cao nhất và thấp nhất
ngay_co_nhiet_do_max = np.argmax(du_lieu_nhiet_do) + 1  # +1 để chuyển từ vị trí (index) sang ngày
ngay_co_nhiet_do_min = np.argmin(du_lieu_nhiet_do) + 1

# Thống kê sự chênh lệch nhiệt độ giữa các ngày và tìm ngày có sự biến đổi nhiệt độ cao nhất
chenh_lech_nhiet_do = np.diff(du_lieu_nhiet_do)
chenh_lech_nhiet_do_max = np.argmax(chenh_lech_nhiet_do) + 1

print("Ngày có nhiệt độ cao nhất trong tháng là ngày thứ:", ngay_co_nhiet_do_max)
print("Ngày có nhiệt độ thấp nhất trong tháng là ngày thứ:", ngay_co_nhiet_do_min)
print("Ngày có sự biến đổi nhiệt độ cao nhất trong tháng là ngày thứ:", chenh_lech_nhiet_do_max)
#2.1.3
# Dùng Fancy Indexing để thực hiện các yêu cầu
# Ngày có nhiệt độ cao hơn 20 độ C
above_20 = du_lieu_nhiet_do[du_lieu_nhiet_do > 20]
print("Các ngày có nhiệt độ cao hơn 20 độ C:")
print(above_20)

# Nhiệt độ của ngày 5, 10, 15, 20, và 25
ngay_chi_dinh = [4, 9, 14, 19, 24]
nhiet_do_ngay_da_chon = du_lieu_nhiet_do[ngay_chi_dinh]
print("\nNhiệt độ của các ngày thứ 5, 10, 15, 20, và 25:")
print(nhiet_do_ngay_da_chon)

# Nhiệt độ của các ngày có nhiệt độ trên trung bình
nhiet_do_trung_binh = np.mean(du_lieu_nhiet_do)
tren_nhiet_do_trung_binh = du_lieu_nhiet_do[du_lieu_nhiet_do > nhiet_do_trung_binh]
print("\nNhiệt độ của các ngày có nhiệt độ trên trung bình:")
print(tren_nhiet_do_trung_binh)

# Nhiệt độ của các ngày chẵn/lẻ trong tháng
nhiet_do_ngay_chan = du_lieu_nhiet_do[::2]  # Các ngày chẵn
nhiet_do_ngay_le = du_lieu_nhiet_do[1::2]  # Các ngày lẻ
print("\nNhiệt độ của các ngày chẵn trong tháng:")
print(nhiet_do_ngay_chan)
print("\nNhiệt độ của các ngày lẻ trong tháng:")
print(nhiet_do_ngay_le)