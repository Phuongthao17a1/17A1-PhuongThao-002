import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect('C:/Users/Thao Phan/Desktop/17A1DHKL_LAB_PHAN_THI_PHUONG_THAO/Lab6/products.db')
c = conn.cursor()

# Tạo bảng sản phẩm nếu chưa có
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

# Hàm để thêm sản phẩm
def add_product():
    name = product_name.get()
    price = product_price.get()
    
    if not name or not price:
        messagebox.showwarning("Input Error", "Hãy điền đủ các trường!!!")
        return
    
    c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
    conn.commit()
    #Xoá nội dung trong hai ô product_name và product_price
    product_name.delete(0, tk.END)
    product_price.delete(0, tk.END)
    #Tải lại danh sách sản phẩm từ cơ sở dữ liệu và cập nhật lên giao diện người dùng.
    load_products()

# Hàm để xóa sản phẩm
def delete_product():
    try:
        selected_product = listbox.curselection() #lấy ra chỉ mục của sản phẩm được chọn
        if not selected_product:
            messagebox.showwarning("Selection Error", "Hãy điền đủ vào các trường!!!")
            return
        product_id = listbox.get(selected_product[0]).split(' ')[0]
        c.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        load_products()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm để cập nhật sản phẩm
def update_product():
    try:
        selected_product = listbox.curselection()
        if not selected_product:
            messagebox.showwarning("Selection Error", "Hãy chọn một sản phẩm để update.")
            return
        
        product_id = listbox.get(selected_product[0]).split(' ')[0]
        new_name = product_name.get()
        new_price = product_price.get()
        
        if not new_name or not new_price:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        c.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (new_name, float(new_price), product_id))
        conn.commit()
        product_name.delete(0, tk.END)
        product_price.delete(0, tk.END)
        load_products()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm để tải danh sách sản phẩm từ cơ sở dữ liệu
def load_products():
    listbox.delete(0, tk.END) #làm sạch list box
    c.execute("SELECT * FROM products")
    for product in c.fetchall():
        listbox.insert(tk.END, f"{product[0]} {product[1]} - ${product[2]:.2f}") # thêm vào "listbox" với định dạng ID-Tên - Giá

# Cấu hình giao diện người dùng
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Labels và Entry widgets
nhan_ten = tk.Label(root, text="Tên sản phẩm:")
nhan_ten.pack()

product_name = tk.Entry(root)
product_name.pack()

nhan_gia = tk.Label(root, text="Giá sản phẩm:")
nhan_gia.pack()

product_price = tk.Entry(root)
product_price.pack()

# Listbox để hiển thị sản phẩm
listbox = tk.Listbox(root, height=10, width=50)
listbox.pack()

# Nút để thêm, xóa, cập nhật sản phẩm
nut_add = tk.Button(root, text="Add Product", command=add_product)
nut_add.pack()

nut_update = tk.Button(root, text="Update Product", command=update_product)
nut_update.pack()

nut_delete = tk.Button(root, text="Delete Product", command=delete_product)
nut_delete.pack()

# Tải danh sách sản phẩm ban đầu
load_products()

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()
