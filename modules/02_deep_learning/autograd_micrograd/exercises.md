# Bài tập: Autograd & Micrograd

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Backward của hàm ReLU**
Hàm ReLU được định nghĩa là $f(x) = \max(0, x)$. Vậy khi truyền ngược (backward) qua một node ReLU, đoạn code sẽ hoạt động như thế nào dựa trên giá trị của dữ liệu đầu vào?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Bổ sung phép tính**
Dựa trên class `Value` cơ bản trong phần học. Hãy cài đặt thêm hàm `__pow__(self, other)` hỗ trợ tính toán số mũ.
Lưu ý: chỉ cần cài đặt `other` là số thuần túy (float/int), không cần là đối tượng `Value`. Ví dụ: `x**2`.
Gợi ý toán học: Đạo hàm của $x^n$ là $n \times x^{n-1}$.

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**1. Mô phỏng PyTorch**
Sử dụng engine tự build, khởi tạo 2 biến $x = \text{Value}(2.0)$ và $y = \text{Value}(-3.0)$.
Tính phương trình $z = 2x^2 - y^3 + x \cdot y$.
Gọi hàm `backward()` thủ công cho đồ thị này và in ra `x.grad`, `y.grad`.
Sau đó tính toán bằng tay (giải tích cơ bản) xem hai đáp án có khớp nhau không.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

**1. Topologial Sort**
Hàm backward cuối cùng của đồ thị phải duyệt qua tất cả các node để gọi hàm `_backward()` của từng node. Tuy nhiên, nó phải được gọi theo đúng thứ tự (đảm bảo node cha tính xong thì mới tính đến node con). Quá trình sắp xếp này trong đồ thị được gọi là Topological Sort.
Hãy viết một hàm đệ quy `build_topo()` để thực hiện Topological Sort cho các node của class `Value`.

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

Không yêu cầu thi đấu trực tiếp, nhưng code Micrograd giúp debug gradient siêu tốt.

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
