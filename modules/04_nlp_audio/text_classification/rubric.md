# Tiêu chí chấm điểm (Rubric)

| Tiêu chí                       | Điểm | Điều kiện đạt được                                                                                                                                                 |
| ------------------------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Baseline (Chạy được mã)** | 20   | Pipeline chạy từ đầu đến cuối không lỗi, tạo ra được file `submission.csv`. Loss trên tập train có giảm.                                                           |
| **2. Tiền xử lý dữ liệu**      | 20   | Implement Dataset class với Tokenizer chuẩn. Không bị lỗi Tensor shape mismatch giữa input_ids và attention_mask. Đã xử lý (clean) các ký tự lạ, HTML tags nếu có. |
| **3. Mô hình**                 | 20   | Tải thành công Pre-trained model (BERT hoặc tương đương). Thiết lập đúng số `num_labels`. (Thưởng 5đ nếu dùng model Tiếng Việt cho data Tiếng Việt).               |
| **4. Kỹ thuật Huấn luyện**     | 20   | Dùng `AdamW`, có Gradient Clipping, có Learning Rate Scheduler (Linear Warmup). Batch size phù hợp không bị OOM.                                                   |
| **5. Đánh giá & Phân tích**    | 20   | In ra báo cáo phân loại (Classification Report) và F1-Score trên tập Validation. Cấu trúc project rõ ràng, có TODOs đã hoàn thiện.                                 |

**Tổng điểm:** 100
