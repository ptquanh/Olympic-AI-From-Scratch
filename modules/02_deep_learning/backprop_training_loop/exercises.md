# Bài tập: Backprop & Training Loop

## Tầng 1: Understand

**1. Tại sao hàm Kích Hoạt lại quan trọng?**
Chuyện gì sẽ xảy ra nếu ta xây dựng một mạng nơ-ron khổng lồ gồm 100 tầng (layer), hàng triệu tham số, nhưng ta lại quên gắn hàm Kích hoạt (như ReLU) ở cuối mỗi nơ-ron?

## Tầng 2: Implement

**1. Tùy chỉnh Optimizer**
Trong Training Loop ở phần học, ta cập nhật theo công thức tĩnh: `p.data -= 0.05 * p.grad`.
Hãy thử cài đặt cơ chế **Learning Rate Decay**: Ở các vòng lặp (epoch) đầu, learning rate là 0.1, sau 100 epochs, nó giảm dần xuống 0.01 để giúp mô hình hội tụ tốt hơn, không bị dao động (văng) quanh điểm tối ưu.

## Tầng 3: Experiment

**1. Khảo sát Data**
Khởi tạo một mạng nơ ron `MLP(2, [16, 16, 1])`.
Cho dữ liệu `make_moons(n_samples=100, noise=0.1)` (dữ liệu hình 2 bán nguyệt xen kẽ nhau) của scikit-learn.
Viết vòng lặp huấn luyện bằng Micrograd Engine của chúng ta để phân loại bộ dữ liệu này. In ra Loss sau mỗi 10 epoch.

## Tầng 4: Transfer

**1. Chuyển sang PyTorch thực sự**
Bây giờ bạn đã hiểu gốc rễ. Hãy thay thế toàn bộ class `MLP`, `Layer`, `Neuron` bên trên bằng thư viện `torch.nn` của PyTorch.

- Sử dụng `nn.Sequential` kết hợp `nn.Linear` và `nn.ReLU`.
- Sử dụng hàm Loss `nn.MSELoss`.
- Sử dụng hàm cập nhật `torch.optim.SGD`.
  Viết lại vòng lặp huấn luyện. Bạn sẽ thấy PyTorch giúp rút ngắn code cực kỳ nhiều nhưng bản chất bên trong y hệt những gì chúng ta vừa tự viết.

## Tầng 5: Olympiad

Không có thi đấu trực tiếp cho nội dung này, nhưng code PyTorch là kỹ năng sống còn.
