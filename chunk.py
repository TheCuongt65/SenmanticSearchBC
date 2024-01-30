from abc import ABC, abstractmethod
import json
import os
class TextChunker(ABC):
    @abstractmethod
    def chunk_text(self, text: str, chunk_size: int) -> list:
        """
        Phương thức này chia mỗi chuỗi văn bản text thành các phần nhỏ

        :param text: Đầu vào là một chuỗi văn bản cần được chia nhỏ
        :param chunk_size: Kích thước của mỗi phần nhỏ
        :return: Một danh sách các phần nhỏ của văn bản
        """
        pass

    @abstractmethod
    def run(self, path: str):
        """
        Phương thức này đọc các file JSON từ thư mục Data.
        Chia documents thành chunks.

        Lưu lại hai thứ:
            * Lưu tất cả chunk thành các File .txt để dùng cho Embedding và lưu vào DataBase sau
            * Lưu các file JSON như mẫu dưới đây để dùng cho Evaluate.

        Mẫu của một file được lưu lại.
            {
                "keyword": "python",
                "document": [
                    {
                        "chunk_true": "Python là một ngôn ngữ lập trình thông dụng.",
                        "score": 0.95
                    },
                    {
                        "chunk_true": "Python được sử dụng rộng rãi trong phân tích dữ liệu.",
                        "score": 0.85
                    },

                    // Thêm nội dung khác ở đây
                ]
            }


        NOTE: Cấu trúc mỗi file Input sẽ có dạng như sau
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
        :param path:
        :return:
        """
        pass

# Ví dụ minh họa sử dụng, có thể thêm các thuộc tính hoặc phương thức cần thiết
# -----------------------------------------------------------------------------#
class MyTextChunker(TextChunker):
    def chunk_text(self, text: str, chunk_size: int) -> list:
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    def run(self, path: str):
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(os.path.join(path, filename), 'r') as f:
                    data = json.load(f)
                    chunks = self.chunk_text(data['document'], 100)
                    # Chia documnet thành các chunk
                    # Lưu chunks vào file .txt và database
                    # Lưu file JSON để dùng cho Evaluate



chunker = MyTextChunker()
path = "/path/files"
# Gọi phương thức run để chia nhỏ văn bản và lưu kết quả
chunker.run(path)