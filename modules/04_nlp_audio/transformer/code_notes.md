# Code Notes: Transformer

## 🔑 Core Patterns

### Pattern 1: Positional Encoding

```python
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        # Tạo ma trận [max_len, d_model] chứa toàn số 0
        pe = torch.zeros(max_len, d_model)

        # Cột pos: [0, 1, 2... max_len-1]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # Số hạng phân số bên trong sin/cos
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        # Gán giá trị
        pe[:, 0::2] = torch.sin(position * div_term) # Vị trí chẵn
        pe[:, 1::2] = torch.cos(position * div_term) # Vị trí lẻ

        # Thêm chiều batch: (1, max_len, d_model)
        pe = pe.unsqueeze(0)

        # Đăng ký làm buffer (không cập nhật qua backprop, nhưng lưu vào state_dict)
        self.register_buffer('pe', pe)

    def forward(self, x):
        # x shape: (batch_size, seq_len, d_model)
        x = x + self.pe[:, :x.size(1)]
        return x

```

### Pattern 2: Pre-LN Transformer Encoder Block

```python
import torch.nn as nn

class EncoderBlock(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, num_heads, batch_first=True)
        self.norm1 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)

        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(), # Hoặc GELU
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model)
        )
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, x, src_mask=None):
        # 1. Pre-LN Self-Attention
        nx = self.norm1(x)
        attn_out, _ = self.attn(nx, nx, nx, attn_mask=src_mask)
        x = x + self.dropout1(attn_out)

        # 2. Pre-LN FFN
        nx = self.norm2(x)
        ffn_out = self.ffn(nx)
        x = x + self.dropout2(ffn_out)

        return x

```

## 📋 API Cheat Sheet

| Việc cần làm                 | Code                                   | Link Docs                                                                                                                         |
| ---------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Đăng ký hằng số trong Module | `self.register_buffer('name', tensor)` | [torch.nn.Module.register_buffer](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_buffer) |
| Chuẩn hóa Layer Norm         | `nn.LayerNorm(d_model)`                | [nn.LayerNorm](https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)                                                 |
| PyTorch Transformer (Có sẵn) | `nn.Transformer(d_model, nhead, ...)`  | [nn.Transformer](https://pytorch.org/docs/stable/generated/torch.nn.Transformer.html)                                             |

## 🏋️ Bài Luyện Code Tay

| #   | Bài                                                                                            | Thời gian | Hint (ẩn)                                                                                                                          |
| --- | ---------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Viết đoạn code khởi tạo class `DecoderBlock` có thêm lớp `Cross-Attention`. (Giả định Pre-LN). | 5 phút    | Có 3 LayerNorm. Self-Attn $\rightarrow$ Norm2 $\rightarrow$ Cross-Attn (Q=nx, K=mem, V=mem) $\rightarrow$ Norm3 $\rightarrow$ FFN. |
| 2   | Code Positional Encoding theo công thức sin/cos                                                | 20p       | Dùng torch.arange và torch.exp                                                                                                     |
| 3   | Khởi tạo Transformer Encoder Block (Pre-LN)                                                    | 15p       | Chú ý thứ tự LayerNorm trước Attention/FFN                                                                                         |

### 🧠 Flashcards

| Hỏi                                                      | Trả lời                                                                                          |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Tại sao phải có Positional Encoding?                     | Vì Attention không có khái niệm về thứ tự từ, tính toán song song toàn bộ dãy.                   |
| Pre-LN khác Post-LN ở đâu?                               | Pre-LN đặt LayerNorm trước Attention/FFN, giúp gradient flow tốt hơn và dễ hội tụ khi model sâu. |
| Hàm kích hoạt nào thường dùng trong FFN của Transformer? | GELU hoặc ReLU.                                                                                  |
