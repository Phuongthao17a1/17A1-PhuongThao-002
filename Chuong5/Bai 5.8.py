import sqlite3

def xoa_hang(database_file, ten_bang, dieu_kien):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {ten_bang} WHERE {dieu_kien}")
    conn.commit()

    print(f"Xóa hàng thành công từ bảng {ten_bang} dựa trên điều kiện: {dieu_kien}")
    conn.close()
database_path = 'C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/nhan_su.db'
bang_delete = 'nhan_vien'
dieu_kien_xoa = 'ID = 1'
xoa_hang(database_path, bang_delete, dieu_kien_xoa)
