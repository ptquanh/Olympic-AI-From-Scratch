# Bài tập: Attention Mechanism

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao là Scaled?**
Chuyện gì sẽ xảy ra với Gradient của hàm Softmax nếu ta KHÔNG chia cho $\sqrt{d_k}$ và kích thước vector (d_k) là 1024?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tính tay ma trận Attention**
Giả sử ta có `Q = [[1, 0], [0, 1]]` và `K = [[1, 0], [0, 1]]`. (Bỏ qua scale).
Hãy tính tay ma trận $QK^T$ và ma trận sau khi đi qua Softmax (theo từng hàng).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Trực quan hóa Masking**
Khởi tạo một ma trận ngẫu nhiên 4x4 (tương ứng với seq_len = 4).
Tạo một ma trận `mask` là ma trận tam giác dưới bằng hàm `torch.tril(torch.ones(4, 4))`.
Dùng hàm `masked_fill` để điền `-inf` vào những chỗ `mask == 0`.
Cuối cùng in ra kết quả của hàm Softmax trên ma trận đó.
Nhận xét về các giá trị xác suất ở nửa trên của ma trận.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Dùng `nn.MultiheadAttention`**
Trong PyTorch có sẵn `nn.MultiheadAttention`. Khởi tạo một layer này với `embed_dim=256` và `num_heads=8`.
Cho vào một tensor `x` có shape `(seq_len=10, batch_size=32, embed_dim=256)` (Lưu ý mặc định PyTorch MHA yêu cầu `batch_first=False`).
Gọi forward pass `out, attn_weights = mha(x, x, x)`.
In ra shape của `out` và `attn_weights`.

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

Hiểu về Multi-head Attention giúp bạn đọc paper và custom architecture khi thi đấu dễ dàng. Việc tính toán độ phức tạp $O(N^2)$ của chiều dài chuỗi là yếu tố cản trở Transformer xử lý văn bản siêu dài.

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
