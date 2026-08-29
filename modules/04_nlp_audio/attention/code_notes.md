# Code Notes: Attention Mechanism

## 🔑 Core Patterns

### Pattern 1: Scaled Dot-Product Attention

```python
import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q, K, V, mask=None):
    # Q, K, V shapes: (batch_size, num_heads, seq_len, d_k)
    d_k = Q.size(-1)

    # 1. Q * K^T (Lưu ý transpose 2 chiều cuối)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)

    # 2. Masking (Dành cho Decoder để không nhìn thấy tương lai)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))

    # 3. Softmax
    attention_weights = F.softmax(scores, dim=-1)

    # 4. Nhân với V
    output = torch.matmul(attention_weights, V)
    return output, attention_weights
```

### Pattern 2: Multi-Head Attention Shape Transformation

```python
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads

        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V, mask=None):
        batch_size = Q.size(0)

        # 1. Linear & Tách Head
        # (batch, seq, d_model) -> (batch, seq, heads, d_k) -> (batch, heads, seq, d_k)
        q = self.W_q(Q).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        k = self.W_k(K).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        v = self.W_v(V).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)

        # 2. Attention
        out, _ = scaled_dot_product_attention(q, k, v, mask)

        # 3. Gộp Head
        # (batch, heads, seq, d_k) -> (batch, seq, heads, d_k) -> (batch, seq, d_model)
        out = out.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # 4. Linear cuối
        return self.W_o(out)
```

## 📋 API Cheat Sheet

| Việc cần làm                           | Code                                          | Link Docs                                                                                            |
| -------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Hoán đổi 2 chiều cuối                  | `x.transpose(-2, -1)`                         | [torch.transpose](https://pytorch.org/docs/stable/generated/torch.transpose.html)                    |
| Masking với giá trị âm vô cùng         | `x.masked_fill(mask == 0, float('-inf'))`     | [torch.Tensor.masked_fill](https://pytorch.org/docs/stable/generated/torch.Tensor.masked_fill_.html) |
| Đảm bảo bộ nhớ liền mạch sau transpose | `x.contiguous()`                              | [torch.Tensor.contiguous](https://pytorch.org/docs/stable/generated/torch.Tensor.contiguous.html)    |
| PyTorch MHA (built-in)                 | `nn.MultiheadAttention(embed_dim, num_heads)` | [nn.MultiheadAttention](https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html)  |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                                                        | Thời gian | Hint (ẩn)                                              |
| --- | ---------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------ |
| 1   | Viết hàm `scaled_dot_product_attention(Q, K, V)` mà không dùng `torch.matmul`, dùng `@` operator thay thế. | 3 phút    | `(Q @ K.transpose(-2, -1)) / math.sqrt(Q.size(-1))`    |
| 2   | Code thao tác tách 1 Tensor `(B, Seq, 512)` thành `(B, 8, Seq, 64)`.                                       | 2 phút    | `view(B, Seq, 8, 64).transpose(1, 2)`                  |
| 3   | Tự code Masked Self-Attention forward pass                                                                 | 15p       | Dùng torch.tril() để tạo mask tam giác dưới, fill -inf |

## 🧠 Flashcards

| Hỏi                                                   | Trả lời                                                                                                                                                                      |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tại sao phải `contiguous()` trước khi `view()`?       | Hàm `transpose()` chỉ thay đổi metadata (stride) mà không đổi thứ tự vật lý trên RAM. `view()` yêu cầu bộ nhớ liền mạch, nên phải dùng `contiguous()` để tạo bản sao vật lý. |
| Masking dùng `-inf` trước hàm Softmax có tác dụng gì? | `exp(-inf) = 0`, nên khi đưa qua Softmax, trọng số của những vị trí bị mask sẽ bằng chính xác 0, coi như bị phớt lờ hoàn toàn.                                               |
