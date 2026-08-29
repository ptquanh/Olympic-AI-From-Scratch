# Bài tập: Autograd & Micrograd

## Tầng 1: Understand

**1. Backward của hàm ReLU**
Hàm ReLU được định nghĩa là $f(x) = \max(0, x)$. Vậy khi truyền ngược (backward) qua một node ReLU, đoạn code sẽ hoạt động như thế nào dựa trên giá trị của dữ liệu đầu vào?

## Tầng 2: Implement

**1. Bổ sung phép tính**
Dựa trên class `Value` cơ bản trong phần học. Hãy cài đặt thêm hàm `__pow__(self, other)` hỗ trợ tính toán số mũ.
Lưu ý: chỉ cần cài đặt `other` là số thuần túy (float/int), không cần là đối tượng `Value`. Ví dụ: `x**2`.
Gợi ý toán học: Đạo hàm của $x^n$ là $n \times x^{n-1}$.

## Tầng 3: Experiment

**1. Mô phỏng PyTorch**
Sử dụng engine tự build, khởi tạo 2 biến $x = \text{Value}(2.0)$ và $y = \text{Value}(-3.0)$.
Tính phương trình $z = 2x^2 - y^3 + x \cdot y$.
Gọi hàm `backward()` thủ công cho đồ thị này và in ra `x.grad`, `y.grad`.
Sau đó tính toán bằng tay (giải tích cơ bản) xem hai đáp án có khớp nhau không.

## Tầng 4: Transfer

**1. Topologial Sort**
Hàm backward cuối cùng của đồ thị phải duyệt qua tất cả các node để gọi hàm `_backward()` của từng node. Tuy nhiên, nó phải được gọi theo đúng thứ tự (đảm bảo node cha tính xong thì mới tính đến node con). Quá trình sắp xếp này trong đồ thị được gọi là Topological Sort.
Hãy viết một hàm đệ quy `build_topo()` để thực hiện Topological Sort cho các node của class `Value`.

## Tầng 5: Olympiad

Không yêu cầu thi đấu trực tiếp, nhưng code Micrograd giúp debug gradient siêu tốt.
