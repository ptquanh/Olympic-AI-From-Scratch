# Bài tập: Backprop & Training Loop

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Tại sao hàm Kích Hoạt lại quan trọng?**
Chuyện gì sẽ xảy ra nếu ta xây dựng một mạng nơ-ron khổng lồ gồm 100 tầng (layer), hàng triệu tham số, nhưng ta lại quên gắn hàm Kích hoạt (như ReLU) ở cuối mỗi nơ-ron?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Tùy chỉnh Optimizer**
Trong Training Loop ở phần học, ta cập nhật theo công thức tĩnh: `p.data -= 0.05 * p.grad`.
Hãy thử cài đặt cơ chế **Learning Rate Decay**: Ở các vòng lặp (epoch) đầu, learning rate là 0.1, sau 100 epochs, nó giảm dần xuống 0.01 để giúp mô hình hội tụ tốt hơn, không bị dao động (văng) quanh điểm tối ưu.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Khảo sát Data**
Khởi tạo một mạng nơ ron `MLP(2, [16, 16, 1])`.
Cho dữ liệu `make_moons(n_samples=100, noise=0.1)` (dữ liệu hình 2 bán nguyệt xen kẽ nhau) của scikit-learn.
Viết vòng lặp huấn luyện bằng Micrograd Engine của chúng ta để phân loại bộ dữ liệu này. In ra Loss sau mỗi 10 epoch.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Chuyển sang PyTorch thực sự**
Bây giờ bạn đã hiểu gốc rễ. Hãy thay thế toàn bộ class `MLP`, `Layer`, `Neuron` bên trên bằng thư viện `torch.nn` của PyTorch.

- Sử dụng `nn.Sequential` kết hợp `nn.Linear` và `nn.ReLU`.
- Sử dụng hàm Loss `nn.MSELoss`.
- Sử dụng hàm cập nhật `torch.optim.SGD`.
  Viết lại vòng lặp huấn luyện. Bạn sẽ thấy PyTorch giúp rút ngắn code cực kỳ nhiều nhưng bản chất bên trong y hệt những gì chúng ta vừa tự viết.

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

Không có thi đấu trực tiếp cho nội dung này, nhưng code PyTorch là kỹ năng sống còn.

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
