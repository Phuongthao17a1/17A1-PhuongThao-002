import sqlite3

conn = sqlite3.connect('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Chuong5/my_database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
conn.commit()
conn.close()
