import requests

# URL  để lấy thông tin các bài post với postId=1
url = 'https://jsonplaceholder.typicode.com/comments?postId=1'

# get url
response = requests.get(url)

# chekc
if response.status_code == 200:
    posts = response.json()
    
    # Hiển thị thông tin 3 bài post đầu tiên
    for post in posts[:3]:  # Giới hạn hiển thị 3 bài
        print(f"Post ID: {post['postId']}, ID: {post['id']}")
        print(f"Name: {post['name']}")
        print(f"Email: {post['email']}")
        print(f"Body: {post['body']}\n")
else:
    print("Không thể lấy thông tin từ API.")