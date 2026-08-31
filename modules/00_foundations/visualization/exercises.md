# Exercises: Visualization

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

**1. Chọn Plot Đúng**
Bạn có các yêu cầu phân tích dữ liệu sau. Hãy đề xuất loại biểu đồ phù hợp nhất:
a) Xem tỷ lệ phần trăm dân số của 3 miền Bắc, Trung, Nam.
b) Xem mối liên hệ giữa Số giờ tự học và Điểm thi cuối kỳ.
c) Xem sự biến động giá cổ phiếu Vinamilk trong năm qua.
d) Kiểm tra xem cột `Lương_tháng` có bị lệch phải (right-skewed) không.

**2. Giải thích lỗi hiển thị**
Đoạn code sau cố gắng vẽ 2 đường lên cùng một hình, nhưng khi chạy không thấy bảng chú thích (legend) đâu cả, mặc dù đã gọi `ax.legend()`. Tại sao? Sửa như thế nào?

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 20, 10])
ax.plot([1, 2, 3], [5, 15, 25])
ax.legend()
plt.show()

```

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

**1. Vẽ đường Training và Validation Loss**
Cho 2 list dữ liệu ghi nhận sai số sau 10 Epochs:

`train_loss = [0.9, 0.7, 0.5, 0.4, 0.35, 0.3, 0.28, 0.25, 0.22, 0.2]`

`val_loss =   [0.9, 0.75, 0.6, 0.55, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]`
Hãy vẽ 2 đường này lên **cùng một đồ thị**.
Yêu cầu bắt buộc:

- Train có màu xanh dương (blue), nhãn "Train Loss".
- Validation có màu cam (orange) hoặc đỏ (red), nét đứt, nhãn "Val Loss".
- Trục X là "Epochs" (từ 1 đến 10), trục Y là "Loss".
- Có Title là "Learning Curve".

Bạn nhận xét gì về hiện tượng xảy ra từ Epoch thứ 5 trở đi?

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

**Trực quan hóa nhiễu**

1. Dùng NumPy tạo một mảng `x` gồm 100 điểm từ 0 đến 10.
2. Tạo mảng `y_true = 2 * x + 1`.
3. Tạo mảng `y_noisy = y_true + np.random.normal(0, 2, size=100)`.
4. Vẽ `x` và `y_noisy` dưới dạng Scatter plot (điểm).
5. Vẽ đè `x` và `y_true` dưới dạng Line plot (đường thẳng màu đỏ, nét liền dày) lên cùng một biểu đồ.

Đây là một trực quan hóa kinh điển mô tả dữ liệu thật (nhiễu) và đường dự đoán lý tưởng (mô hình).

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
