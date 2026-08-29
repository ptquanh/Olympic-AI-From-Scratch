# Lời giải: Regularization

<details><summary><b>Tầng 1: Understand</b></summary>
Dữ liệu truyền qua các tầng nơ ron sâu thường bị xô lệch (Internal Covariate Shift). BatchNorm đưa dữ liệu sau mỗi tầng về lại trạng thái chuẩn (mean=0, std=1), giúp mô hình ổn định, cho phép dùng Learning Rate to hơn để hội tụ cực nhanh.
</details>
<details><summary><b>Tầng 2: Implement</b></summary>

```python
best_loss = float('inf')
patience = 5
patience_counter = 0

for epoch in range(100):
    # ... code train ...

    val_loss = validate(model, val_loader)

    if val_loss < best_loss:
        best_loss = val_loss
        patience_counter = 0 # Reset
        torch.save(model.state_dict(), 'best_model.pth')
    else:
        patience_counter += 1

    if patience_counter >= patience:
        print("Early Stopped!")
        break
```

</details>
