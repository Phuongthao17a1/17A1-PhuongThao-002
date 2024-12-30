import sqlite3

def create_database():
    connection = sqlite3.connect("C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/mydatabase.db")
    cursor = connection.cursor()
    #tạo một con trỏ (cursor) từ kết nối đó để thực hiện các truy vấn SQL.
    cursor.execute('''CREATE TABLE IF NOT EXISTS example_table
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    connection.close()

def connect_and_print_version():
    connection = sqlite3.connect("C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/mydatabase.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT SQLITE_VERSION()")#truy vấn SQL để lấy phiên bản của SQLite.
    version = cursor.fetchone()[0]
    print(f"Phiên bản SQLite: {version}")
    connection.close()

create_database()

connect_and_print_version()
