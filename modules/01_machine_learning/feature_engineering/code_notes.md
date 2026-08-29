# Code Notes: Feature Engineering

## 🔑 Core Patterns

### Pattern 1: Target Encoding cơ bản

```python
# Tính trung bình nhãn Y theo từng nhóm X
target_mean = df_train.groupby('category_col')['target'].mean()
df_train['category_col_encoded'] = df_train['category_col'].map(target_mean)
df_test['category_col_encoded'] = df_test['category_col'].map(target_mean) # Dùng MAP của TRAIN
```

**Ghi nhớ:** KHÔNG ĐƯỢC tính `target_mean` trên tập Test, phải lấy dictionary từ Train map sang Test (tránh Leakage).

### Pattern 2: One-Hot Encoding với Pandas

```python
import pandas as pd
df = pd.get_dummies(df, columns=['Color', 'Size'])
```

## 📋 API Cheat Sheet

| Việc cần làm          | Code                                  | Link Docs                                                                               |
| --------------------- | ------------------------------------- | --------------------------------------------------------------------------------------- |
| Chuyển kiểu datetime  | `pd.to_datetime(df['Date'])`          | [pandas datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) |
| Lấy tháng từ cột date | `df['Date'].dt.month`                 | [dt accessor](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html)       |
| One-Hot Encoding      | `pd.get_dummies(df, columns=['col'])` | [get_dummies](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)     |

## 🏋️ Bài Luyện Code Tay

Đóng tài liệu, mở notebook trống, hẹn giờ.

| #   | Bài                                                                        | Thời gian | Hint (ẩn)                                          |
| --- | -------------------------------------------------------------------------- | --------- | -------------------------------------------------- |
| 1   | Viết đoạn code điền giá trị thiếu (NA) bằng giá trị trung bình của cột đó. | 2 phút    | `df['col'].fillna(df['col'].mean(), inplace=True)` |
| 2   | Viết code thực hiện One-Hot Encoding cho cột 'City'.                       | 2 phút    | `pd.get_dummies(df, columns=['City'])`             |

## 🧠 Flashcards

| Hỏi                                                         | Trả lời                                                                                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Khi nào dùng Label Encoding, khi nào dùng One-Hot Encoding? | Dùng Label cho biến có tính thứ tự (Cao, Trung bình, Thấp). Dùng One-hot cho biến không có tính thứ tự (Màu đỏ, Màu xanh). |
| Data Leakage trong Target Encoding là gì?                   | Tính toán target encoding dựa trên nhãn của cả tập Validation/Test thay vì chỉ tập Train.                                  |
