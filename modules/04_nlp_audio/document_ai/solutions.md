# Lời giải: Document AI

<details><summary><b>U-1 — Understand</b></summary>

OCR text thuần làm mất vị trí 2D và có thể làm sai reading order. Trên hóa đơn, “Total” liên kết với số cùng dòng/cột; hai token có thể xa nhau trong chuỗi OCR. Text-only vẫn hợp lý cho trang một cột có thứ tự đọc ổn định hoặc khi task chỉ cần keyword không phụ thuộc layout.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
def normalize_box(box, width, height):
    x1,y1,x2,y2 = box
    if width <= 0 or height <= 0 or x2 < x1 or y2 < y1:
        raise ValueError("invalid page or box")
    values = [1000*x1/width, 1000*y1/height, 1000*x2/width, 1000*y2/height]
    return [int(round(min(1000,max(0,v)))) for v in values]

```

Test yêu cầu trả `[100,100,500,300]`.

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Định nghĩa trước “cùng dòng” bằng overlap theo y và khoảng cách x tối đa. Áp cùng rule cho clean/shifted; báo số pair đúng/tổng pair. Nếu chỉ nhìn OCR text sẽ không phát hiện lỗi tọa độ, nên error analysis phải tách token accuracy và layout-pair accuracy.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
