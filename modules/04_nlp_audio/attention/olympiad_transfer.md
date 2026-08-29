# Olympiad Transfer: Attention Mechanism

## 1. Nhận diện trong đề

Khi đề bài yêu cầu "trích xuất đặc trưng của tập hợp mà không phụ thuộc thứ tự", hoặc khi giải quyết bài toán trên đồ thị (Graph Neural Network), Attention là kỹ thuật ưu việt. Trong thi đấu NLP, bạn không phải viết tay Attention, nhưng **hiểu cách Attention bị OOM (Out Of Memory) với sequence dài** là mấu chốt.

## 2. Baseline tối thiểu

Thay vì viết tay, luôn gọi `nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)` khi build custom module. Thuộc tính `batch_first=True` rất quan trọng vì mặc định của hàm này (do tàn dư lịch sử) là `batch_first=False`. Code baseline thường mất khoảng 10-15 phút để tích hợp.

## 3. Metric & Validation

Thường không đánh giá trực tiếp module Attention mà đánh giá qua mô hình downstream (ví dụ classification dùng F1-score, translation dùng BLEU). Chú ý validation loss: nếu loss hội tụ chậm, có thể learning rate quá lớn, khiến softmax trong attention bão hòa.

## 4. Failure modes

- **Shape Mismatch trong quá trình transpose:** Trong MHA, khi transpose từ `(batch, seq, heads, d_k)` sang `(batch, heads, seq, d_k)` và gọi `view()` để gộp lại, nếu quên gọi `.contiguous()`, PyTorch sẽ báo lỗi văng RuntimeError.
- **OOM (Out of memory):** Độ phức tạp bộ nhớ của Attention là $O(N^2)$ với $N$ là seq_len. GPU sẽ lập tức văng lỗi CUDA Out of memory nếu sequence quá dài. Giảm batch size hoặc dùng gradient accumulation.

## 5. Sau baseline

1. **Thêm Masking:** Nếu xử lý sequence có độ dài khác nhau, bắt buộc phải mask các padding tokens để chúng không ảnh hưởng đến Attention.
2. **Flash Attention:** Tối ưu hóa GPU memory khi sequence quá dài, tích hợp Flash Attention hoặc dùng các xformers / scaled_dot_product_attention.
3. **Thêm cơ chế Gating:** Tránh cho các head của attention chú ý vào những thứ không cần thiết.

## 6. Phân bổ thời gian

- **Vòng Sơ loại (4h):**
  - 3h Public: Dùng 15 phút để tích hợp `MultiheadAttention` của PyTorch vào kiến trúc có sẵn (nếu cần model custom). Thời gian còn lại để EDA và tuning.
  - 1h Private: Kiểm tra xem masking có hoạt động chuẩn trên tập validation không.
- **Vòng Chung kết (6h):**
  - 5h Public: Có thể custom một số attention variant (như Additive Attention) hoặc thêm Flash Attention nếu dữ liệu dài.
  - 1h Private: Check lại inference speed.
