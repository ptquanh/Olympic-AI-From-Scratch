# Lời giải: Feature Engineering

<details><summary><b>Tầng 1: Understand</b></summary>

Để tránh mô hình học thuộc (Target Leakage), ta có thể sử dụng các kỹ thuật như **K-Fold Target Encoding** (tính trung bình dựa trên k-1 folds, dùng để gán cho fold còn lại) hoặc thêm **Smoothing** (kéo giá trị mã hóa gần về với giá trị trung bình tổng nếu số lượng mẫu của Category đó quá ít). Thư viện `category_encoders` hỗ trợ sẵn điều này.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Label Encoding gán các số 0, 1, 2 cho C (Cherbourg), Q (Queenstown), S (Southampton). Logistic Regression sẽ ngầm định S lớn hơn C, gây ra sai số. One-Hot Encoding biến nó thành 3 cột riêng biệt, giúp Logistic Regression hoạt động đúng bản chất.

</details>
