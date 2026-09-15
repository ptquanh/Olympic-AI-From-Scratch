# Solutions: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

Chỉ mở sau khi tự làm; đối chiếu cả hành vi và lý do.

## E-1

<details><summary>Mở lời giải</summary>

Xem diagnostic ở solution. Phân biệt lỗi dấu với lr quá lớn bằng một bước nhỏ và gradient số.

**Kết quả cần kiểm tra:** Bad step tăng loss trên fixture; correct step giảm; có bảng hoặc plot được gắn nhãn đầy đủ.

**Lỗi thường gặp:** Loss giảm nghĩa là mọi gradient đúng. Một số lỗi vẫn làm loss giảm; đối chiếu finite difference trên case không suy biến.

</details>

## T-1

<details><summary>Mở lời giải</summary>

CrossEntropyLoss nhận logits (n,C), target index (n,); kiểm tra gradient norm và thay đổi tham số; eval kết hợp no_grad cho inference.

**Kết quả cần kiểm tra:** Liệt kê logits/target shape, loss phù hợp, zero_grad→forward→loss→backward→step, train/eval và tiny-overfit.

**Lỗi thường gặp:** Gradient càng gần 0 càng tốt. Có thể bị đứt graph hoặc saturation; kiểm tra parameter update và tiny-overfit.

</details>

## O-1

<details><summary>Mở lời giải</summary>

Đối chiếu gradient số, sửa hướng update và refit bằng config được chọn qua validation; chạy lại từ kernel sạch.

**Kết quả cần kiểm tra:** Gradient relative error <1e-6 trên fixture; tiny accuracy=1; 64 dòng id/label; postmortem nêu root cause.

**Lỗi thường gặp:** Batch dễ học được thì bài thi sẽ điểm cao. Đó là sanity check cho loop; validation độc lập mới đo generalization.

</details>

## Code đối chiếu chạy độc lập

```python
import numpy as np
X = np.array([[-1.0], [1.0]])
y = np.array([0.0, 1.0])
w = np.zeros(1)
p = 1 / (1 + np.exp(-(X @ w)))
gradient = X.T @ (p - y) / len(y)
assert np.allclose(gradient, [-0.5])
w -= 0.1 * gradient
assert np.allclose(w, [0.05])
```

Để tái hiện toàn bộ pipeline và số đo, chạy [starter.ipynb](starter.ipynb) → [solution.ipynb](solution.ipynb). Các phép thử không bắt buộc phương án cải tiến phải thắng baseline.
