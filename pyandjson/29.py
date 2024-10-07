import json

#Tạo một từ điển Python đã sắp xếp theo khóa
tu_dien = {
    "d": 4,
    "a": 1,
    "c": 3,
    "b": 2
}

# Chuyeern đổi từ điển Python sang chuỗi JSON với thụt lề 4
chuoi_json = json.dumps(tu_dien, indent=4, sort_keys=True)

#In ra các thành viên của đối tượng với mức thụt lề 4
print(chuoi_json)