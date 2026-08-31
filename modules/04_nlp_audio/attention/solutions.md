# Lời giải: Attention Mechanism

<details><summary><b>U-1 — Understand</b></summary>
Tích vô hướng của 2 vector càng dài thì kết quả càng lớn. Nếu d_k = 1024, giá trị tích vô hướng có thể rất lớn. Khi đưa các số lớn này vào hàm Softmax (dùng $e^x$), một giá trị sẽ cực kỳ lớn và chèn ép hoàn toàn các giá trị khác (trở thành vector one-hot như [1, 0, 0, 0]). Hàm Softmax lúc này bị "bão hòa", đạo hàm (gradient) gần như bằng 0 (Vanishing Gradient), khiến mô hình không học được gì cả.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>
$QK^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$

Softmax theo từng hàng:

- Hàng 1: $e^1 / (e^1 + e^0) \approx 2.71 / 3.71 \approx 0.73$, và $1 / 3.71 \approx 0.27$.
- Kết quả: $\begin{bmatrix} 0.73 & 0.27 \\ 0.27 & 0.73 \end{bmatrix}$

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

```python
import torch
import torch.nn.functional as F

scores = torch.randn(4, 4)
mask = torch.tril(torch.ones(4, 4))
scores = scores.masked_fill(mask == 0, float('-inf'))
attn = F.softmax(scores, dim=-1)

print(attn)

```

Nhận xét: Xác suất ở nửa trên (tương ứng với các từ ở tương lai) hoàn toàn bằng 0. Mỗi từ ở hàng $i$ chỉ có thể chia sẻ tỷ lệ "chú ý" (tổng=1) cho các từ từ $0$ đến $i$. Đây chính là **Causal Masking** dùng trong mô hình Decoder (như GPT).

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

```python
import torch
import torch.nn as nn

mha = nn.MultiheadAttention(embed_dim=256, num_heads=8)
x = torch.randn(10, 32, 256) # (seq, batch, embed)

out, attn_weights = mha(x, x, x)

print("Output shape:", out.shape) # (10, 32, 256)
print("Attn Weights shape:", attn_weights.shape) # (32, 10, 10)

```

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
