import json

#Đối tượng Python mẫu (từ điển)
doi_tuong_python = {
    "ten": "Phan Thảo",
    "tuoi": 19,
    "dia_chi": "123 Đường XYZ, Thành phố HN"
}

# Chuyeern đổi đối tượng Python thành chuỗi JSON với cú pháp yêu cầu
chuoi_json = json.dumps(doi_tuong_python, ensure_ascii=True, check_circular=True, allow_nan=True)

#In ra chuỗi JSON đã tạo
print(f"Chuỗi JSON: {chuoi_json}\n")

#In ra tất cả các giá trị trong đối tượng Python
print("Các giá trị trong đối tượng Python:")
for key, value in doi_tuong_python.items():
    print(f"{key}: {value}")