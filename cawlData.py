import pandas as pd
import mysql.connector
import os
import re
from bs4 import BeautifulSoup

# Kết nối đến cơ sở dữ liệu MySQL
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="voithan",
    database="bot"
)

# Thực hiện truy vấn SQL và đọc kết quả vào DataFrame
query = "SELECT id, url, title, description, content FROM article"
df = pd.read_sql(query, connection)

# Đóng kết nối MySQL
connection.close()
# print(df)
# Xuất DataFrame ra file CSV

# df.to_csv("/mnt/d/BookingCare/systemQA/fileBC.csv", index=False)

# Đảm bảo thư mục xuất file tồn tại
output_directory = "/mnt/d/BookingCare/systemQA/fileBC_html"
os.makedirs(output_directory, exist_ok=True)

# i = 1

# Duyệt qua từng dòng của DataFrame và ghi vào file .txt
for index, row in df.iterrows():
    id_value = row['id']

    title_value = re.sub(r'[!@#$%^&*/\\]', '', row['title']) if pd.notna(row['title']) else ""
    description_value = row['description'] if pd.notna(row['description']) else ""
    content_value = row['content'] if pd.notna(row['content']) else ""

    # Sử dụng BeautifulSoup để loại bỏ các thẻ HTML
    soup = BeautifulSoup(content_value, 'html.parser')

    # Chuyển đổi HTML thành văn bản thuần túy hoặc không, cmt để dùng
    # plain_text = soup.get_text(separator='\n')
    plain_text = content_value

    print(id_value, title_value, description_value, plain_text)
    # Tạo tên file từ id
    filename = os.path.join(output_directory, f"{id_value}_{title_value[:100]}.txt")

    # Ghi dữ liệu vào file .txt
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Description: {description_value}\n")
        file.write(f"Content: {plain_text}\n")

    # if i == 10:
    #     break
    # else:
    #     i = i + 1

print("Xuất files thành công!")
