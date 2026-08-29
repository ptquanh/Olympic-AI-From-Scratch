# Lời giải: Embeddings

<details><summary><b>Tầng 1: Understand</b></summary>
Về mặt Toán học, đưa One-hot vector kích thước 50,000 vào `nn.Linear(50000, 256)` (tức là nhân ma trận $[1 \times 50000] \cdot [50000 \times 256]$) SẼ CHO RA KẾT QUẢ Y HỆT như việc "bốc" hàng thứ $i$ trong `nn.Embedding(50000, 256)`. Tuy nhiên, về mặt Máy tính (Computer Science), nhân ma trận khổng lồ chứa 49,999 số 0 là vô cùng tốn CPU/GPU và RAM. `nn.Embedding` đơn giản chỉ là Lookup Table (trỏ tới ô nhớ và lấy ra) nên cực kỳ nhanh.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>
(1*1.1 + 2*1.9 + 3*3.2) / (sqrt(14) * sqrt(15.06)) = 14.5 / (3.74 * 3.88) = 0.999. Rất gần 1.
</details>

<details><summary><b>Tầng 3: Experiment</b></summary>
Nó sẽ gần 0 (trực giao). Trong không gian chiều cao (100 chiều), hai vector khởi tạo ngẫu nhiên (Gaussian) hầu như luôn luôn vuông góc với nhau (độ tương đồng = 0).
</details>
