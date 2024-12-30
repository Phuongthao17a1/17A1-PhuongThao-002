import sqlite3

# Kết nối tới cơ sở dữ liệu product.db
conn = sqlite3.connect('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab4/product.db')
cursor = conn.cursor()

# Hàm hiển thị menu
def hien_thi_menu():
    print("=== MENU ===")
    print("1. Hiển Thị Danh Sách Sản Phẩm")
    print("2. Thêm Sản Phẩm Mới")
    print("3. Tìm Kiếm Sản Phẩm Theo Tên")
    print("4. Cập Nhật Thông Tin Sản Phẩm")
    print("5. Xóa Sản Phẩm")
    print("6. Thoát")

# Hàm xử lý chức năng Hiển Thị Danh Sách Sản Phẩm
def hien_thi_product():
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    for product in products:
        print(product)

# Hàm xử lý chức năng Thêm Sản Phẩm Mới
def add_product():
    Name= input("Nhập tên sản phẩm:")
    Price= float(input("Nhập giá sản phẩm:"))
    Amount= int(input("Nhập só lượng sản phẩm:"))
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (Name, Price, Amount))
    conn.commit()
    print("Đã thêm sản phẩm mới vào CSDL.")
    
# Hàm xử lý chức năng Tìm Kiếm Sản Phẩm Theo Tên
def tim_kiem_product():
    name = input("Nhập tên sản phẩm cần tìm: ")
    cursor.execute("SELECT * FROM product WHERE name=?", (name,))
    product = cursor.fetchone()
    if product:
        print(product)
    else:
        print("Không tìm thấy sản phẩm có tên này.")

# Hàm xử lý chức năng Cập Nhật Thông Tin Sản Phẩm
def update_product():
    id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    price = float(input("Nhập giá mới cho sản phẩm: "))
    amount = int(input("Nhập số lượng mới cho sản phẩm: "))
    cursor.execute("UPDATE product SET price=?, amount=? WHERE id=?", (price, amount, id))
    conn.commit()
    print("Đã cập nhật thông tin sản phẩm.")

# Hàm xử lý chức năng Xóa Sản Phẩm
def delete_product():
    id = int(input("Nhập ID sản phẩm cần xóa: "))
    cursor.execute("DELETE FROM product WHERE id=?", (id,))
    conn.commit()
    print("Đã xóa sản phẩm khỏi CSDL.")

# Chương trình main
while True:
    hien_thi_menu()
    choice = input("Chọn chức năng (1-6): ")

    if choice == '1':
        hien_thi_product()
    elif choice == '2':
        add_product()
    elif choice == '3':
        tim_kiem_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    elif choice == '6':
        print("Kết thúc chương trình. Hẹn gặp lại!")
        break
    else:
        print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.")

# Đóng kết nối tới cơ sở dữ liệu
conn.close()