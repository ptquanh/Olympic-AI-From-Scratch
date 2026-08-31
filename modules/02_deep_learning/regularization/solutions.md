# Lời giải: Regularization

<details><summary><b>U-1 — Understand</b></summary>
1. BatchNorm đưa dữ liệu sau mỗi tầng về lại trạng thái chuẩn (mean=0, std=1), giúp mô hình ổn định, cho phép dùng Learning Rate to hơn để hội tụ cực nhanh.
2. KHÔNG. Khi gọi `model.eval()`, Dropout ngừng vô hiệu hóa nơ-ron (100% nơ-ron được giữ lại). Tuy nhiên, vì lúc Train chỉ có p% nơ-ron hoạt động, tổng độ lớn tín hiệu truyền đi bị giảm đi. Để cân bằng, PyTorch tự động nhân (scale) các trọng số lên theo tỷ lệ $1/(1-p)$ trong quá trình huấn luyện, nên lúc Test/Eval không cần tính toán bù trừ gì thêm.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
best_loss = float('inf')
patience = 5
patience_counter = 0

for epoch in range(100):
    # ... code train ...
    val_loss = 0.5 # Ví dụ lấy được val_loss = validate(model, val_loader)

    if val_loss < best_loss:
        best_loss = val_loss
        patience_counter = 0 # Reset
        # torch.save(model.state_dict(), 'best_model.pth')
    else:
        patience_counter += 1

    if patience_counter >= patience:
        print("Early Stopped!")
        break

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>
Khi không có weight decay, trọng số có thể phình to vô hạn để "học vẹt" (memorize) dữ liệu, biểu đồ phân phối trải rất rộng (từ âm vài trăm đến dương vài trăm). Khi thêm weight decay=0.1, toàn bộ các trọng số bị ép mạnh về rất sát giá trị 0. Biểu đồ tập trung dày đặc quanh số 0. Mạng bị "bóp" lại, do đó mất khả năng học vẹt và chống Overfitting rất tốt.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
