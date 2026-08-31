# Lời giải: Transformer

<details><summary><b>U-1 — Understand</b></summary>
Trong NLP, một batch thường chứa nhiều câu có độ dài ngắn khác nhau (VD: câu 5 từ và câu 50 từ). Nếu dùng Batch Norm, việc tính trung bình dọc theo chiều batch cho từ ở vị trí thứ 50 sẽ gặp rất ít mẫu (vì hầu hết các câu khác đều ngắn và đã bị chèn padding 0). Việc này dẫn đến mean/std bị sai lệch nghiêm trọng. Ngược lại, Layer Norm tính trung bình trên từng cụm từ (từng dòng vector d_model độc lập), không bị phụ thuộc vào các câu khác trong batch.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>
Trong Cross Attention, Query (Q) là từ đang sinh ra (target), còn Key (K) và Value (V) là từ được lấy từ bảng mã hóa (memory/encoder output).

```python
import torch.nn as nn

cross_attn = nn.MultiheadAttention(d_model=512, num_heads=8, batch_first=True)

# target_embeds: (batch, tgt_seq_len, 512)

# memory: (batch, src_seq_len, 512)

out, _ = cross_attn(query=target_embeds, key=memory, value=memory)

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

```python
import torch
# Giả sử class PositionalEncoding đã định nghĩa như Pattern 1
pe = PositionalEncoding(d_model=512)

# 1 câu có 2 từ, embed toàn số 1
words = torch.ones(1, 2, 512)
out = pe(words)

# Lấy ra từ vị trí 0 (Tôi) và từ vị trí 1 (đẹp)
word0 = out[0, 0, :]
word1 = out[0, 1, :]

print("MSE:", torch.nn.MSELoss()(word0, word1).item())

```

Chúng không còn giống nhau nữa. PE đã "tiêm" tọa độ độc nhất vào từng từ, giúp Attention biết rằng dù 2 từ giống hệt nhau nhưng nằm ở 2 vị trí khác nhau trong câu.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>

<details><summary><b>T-1 — Transfer</b></summary>

```python
import torch
import torch.nn as nn

encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8, batch_first=True)
transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)

src = torch.rand(32, 10, 512)
out = transformer_encoder(src)

print(out.shape) # (32, 10, 512)

```

Shape đầu ra hoàn toàn bằng với shape đầu vào.

**Lỗi thường gặp:** fit preprocessing/chọn threshold trên test, dùng metric sai hoặc bỏ qua failure mode.

</details>

```

<details><summary><b>O-1 — Olympiad</b></summary>

Đáp án là một quy trình: baseline sớm, validation chống leakage, lưu seed/config, theo dõi metric và dành thời gian tái chạy artifact cuối. Chi tiết phụ thuộc profile kỳ thi; xem `olympiad_transfer.md`.

**Lỗi thường gặp:** áp luật của kỳ thi khác, không lưu config/artifact hoặc hết timebox mà chưa chạy infer cuối.

</details>
```
