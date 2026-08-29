# Lời giải: Document AI

<details><summary><b>Tầng 1: Understand</b></summary>
Việc trích xuất text thuần (BERT) làm mất đi toạ độ 2D của chữ. Trong hóa đơn, chữ "Total" và con số "100$" có ý nghĩa vì chúng nằm ngang hàng nhau (hoặc gần nhau) trên ảnh, dù theo trình tự text tuyến tính chúng có thể bị đọc cách xa nhau. LayoutLM học vector dựa trên cả nội dung chữ VÀ tọa độ Bounding Box (x, y) của chữ đó.
</details>

<details><summary><b>Tầng 2: Implement</b></summary>
Tùy vào ảnh của bạn, code mẫu như trong `code_notes.md`.
</details>
