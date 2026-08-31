# SVM & KNN

> **Track:** Foundation 📖 | Contest ⏭️ nếu pass diagnostic

## ① Prerequisite Check

1. Bạn có giải thích được tại sao feature scale làm thay đổi Euclidean distance?
2. Bạn có phân biệt train/validation/test và chỉ fit scaler trên train?
3. Bạn có đọc được confusion matrix và Macro F1?

Nếu chưa, đọc lại NumPy/Pandas, Feature Engineering và Metrics & Validation.

## ② Learning Outcomes

- Dự đoán nhãn KNN bằng cách tính distance và majority vote trên ví dụ nhỏ.
- Giải thích margin, support vectors và vai trò của `C` trong SVM.
- Chọn scaling, distance/kernel và validation mà không gây leakage.
- Chẩn đoán KNN chậm/nhạy scale và SVM quá khớp do `C`/`gamma`.

## ③ Concept Map

`Scaling + Metrics → [KNN: local neighbors | SVM: maximum margin] → small/medium tabular baseline`

## ④ Intuition

KNN không học công thức tham số: điểm mới nhận nhãn từ các hàng xóm gần nhất. Vì vậy prediction chậm và khái niệm “gần” phụ thuộc trực tiếp vào scale/distance.

Linear SVM tìm một hyperplane không chỉ phân tách mà còn tối đa khoảng cách tới các điểm gần biên nhất. Các điểm này là support vectors; phần lớn điểm xa biên không quyết định nghiệm. Soft margin cho phép vi phạm để cân bằng margin rộng và training error.

## ⑤ Math & Worked Example

Với KNN, Euclidean distance là `d(x,z)=sqrt(sum_j (x_j-z_j)^2)`. Nếu một feature nằm trong `[0,1]` còn feature khác trong `[0,100000]`, feature thứ hai gần như quyết định toàn bộ distance.

SVM tuyến tính tối thiểu hóa dạng regularized hinge loss:

`1/2 ||w||² + C Σ max(0, 1 - y_i(wᵀx_i+b))`.

`C` lớn phạt vi phạm mạnh hơn nhưng không đồng nghĩa luôn tổng quát hóa tốt hơn. Với ba điểm train `(0,0)→0`, `(1,0)→0`, `(0,2)→1`, điểm `(0,1.5)` gần điểm lớp 1 nhất với `k=1`; khi `k=3`, majority lại là lớp 0. Đây là bias–variance trade-off của `k`.

## ⑧ Framework / Lab

`lab.ipynb` so sánh `KNeighborsClassifier` và `SVC` trên cùng split. Đặt scaler và model trong `Pipeline` để mỗi fold chỉ học thống kê từ training fold.

## ⑩ Misconceptions

- ❌ **Sai:** KNN không train nên không thể overfit. → ✅ `k=1` có variance cao và ghi nhớ noise.
- ❌ **Sai:** SVM luôn cần kernel RBF. → ✅ Linear SVM thường mạnh với dữ liệu sparse/high-dimensional.
- ❌ **Sai:** Scale toàn bộ dữ liệu trước cross-validation là vô hại. → ✅ Đó là leakage.

## ⑮ Mastery Check

Bạn đạt bài khi giải thích được ảnh hưởng của scale, chọn được `k/C/gamma` bằng validation và chỉ ra vì sao KNN không phù hợp dataset inference rất lớn.

## ⑯ Time Estimate

Theory: ~1h · Code: ~1h · Exercises: ~1h
