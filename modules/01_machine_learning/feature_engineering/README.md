# 🛠 Feature Engineering

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Pandas DataFrame cơ bản (điền missing, tính toán cột).

## ② Learning Outcomes

- **Implement:** Biết cách dùng One-Hot Encoding và Label Encoding cho biến phân loại.
- **Implement:** Biết cách tạo feature mới (vd: Tuổi = Năm nay - Năm sinh).
- **Diagnose:** Tránh được Data Leakage (dùng thông tin test để xử lý train).

## ③ Concept Map

`Tree Ensembles` → **`Feature Engineering`** → `Hyperparameter Tuning`

## ④ Intuition

Nếu dữ liệu là rác, mô hình học máy (dù là thuật toán xịn nhất) cũng chỉ cho ra kết quả rác ("Garbage In, Garbage Out"). Feature Engineering là nghệ thuật biến đổi dữ liệu thành dạng mô hình dễ học nhất.

## ⑧ Framework / Lab

Xem `lab.ipynb`

## ⑩ Misconceptions

- ❌ **Sai:** Thuật toán AI càng mạnh thì không cần Feature Engineering.
- ✅ **Đúng:** Tree-based models và Neural Networks có khả năng tự trích xuất đặc trưng, nhưng cung cấp đặc trưng rõ ràng ngay từ đầu sẽ giúp mô hình hội tụ nhanh hơn và đạt đỉnh cao hơn.

## ⑪ Code Notes

Xem `code_notes.md`

## ⑫ Exercises

Xem `exercises.md`

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
