from abc import ABC, abstractmethod
import json

class SemanticSearchEvaluator(ABC):
    @abstractmethod
    def evaluate(self, query: str, results: list) -> float:
        """
        Phương thức này đánh giá kết quả Senmantic Search dựa trên một truy vấn và kết quả.

        :param query: Truy vấn tìm kiếm ngữ nghĩa.
        :param results: Danh sách các kết quả tìm kiếm.
        :return: Điểm số đánh giá.
        """
        pass

    @abstractmethod
    def evaluate_all(self, path_queries_results: str) -> float:
        """
        Phương thức này đánh giá kết quả Senmantic Search dựa trên tất cả các truy vấn và kết quả.
        Mỗi file trong thư mục path_queries_results sẽ có mẫu như sau:
        {
                "keyword": "python",
                "document": [
                    {
                        "chunk_predict": "Python là một ngôn ngữ lập trình thông dụng.",
                        "score": 0.95
                    },
                    {
                        "chunk_predict": "Python được sử dụng rộng rãi trong phân tích dữ liệu.",
                        "score": 0.85
                    },

                    // Thêm nội dung khác ở đây
                ]
            }

        :param path_queries_results: Đường dẫn tới thư mục chưa tất cả các Truy vấn và kết quả.
        :return: float
        """


# Ví dụ minh họa định nghĩa sử dụng, có thể thêm các thuộc tính hoặc phương thức cần thiết
# ----------------------------------------------------------------------------------------#

if __name__ == '__main__':

    class MySemanticSearchEvaluator(SemanticSearchEvaluator):
        def evaluate(self, query: str, results: list) -> float:
            # Đây là một hàm đánh giá giả định
            return len(results) / 100.0

        def evaluate_all(self, path_queries_results: str) -> float:
            # Đây là một logic giả định
            with open(path_queries_results, 'r') as f:
                data = json.load(f)
            total_score = 0
            for query_results in data:
                query = query_results['query']
                results = query_results['results']
                total_score += self.evaluate(query, results)
            return total_score / len(data)

    # Sử dụng lớp MySemanticSearchEvaluator
    evaluator = MySemanticSearchEvaluator()
    score = evaluator.evaluate_all('path_to_your_file.json')
    print(f'The evaluation score is {score}')