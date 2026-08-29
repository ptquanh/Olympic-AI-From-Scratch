# Bài tập: Transformer (Encoder/Decoder)

## Tầng 1: Understand

**1. Tại sao lại dùng Layer Norm thay vì Batch Norm?**
Trong CNN (CV), ta luôn dùng Batch Normalization. Nhưng trong Transformer (NLP), ta lại luôn dùng Layer Normalization. Tại sao? (Gợi ý: Độ dài của các câu trong một batch).

## Tầng 2: Implement

**1. Code Cross Attention**
Trong Decoder, khối Cross Attention nhận Q, K, V từ đâu? Hãy viết một đoạn code giả lập việc truyền biến vào `nn.MultiheadAttention` cho thao tác Cross Attention này.
Input có `target_embeds` (Từ đang dịch) và `memory` (Output của Encoder).

## Tầng 3: Experiment

**1. Hiệu ứng cộng dồn Positional Encoding**
Cho tensor biểu diễn từ (word embeddings) của 2 từ "Tôi" và "đẹp" giống hệt nhau (đều là ma trận toàn số 1, kích thước 1x512).
Nếu đưa qua lớp `PositionalEncoding(d_model=512)` như Pattern 1, tính khoảng cách (L1 hoặc MSE) giữa hai vector của 2 từ này sau khi cộng vị trí. Chúng có còn giống nhau không?

## Tầng 4: Transfer

**1. Khám phá `nn.TransformerEncoder`**
Trong PyTorch có sẵn `nn.TransformerEncoder`.
Hãy tạo một layer `encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8, batch_first=True)`.
Sau đó tạo `transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=6)`.
Cho một tensor đầu vào `src = torch.rand(32, 10, 512)` và in ra shape đầu ra. Bạn thấy PyTorch đã đóng gói toàn bộ vòng lặp n-layers cho chúng ta cực kỳ tiện lợi.

## Tầng 5: Olympiad

Trong các kỳ thi, người ta ít khi phải train 1 transformer model from scratch, mà thường load weight của BERT/RoBERTa rồi gắn thêm 1 classification head lên trên. Tuy nhiên, việc am hiểu Encoder Block giúp ta đọc hiểu các Config JSON của HuggingFace, dễ dàng debug các kiến trúc và có thể đóng băng/chỉnh sửa layer linh hoạt.
