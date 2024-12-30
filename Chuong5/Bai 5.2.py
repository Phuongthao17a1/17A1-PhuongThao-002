import sqlite3
conn = sqlite3.connect(':memory:') #tạo một kết nối tới một cơ sở dữ liệu SQLite tạm thời trong bộ nhớ

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS nhan_vien (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT
    )
''')

cursor.execute("INSERT INTO nhan_vien (name, position) VALUES (?, ?)", ('ANH', 'Quản lý'))
cursor.execute("INSERT INTO nhan_vien (name, position) VALUES (?, ?)", ('Vy', 'Ke toan'))
cursor.execute("INSERT INTO nhan_vien (name, position) VALUES (?, ?)", ('Thu', 'Thu ngân'))

conn.commit()

cursor.execute("SELECT * FROM nhan_vien")
rows = cursor.fetchall()

print("Dữ liệu trong bảng nhan_vien:")
for row in rows:
    print(row)
conn.close()
