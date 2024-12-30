import sqlite3


def update_cot(database_file, ten_bang, cot_update, new_age):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute(f"UPDATE {ten_bang} SET {cot_update} = ?", (new_age,))

    conn.commit()

    print(f"Cập nhật thành công. Tất cả giá trị trong cột {cot_update} đã được đặt thành {new_age}.")

    conn.close()

database_path = 'C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/nhan_su.db'

bang_update = 'nhan_vien'
cot_update = 'Age'
new_age = 21

update_cot(database_path, bang_update, cot_update, new_age)
