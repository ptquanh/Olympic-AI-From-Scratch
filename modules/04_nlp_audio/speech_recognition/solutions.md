# Lời giải: Speech Recognition

<details><summary><b>U-1 — Understand</b></summary>

Reference có năm từ và hypothesis thiếu “mua”: `D=1`, `S=I=0`, nên `WER=(S+D+I)/N=1/5=0.2`.

**Lỗi thường gặp:** nhắc lại định nghĩa nhưng không nêu giả định hoặc không kiểm tra được kết luận.

</details>

<details><summary><b>I-1 — Implement</b></summary>

```python
def distance(a, b):
    previous = list(range(len(b)+1))
    for i, x in enumerate(a, 1):
        current = [i]
        for j, y in enumerate(b, 1):
            current.append(min(current[-1]+1, previous[j]+1,
                               previous[j-1] + (x != y)))
        previous = current
    return previous[-1]

def wer(reference, hypothesis):
    ref, hyp = reference.split(), hypothesis.split()
    if not ref:
        raise ValueError("empty reference")
    return distance(ref, hyp) / len(ref)

```

**Lỗi thường gặp:** copy code mà không assert input, output, shape và edge case.

</details>

<details><summary><b>E-1 — Experiment</b></summary>

Áp cùng một normalization function cho cả reference và hypothesis, lưu transcript sau chuẩn hóa và tính corpus-level edits/words. Không chọn normalization bằng private test; policy phải theo đề hoặc được khóa bằng validation trước khi chấm test.

**Lỗi thường gặp:** đổi nhiều biến cùng lúc, không cố định seed/split hoặc chỉ báo một lần chạy thuận lợi.

</details>
