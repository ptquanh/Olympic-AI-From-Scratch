# Text Classification Competition Lab

> **Track:** Foundation ⭐ | Contest ⭐

## ① Giới thiệu

Chào mừng đến với Đấu trường Phân loại Văn bản! Khác với các bài toán CV (xử lý ảnh) mà bạn đã làm, xử lý văn bản yêu cầu một quy trình tiền xử lý khá lằng nhằng (Tokenization, Padding, Truncation) trước khi có thể đưa vào mạng Neural Network.

## ② Learning Outcomes

- Xây dựng thành công pipeline tiền xử lý văn bản bằng `AutoTokenizer` của thư viện HuggingFace.
- Áp dụng Transfer Learning: tải mô hình pre-trained BERT/PhoBERT bằng `AutoModelForSequenceClassification`.
- Fine-tune (huấn luyện tinh chỉnh) mô hình bằng PyTorch training loop chuẩn.
- Ghi log và đánh giá kết quả bằng metric F1-Score (rất quan trọng trong NLP).

## ③ Bài toán: Nhận diện bình luận độc hại (Toxic Comment Classification)

**Mô tả:**
Trên các nền tảng mạng xã hội, việc tự động phát hiện và lọc các bình luận mang tính chất công kích, thù ghét là bài toán sống còn. Bạn được cung cấp một tập dữ liệu gồm các bình luận và nhãn 0 (Bình thường) hoặc 1 (Độc hại).

**Metric đánh giá:** F1-Score (Macro)
Trong bài toán này, số lượng bình luận bình thường thường áp đảo bình luận độc hại (Mất cân bằng dữ liệu). Do đó, Accuracy (độ chính xác tổng thể) sẽ không phản ánh đúng thực tế. Ta dùng F1-Score để đánh giá độ hiệu quả của việc bắt đúng các bình luận độc hại mà không nhận diện nhầm quá nhiều bình luận bình thường.

## ④ Hướng dẫn triển khai

1. **Dữ liệu:** (Giả lập) Tải tập dữ liệu text (tiếng Anh hoặc tiếng Việt).
2. **Tokenizer:** Văn bản không thể nhân ma trận được. Bạn phải chuyển nó thành số. Gọi `tokenizer(text, padding=True, truncation=True, max_length=128)` để biến câu thành các mảng số nguyên (input_ids) và mảng mặt nạ (attention_mask).
3. **Mô hình:** Tải pre-trained model (VD: `bert-base-uncased` hoặc `vinai/phobert-base`). Thay thế lớp phân loại (Classifier head) bằng một lớp mới có `num_labels=2`.
4. **Huấn luyện:** Sử dụng `AdamW` với Learning Rate siêu nhỏ (VD: `2e-5`) vì mô hình đã được huấn luyện rất tốt rồi, ta chỉ "tinh chỉnh" (fine-tune) nhẹ lại mà thôi.
5. **Nộp bài:** Chạy tập test, in kết quả ra file `submission.csv` và kiểm tra trên rubric.

## ⑯ Time Estimate

Theory: ~1h, Code: ~4h (Fine-tuning BERT khá tốn thời gian chạy)
