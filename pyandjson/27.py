import json

#Dữ liệu JSON mẫu
json_data = '{ "ten": "Phan Thao","tuoi": 19, "dia_chi": "123 Đường XYZ, Thành phố HN" }'

#Chuyển đổi dữ liệu JSON thành đối tượng Python
doi_tuong = json.loads(json_data)

# In ra đối tượng Python đã chuyển đoi
print(doi_tuong)