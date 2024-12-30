import sqlite3

def bang_danh_sach(database_file):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = cursor.fetchall()
    if tables:
        print("Các bảng trong cơ sở dữ liệu:")
        for table in tables:
            print(table[0])
    else:
        print("Không có bảng nào trong cơ sở dữ liệu.")

    conn.close()

database_path = 'C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/my_database.db'
bang_danh_sach(database_path)
