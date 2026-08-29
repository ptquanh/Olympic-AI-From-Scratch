# Lời giải: Prompt Engineering

<details><summary><b>Tầng 1: Understand</b></summary>

1. System Prompt đóng vai trò định hình "nhân cách", ngữ cảnh cốt lõi và các quy tắc chung cho LLM trong toàn bộ cuộc hội thoại. Nó khác với User Prompt là những câu hỏi hoặc yêu cầu cụ thể theo từng lượt.
2. Từ "Let's think step by step" kích hoạt kỹ thuật Chain-of-Thought (Zero-shot CoT).
3. Hạn chế của Few-shot: Tốn nhiều token (dẫn đến tốn tiền và chậm), có thể làm mô hình học vẹt (overfit) vào format của ví dụ thay vì hiểu bản chất, và bị giới hạn bởi context window của mô hình.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

1. System: "Bạn là một AI phân tích cảm xúc. Bạn chỉ được trả lời 'TÍCH CỰC' hoặc 'TIÊU CỰC', không được giải thích thêm."
   User: "Món ăn này quá tuyệt vời!" -> TÍCH CỰC.
2. Thay đổi prompt thành: "Translate English to French:\napple => pomme\ncat => chat\nhello =>" để mô hình học theo pattern.

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

1. Khi không có CoT, mô hình có thể trả lời sai (ví dụ: cộng sai số). Khi thêm CoT, do mô hình sinh ra từng bước trung gian, nó có thời gian "suy nghĩ" và tính toán chính xác hơn trước khi đưa ra kết quả cuối.
2. Mô hình nhỏ (như `gpt2`) không có khả năng reasoning tốt, nên dù dùng Few-shot hay CoT, nó vẫn sinh ra text vô nghĩa hoặc không theo format. Các kỹ thuật này chỉ phát huy sức mạnh trên các mô hình đủ lớn (như GPT-3, Llama-2-7B trở lên).

</details>
