# Lời giải: Tree Ensembles

<details><summary><b>Tầng 1: Understand</b></summary>

Vì logic là IF-ELSE (vd: `income > 1000`), nếu ta nhân toàn bộ biến `income` lên 1,000,000 lần thì điều kiện cũng tự động biến đổi thành `income > 1000000000`. Cấu trúc nhánh cây không hề thay đổi, tính chất phân rã của cây chỉ phụ thuộc vào THỨ TỰ (thứ hạng) của dữ liệu chứ không phụ thuộc vào độ lớn tuyến tính.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

Thường thì `LGBMClassifier` sẽ chạy nhanh hơn rất nhiều (gấp 3-10 lần tùy dữ liệu) so với `RandomForestClassifier` nhờ vào cơ chế xây dựng cây theo Histogram và theo lá (leaf-wise).

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Khi chạy 1000 cây trên 100 mẫu với `max_depth=15`, độ chính xác trên tập Train sẽ là 100% nhưng tập Test sẽ rất thấp -> Mô hình đã bị Overfitting nặng.
Khi giảm `max_depth=3`, mô hình bớt phức tạp hơn và có khả năng khái quát tốt hơn trên tập Test.

</details>
