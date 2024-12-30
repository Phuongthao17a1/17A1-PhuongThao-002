import sqlite3

def create_database():
    connection = sqlite3.connect("C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/my_database.db")
    cursor = connection.cursor()
    #tạo một con trỏ (cursor) từ kết nối đó để thực hiện các truy vấn SQL.
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    connection.close()

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

def chen_va_hien_thi(database_file, table_name):
    conn = sqlite3.connect(database_file)

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", ('Anh', 25))
    cursor.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", ('Vy', 30))

    conn.commit()

    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()
    if rows:
        print(f"\nDữ liệu từ bảng {table_name}:")
        for row in rows:
            print(row)
    else:
        print(f"\nKhông có dữ liệu trong bảng {table_name}.")

    conn.close()

database_path = 'C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/my_database.db'

table_name = 'students'

bang_danh_sach(database_path)

chen_va_hien_thi(database_path, table_name)
