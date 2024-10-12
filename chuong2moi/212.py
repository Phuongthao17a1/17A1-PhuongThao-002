import requests

# URL 
url = 'https://jsonplaceholder.typicode.com/posts'

# Gửi yêu cầu đến API
response = requests.get(url)

# chekc state khi gọi api từ net
if response.status_code == 200:
    books = response.json()
    
    # Hiển thị list sách
    for book in books[:5]:  # Hiển thị 5 sách đầu tiên
        print(f"User ID: {book['userId']}, ID: {book['id']}, Title: {book['title']}")
        print(f"Body: {book['body']}\n")
else:
    print("Không thể lấy danh sách sách từ API.")