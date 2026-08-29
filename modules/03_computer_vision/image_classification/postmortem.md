# Postmortem: Phân tích lỗi thường gặp

Sau khi chấm chéo hàng trăm bài dự thi Olympic và bài tập lớn, đây là những lỗi "chết người" sinh viên hay mắc phải nhất trong bài Image Classification:

## 1. Quên `model.eval()` hoặc `torch.no_grad()` khi Validation/Inference

**Triệu chứng:** Hết RAM (OOM - Out of Memory) một cách vô lý.
**Lý do:** Nếu không có `torch.no_grad()`, PyTorch vẫn âm thầm xây dựng đồ thị đạo hàm khổng lồ trong bộ nhớ kể cả lúc đang tính Val Loss. Còn nếu thiếu `model.eval()`, các lớp như Dropout, BatchNorm sẽ hoạt động sai lệch, khiến độ chính xác trên tập Validation giảm sốc so với tập Train.

## 2. Leakage (Rò rỉ) Data Augmentation sang tập Validation

**Triệu chứng:** Accuracy trên tập Validation rất thấp và rất bất ổn định (nhảy lên nhảy xuống).
**Lý do:** Bạn đã truyền nhầm `train_transforms` (chứa các lệnh xoay ảnh ngẫu nhiên, nhiễu ngẫu nhiên) cho tập Validation.

## 3. Khởi tạo Learning Rate quá cao khi Fine-Tuning

**Triệu chứng:** Loss tụt rất nhanh lúc đầu, nhưng sau đó Loss bỗng dưng văng lên trời (NaN) hoặc Loss đi ngang mãi mãi.
**Lý do:** Mô hình Pre-trained đã được train hội tụ từ trước. Việc bạn dùng Learning Rate quá to (ví dụ: `0.1` hay `0.01` thay vì `1e-4`) sẽ làm phá vỡ các trọng số đã được tinh chỉnh của mô hình cũ, gây sốc (Catastrophic Forgetting). Khi Fine-Tuning, luôn bắt đầu bằng Learning Rate nhỏ (VD: `1e-4` cho mạng AdamW).
