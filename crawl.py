import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class DataCrawler(ABC):
    @abstractmethod
    def fetch(self, url: str):
        '''
        Hàm trả về file HTML khi có url

        :param url:
        :return:
        '''
        pass

    @abstractmethod
    def parse(self, html: str):
        '''
        Hàm dùng để phân tích mã HTML

        :param html:
        :return:
        '''
        pass

    @abstractmethod
    def run(self, keywords: list):
        '''
        Hàm chạy để load các trang web.
        Lưu các file dưới dạng JSON như bên dưới (Mỗi một keyword sẽ là một file JSON).
        Quy cách tên file như sau: "keyword_tentrangweb_đường-dẫn.txt"

        Mẫu file JSON:
                 {
                    "keyword": "từ khóa",
                    "documents": [
                        {
                            "url": "https://www.example.com",
                            "html": "<html><body><h1>Tiêu đề</h1><p>Đây là một đoạn văn mô phỏng.</p></body></html>",
                            "snippet": "Đây là một đoạn văn mô phỏng.",
                            "score": 0.95
                        },
                        {
                            "url": "https://www.example2.com",
                            "html": "<html><body><h1>Tiêu đề khác</h1><p>Đây là một đoạn văn mô phỏng khác.</p></body></html>",
                            "snippet": "Đây là một đoạn văn mô phỏng khác.",
                            "score": 0.85
                        }
                        // thêm các trang khác vào đây...
                    ]
                }


        :param keywords: Danh sách từ khóa
        :return:
        '''
        pass

# Ví dụ minh họa sử dụng, có thể thêm các thuộc tính hoặc phương thức cần thiết
# -----------------------------------------------------------------------------#
class MyDataCrawler(DataCrawler):
    def fetch(self, url: str):
        response = requests.get(url)
        return response.text

    def parse(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        return data

    def run(self, keywords: list):
        for keyword in keywords:
            html = self.fetch(url)
            data = self.parse(html)
            # Lưu file JSON dưới dạng như sau
