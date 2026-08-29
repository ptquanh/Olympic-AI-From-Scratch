# Olympiad Transfer: Transformer

## 1. Nhận diện trong đề

Bất kỳ bài toán nào về phân tích văn bản (Text Classification, NER, QA, Translation), Transformer (cụ thể là BERT/RoBERTa/T5/GPT) đều là SOTA.

## 2. Baseline tối thiểu

Thay vì build from scratch, baseline là dùng thư viện HuggingFace `transformers`.

- Import `AutoModelForSequenceClassification`
- Gọi hàm `model(input_ids, attention_mask)`

Tuy nhiên, kiến thức from scratch trong bài này giúp bạn hiểu cấu trúc đầu vào `attention_mask` của HuggingFace chính là cái "mask" ta đã học, và `hidden_states` chứa các output của từng Encoder Block.

## 3. Failure modes

- **Quên Padding Mask:** Nếu câu ngắn được đệm bằng padding token `0`, mà bạn KHÔNG dùng Padding Mask trong Attention, các từ thật sẽ "chú ý" (attention) sang phần padding (vì padding vector có giá trị). Dẫn đến output bị nhiễu.
- **Learning rate warmup:** Transformer RẤT khó huấn luyện from scratch nếu không có Learning Rate Warmup (tăng dần LR từ 0 lên max trong khoảng 10% quá trình đầu, sau đó giảm dần). Nếu train mà loss bị `NaN` hoặc kẹt, hãy thêm warmup scheduler.

### 3. Metric & Validation

- **Metric:** Thường là BLEU/ROUGE cho Machine Translation hoặc F1 cho Classification.
- **Validation:** Giữ nguyên một tập Hold-out lớn để đánh giá khả năng generalisation.

### 4. Failure modes

- **Catastrophic Forgetting:** Nếu fine-tune với Learning Rate quá lớn. Bắt buộc lr < 5e-5.
- **Vanishing Gradient:** Xảy ra nếu quên LayerNorm trong các block sâu.

### 5. Sau baseline

- Thay vì dùng Transformer From Scratch, hãy sử dụng RoBERTa/DeBERTa pre-trained (luôn thắng trong mọi kỳ thi).
- Dùng kỹ thuật Layer-wise Learning Rate Decay (LLRD).

### 6. Phân bổ thời gian (Chung kết 6h)

- 1h: EDA text, tìm max_length phù hợp.
- 1h: Dựng baseline bằng Pre-trained Transformer.
- 3h: Luyện tập mô hình (thường train rất chậm, cần setup sớm).
- 1h: Phân tích lỗi, tuning.
