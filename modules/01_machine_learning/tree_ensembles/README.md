# 🌲 Tree Ensembles (Rừng cây và Boosting)

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Bạn có biết làm thế nào để chơi trò "Ai là triệu phú" với quyền trợ giúp 50/50?
- Cấu trúc dữ liệu Cây (Tree) là gì?

## ② Learning Outcomes

- **Explain:** Hiểu được sự khác biệt giữa Bagging (Random Forest) và Boosting (XGBoost, LightGBM).
- **Implement:** Dùng LightGBM và XGBoost để train dữ liệu dạng bảng (Tabular Data).
- **Diagnose:** Nhận biết được khi nào Tree model bị Overfitting và cách chỉnh tham số để sửa lỗi.

## ③ Concept Map

`Logistic Regression` → **`Tree Ensembles`** → `Feature Engineering`

## ④ Intuition (Trực giác)

Nếu chỉ có 1 người đoán (Decision Tree), quyết định có thể rất sai lệch.

- **Random Forest (Bagging):** Mời 100 người đoán ngẫu nhiên. Lấy kết quả bầu chọn nhiều nhất. Sức mạnh tập thể giúp giảm sai số.
- **Boosting (XGBoost):** Người thứ 1 làm bài thi, sai 3 câu. Người thứ 2 tập trung học đúng 3 câu sai đó rồi làm lại. Người thứ 3 học cái sai của người 2. Cứ thế, mô hình đằng sau sẽ sửa lỗi cho mô hình đằng trước. Cuối cùng, tổng hợp lại sẽ có một kết quả hoàn hảo.

## ⑤ Math / Derivation

**(Concept Lesson - Không yêu cầu Code Toán)**
Nhưng cần nắm vững:

- **Decision Tree:** Tách nhánh bằng Gini Impurity hoặc Entropy (cho phân loại) và MSE (cho hồi quy).
- **XGBoost:** Dùng đạo hàm bậc 1 (Gradient) và bậc 2 (Hessian) của hàm Loss để quyết định cách tách nhánh.

## ⑥ Worked Example

Thay vì làm 1 cây Decision Tree khổng lồ sâu 100 tầng (chắc chắn overfit vì nó nhớ từng data point), ta làm 100 cây nhỏ sâu 5 tầng. Trọng số của các cây sẽ được cộng gộp (Boosting). Tốc độ train sẽ lâu hơn nhưng độ chính xác cực cao.

## ⑧ Framework / Lab

Xem `lab.ipynb`

## ⑩ Misconceptions

- ❌ **Sai:** XGBoost luôn tốt hơn Random Forest.
- ✅ **Đúng:** XGBoost mạnh hơn nhưng rất dễ Overfitting nếu chỉnh tham số không khéo. Random Forest gần như không thể Overfitting dù bạn cho 1000 cây, rất an toàn để làm Baseline.
- ❌ **Sai:** Tree-based models cần phải Scale dữ liệu (StandardScaler) giống Linear/Logistic Regression.
- ✅ **Đúng:** Không cần! Việc phân tách nhánh `X > 5` không phụ thuộc vào việc 5 hay 500.

## ⑪ Code Notes

Xem `code_notes.md`

## ⑫ Exercises

Xem `exercises.md`

## ⑬ Olympiad Transfer

Trong các cuộc thi Olympic AI và Kaggle, nếu đề bài cho dữ liệu Bảng (Tabular) như Excel (csv), thì **LightGBM và XGBoost là VUA**. Đừng mất thời gian thử Deep Learning cho Tabular data trừ khi bạn còn rất nhiều thời gian. Hãy tập trung dùng LightGBM.

## ⑭ References

Xem `references.md`

## ⑯ Time Estimate

Theory: ~1h, Code: ~1h, Exercises: ~1h
