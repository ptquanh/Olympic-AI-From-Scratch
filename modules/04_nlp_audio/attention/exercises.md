# Bài tập: Attention Mechanism

## Tầng 1: Understand

**1. Tại sao là Scaled?**
Chuyện gì sẽ xảy ra với Gradient của hàm Softmax nếu ta KHÔNG chia cho $\sqrt{d_k}$ và kích thước vector (d_k) là 1024?

## Tầng 2: Implement

**1. Tính tay ma trận Attention**
Giả sử ta có `Q = [[1, 0], [0, 1]]` và `K = [[1, 0], [0, 1]]`. (Bỏ qua scale).
Hãy tính tay ma trận $QK^T$ và ma trận sau khi đi qua Softmax (theo từng hàng).

## Tầng 3: Experiment

**1. Trực quan hóa Masking**
Khởi tạo một ma trận ngẫu nhiên 4x4 (tương ứng với seq_len = 4).
Tạo một ma trận `mask` là ma trận tam giác dưới bằng hàm `torch.tril(torch.ones(4, 4))`.
Dùng hàm `masked_fill` để điền `-inf` vào những chỗ `mask == 0`.
Cuối cùng in ra kết quả của hàm Softmax trên ma trận đó.
Nhận xét về các giá trị xác suất ở nửa trên của ma trận.

## Tầng 4: Transfer

**1. Dùng `nn.MultiheadAttention`**
Trong PyTorch có sẵn `nn.MultiheadAttention`. Khởi tạo một layer này với `embed_dim=256` và `num_heads=8`.
Cho vào một tensor `x` có shape `(seq_len=10, batch_size=32, embed_dim=256)` (Lưu ý mặc định PyTorch MHA yêu cầu `batch_first=False`).
Gọi forward pass `out, attn_weights = mha(x, x, x)`.
In ra shape của `out` và `attn_weights`.

## Tầng 5: Olympiad

Hiểu về Multi-head Attention giúp bạn đọc paper và custom architecture khi thi đấu dễ dàng. Việc tính toán độ phức tạp $O(N^2)$ của chiều dài chuỗi là yếu tố cản trở Transformer xử lý văn bản siêu dài.
