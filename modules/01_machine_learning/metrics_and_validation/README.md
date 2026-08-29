# 📏 Metrics & Validation (Đánh giá và Thẩm định mô hình)

> **Track:** Foundation ⭐ | Contest ⭐

## ① Prerequisite Check

- Bạn có biết tại sao không nên dùng tập Training để đánh giá mô hình không?
- Trong bài toán chuẩn đoán ung thư (99% Khỏe, 1% Bệnh), nếu mô hình đoán tất cả là Khỏe thì Accuracy là bao nhiêu? Mô hình đó có tốt không?

## ② Learning Outcomes

- **Derive:** Tự code tay Accuracy, Precision, Recall, F1-Score từ Confusion Matrix.
- **Implement:** Dùng K-Fold Cross Validation để đánh giá khách quan.
- **Explain:** Giải thích được ý nghĩa của ROC/AUC và khi nào thì dùng F1 thay vì Accuracy.

## ③ Concept Map

`Logistic Regression` → **`Metrics & Validation`** → `Feature Engineering` / `Pipeline`

## ④ Intuition (Trực giác)

Nếu bạn học bài (Training Data) và đi thi bằng đúng bộ đề cương đã học, việc bạn được 10 điểm (Accuracy 100%) không chứng minh được bạn giỏi. Bạn chỉ đang "học vẹt" (Overfitting).
Để biết bạn có thực sự giỏi, đề thi phải là những bài bạn chưa từng thấy bao giờ (Test Data).
Hơn nữa, nếu đề thi có 99 câu dễ và 1 câu khó, bạn làm đúng 99 câu dễ (Accuracy 99%) nhưng bỏ câu khó. Nếu câu khó đó là "Tìm ra bệnh nhân ung thư", thì điểm 99% của bạn là vô nghĩa. Ta cần các thước đo khác như Precision, Recall, F1.

## ⑤ Math / Derivation

**Confusion Matrix (Ma trận nhầm lẫn):**

- **TP (True Positive):** Đoán Bệnh, Thật là Bệnh (Đúng).
- **TN (True Negative):** Đoán Khỏe, Thật là Khỏe (Đúng).
- **FP (False Positive):** Đoán Bệnh, Thật là Khỏe (Đoán nhầm, Báo động giả).
- **FN (False Negative):** Đoán Khỏe, Thật là Bệnh (Bỏ sót bệnh nhân - Cực kỳ nguy hiểm).

**Công thức:**

- `Accuracy` = (TP + TN) / Tổng
- `Precision` = TP / (TP + FP) -> Trong số những ca báo Bệnh, bao nhiêu ca thật sự Bệnh?
- `Recall` = TP / (TP + FN) -> Trong số những ca thật sự Bệnh, tìm ra được bao nhiêu ca?
- `F1-Score` = 2 _ (Precision _ Recall) / (Precision + Recall) -> Trung bình điều hòa.

## ⑥ Worked Example

Có 10 bệnh nhân (2 Bệnh, 8 Khỏe). Mô hình đoán 3 người Bệnh (trong đó trúng 1, sai 2).

- TP = 1
- FN = 1 (1 người bệnh bị bỏ sót)
- FP = 2 (2 người khỏe bị chẩn đoán nhầm)
- TN = 6 (6 người khỏe chẩn đoán đúng)
  `Accuracy` = (1+6)/10 = 70%.
  `Precision` = 1 / (1+2) = 33.3% (Báo động giả rất nhiều).
  `Recall` = 1 / (1+1) = 50% (Bỏ sót một nửa số bệnh nhân).
  `F1-Score` = 2 _ (0.33 _ 0.5) / (0.33 + 0.5) = 0.4. (Một con số tệ, phản ánh đúng chất lượng mô hình).

## ⑦ From-Scratch

Xem `01_from_scratch.ipynb`

## ⑧ Framework

Xem `02_framework.ipynb`

## ⑨ Experiments

Xem `03_experiments.ipynb`

## ⑩ Misconceptions

- ❌ **Sai:** Train xong cắt 20% ra làm Test set là đủ an toàn rồi.
- ✅ **Đúng:** Nếu bạn lấy 20% đó ra thử nghiệm và tinh chỉnh mô hình nhiều lần, 20% đó không còn là Test set khách quan nữa (Information Leakage). Cần dùng Train/Validation/Test hoặc K-Fold Cross Validation.
- ❌ **Sai:** ROC/AUC được tính dựa trên số lượng class 0 và 1 dự đoán ra.
- ✅ **Đúng:** ROC/AUC bắt buộc phải tính dựa trên **xác suất** (probability). Nó đánh giá xem mô hình xếp hạng (ranking) các mẫu có tốt không ở mọi ngưỡng threshold.

## ⑪ Code Notes

Xem `code_notes.md`

## ⑫ Exercises

Xem `exercises.md`

## ⑬ Olympiad Transfer

Xem `olympiad_transfer.md`

## ⑭ References

Xem `references.md`

## ⑮ Mastery Check

- Làm sao để ngăn chặn Data Leakage khi làm Cross Validation kết hợp với Data Scaling? (Gợi ý: Dùng `Pipeline`).
- Nếu bài toán yêu cầu "Không được bỏ sót bệnh nhân nào dù có chẩn đoán nhầm người khỏe", bạn sẽ ưu tiên tối ưu Precision hay Recall?

## ⑯ Time Estimate

Theory: ~1h, Code: ~1.5h, Exercises: ~1h
