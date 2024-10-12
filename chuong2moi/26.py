import requests
import xml.dom.minidom
import csv

# B1 Tải RSS feed từ URL và lưu vào tệp XML
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
get_url = requests.get(url)

with open('rssfeed.xml', 'wb') as file:
    file.write(get_url.content)

# B2 phan tich  XML and save vào điển 
dom = xml.dom.minidom.parse('rssfeed.xml')
items = dom.getElementsByTagName('item')

news_list = []
for item in items:
    title = item.getElementsByTagName('title')[0].firstChild.nodeValue
    link = item.getElementsByTagName('link')[0].firstChild.nodeValue
    description = item.getElementsByTagName('description')[0].firstChild.nodeValue
    news_list.append({'title': title, 'link': link, 'description': description})

# B3 save các tin tức vào tệp CSV---------------------------------------------------
with open('news.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'link', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for news in news_list:
        writer.writerow(news)

print("Đã hoàn thành lưu RSS feed vào tệp news.csv")