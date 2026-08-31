# Olympiad Transfer: Autograd & Micrograd

> **Profile áp dụng:** General, trừ các mục ghi rõ PTIT 2026. Các mốc 4h/6h trong tài liệu này chỉ là timebox của PTIT 2026, không phải luật chung. Đã kiểm chứng 2026-08-31; xem [competition profiles](../../../COMPETITION_PROFILES.md) và ưu tiên thông báo chính thức mới hơn.

## 1. Tầm quan trọng trong thi đấu

Bài học này chủ yếu tập trung vào việc **xây dựng tư duy gốc rễ**. Bạn hiếm khi phải code một autograd engine thủ công trong phòng thi (PyTorch đã làm quá tốt điều đó). Tuy nhiên, hiểu về cách dòng chảy gradient đi qua mạng nơ-ron giúp bạn Debug những lỗi "chết người" trong phòng thi, ví dụ như **Vanishing Gradient** hay **Exploding Gradient**.

## 2. Gradient Của Các Phép Toán Cơ Bản

- **Phép Cộng (Add):** Gradient Router. Nhận 1 và phân bổ giống hệt nhau xuống các nhánh con.
- **Phép Nhân (Multiply):** Gradient Switcher. Đổi chéo (swap) dữ liệu của $x$ cho $y$. Gradient của một nhánh sẽ tỉ lệ thuận với độ lớn dữ liệu của nhánh còn lại.
- **Phép Max (như ReLU):** Gradient Router (có điều kiện). Chỉ cho luồng gradient chảy qua nhánh có giá trị lớn nhất, các nhánh khác bị vô hiệu hóa (0).

## 3. Tại sao mạng nơ ron sâu lại khó huấn luyện (Failure Mode)?

Nếu bạn sử dụng phép nhân (Multiply) trong mạng và giá trị của trọng số nhỏ hơn 1 (vd: 0.1), ở mỗi tầng, gradient sẽ liên tục bị nhân với 0.1. Đi qua 50 tầng mạng, gradient sẽ về xấp xỉ 0 (1e-50) — biến mất. Điều này giải thích tại sao mạng tích chập sâu hay mạng RNN truyền thống cực kỳ khó hội tụ nếu thiếu cấu trúc Residual (ResNet). (ResNet dùng phép cộng để truyền thẳng gradient mà không qua phép nhân).
