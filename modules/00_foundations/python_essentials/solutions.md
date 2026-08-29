# Lời giải: Python Essentials

<details><summary><b>Tầng 1: Understand</b></summary>

Vì List trong Python là kiểu dữ liệu tham chiếu (Reference). Khi thực hiện `b = a`, `a` và `b` cùng trỏ đến một vùng nhớ. Khi đổi `b[0]`, vùng nhớ thay đổi nên `a[0]` cũng thay đổi theo. Cách khắc phục: `b = a.copy()`.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
[x for x in lst if x % 2 == 0 and x % 3 == 0]
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

`Exception` là lớp cha của mọi lỗi trong Python. Nếu ta `except Exception as e:` trước `except ValueError:`, Python sẽ bắt lỗi ở khối `Exception` ngay lập tức và bỏ qua `ValueError`. Thứ tự đúng là bắt từ lỗi cụ thể nhất (nhỏ nhất) lên lỗi chung chung nhất (to nhất).

</details>
