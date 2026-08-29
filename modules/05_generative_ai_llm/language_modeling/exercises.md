# Bài tập: Language Modeling

## Tầng 1: Understand

1. Một mô hình LM được yêu cầu dự đoán từ tiếp theo của câu "Trời hôm nay rất...". Nó đưa ra các xác suất: `{"đẹp": 0.8, "xấu": 0.1, "mua": 0.05, "bão": 0.05}`. Nếu sử dụng Greedy Search, mô hình sẽ chọn từ nào?
2. Tại sao người ta không dùng BERT để sinh ra một đoạn văn bản dài?
3. Nếu Loss trên tập Test là 2.5, thì Perplexity xấp xỉ bằng bao nhiêu? ($e pprox 2.718$)

## Tầng 2: Implement

1. Mở `lab.ipynb`, khởi tạo HuggingFace pipeline với mô hình `gpt2`. Truyền vào prompt: "The future of AI is".
2. Chỉnh tham số `temperature` của pipeline (thử giá trị 0.1 và 2.0). Chạy lại nhiều lần và quan sát sự thay đổi trong văn bản được sinh ra. Viết nhận xét vào cell markdown.

## Tầng 3: Experiment

1. Thay thế mô hình `gpt2` bằng một mô hình khác nhỏ trên HuggingFace (ví dụ `TinyLlama/TinyLlama-1.1B-Chat-v1.0` - có thể chạy hơi chậm trên CPU). So sánh chất lượng văn bản sinh ra giữa hai mô hình.
2. Tìm hiểu về tham số `top_k` và `top_p` trong hàm sinh văn bản. Thử nghiệm kết hợp `temperature=0.7`, `top_k=50` xem kết quả có tự nhiên hơn không.
