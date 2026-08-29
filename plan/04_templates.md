# 📝 Templates

> [← Quay lại Tổng Quan](00_tong_quan.md)

Các template dưới đây dùng khi soạn từng chương. Copy và điền.

---

## README.md Template (Core Chapter)

````markdown
# [Tên Topic]

> **Thời gian học ước tính:** X giờ (theory: Xh, code: Xh, exercises: Xh)
> **Loại:** Core Chapter
> **Track:** Foundation ⭐ | Contest 📖

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. [Câu kiểm tra kiến thức nền 1]
2. [Câu kiểm tra kiến thức nền 2]
3. [Câu kiểm tra kiến thức nền 3]

Nếu chưa → quay lại [chương X](link).

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] [Outcome 1 — quan sát được, đo được]
- [ ] [Outcome 2]
- [ ] [Outcome 3]

## Concept Map

```text
[Chương trước] ──→ [CHƯƠNG NÀY] ──→ [Chương sau]
                        │
                        ├── dùng trong [Detection]
                        └── nền tảng cho [Transformer]
```

## 1. Intuition — Tại Sao Cần?

[Giải thích vấn đề mà concept này giải quyết. Không dùng thuật ngữ chưa định nghĩa.]

## 2. Math & Derivation

[Derive, không chỉ ghi. Mỗi bước giải thích "tại sao bước này".]

## 3. Worked Example

[Ví dụ hoàn chỉnh, tính tay được, trước khi giao bài.]

## 4. Shape Analysis

[Kích thước tensor đầu vào/đầu ra, ý nghĩa mỗi chiều.]

## 5. Complexity

[Time/space complexity. Giới hạn thực tế.]

## 6. Common Mistakes & Misconceptions

> ❌ **Sai:** [Cách hiểu sai phổ biến]
> ✅ **Đúng:** [Cách hiểu đúng + tại sao]

## 7. Connections

[Concept này nối với những gì? Tại sao quan trọng cho Olympic?]
````

---

## code_notes.md Template

````markdown
# Code Notes: [Tên Topic]

## 🔑 Core Patterns (Phải nhớ)

### Pattern 1: [Tên — vd: "Gradient Descent Update"]

```python
# Mô tả: [1 dòng]
# Khi nào dùng: [tình huống cụ thể]

def gradient_descent(X, y, lr=0.01, epochs=100):
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(epochs):
        y_pred = X @ w + b
        dw = (2 / len(y)) * X.T @ (y_pred - y)
        db = (2 / len(y)) * np.sum(y_pred - y)
        w -= lr * dw
        b -= lr * db
    return w, b
```

**Ghi nhớ:** `dw = X.T @ error`, `db = sum(error)`, update = `param -= lr * grad`

## 📋 API Cheat Sheet

| Việc cần làm   | Code                                               | Docs                                              |
| -------------- | -------------------------------------------------- | ------------------------------------------------- |
| Tạo DataLoader | `DataLoader(dataset, batch_size=32, shuffle=True)` | [link](https://pytorch.org/docs/stable/data.html) |
| K-Fold split   | `KFold(n_splits=5, shuffle=True, random_state=42)` | [link](https://scikit-learn.org/stable/)          |

## 🏋️ Bài Luyện Code Tay

**Quy tắc:** Đóng tất cả tài liệu. Mở notebook trống. Hẹn giờ.

| #   | Bài                                         | Thời gian | Hint (chỉ xem khi bí)                     |
| --- | ------------------------------------------- | --------- | ----------------------------------------- |
| 1   | Code gradient descent cho linear regression | 15 phút   | `dw = X.T @ error / n`                    |
| 2   | Code training loop PyTorch (không nhìn)     | 10 phút   | `zero → forward → loss → backward → step` |

## 🧠 Flashcards (Hỏi → Trả lời)

| Hỏi                                | Trả lời                             |
| ---------------------------------- | ----------------------------------- |
| Learning rate quá lớn → gì xảy ra? | Loss oscillate hoặc diverge         |
| `model.eval()` làm gì?             | Tắt dropout + BN dùng running stats |
````

---

## references.md Template

```markdown
# References: [Tên Topic]

## 📚 Official Documentation

| Thư viện     | Đọc gì                  | Link                                                                                                   |
| ------------ | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| NumPy        | Broadcasting rules      | [numpy.org/.../broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)               |
| PyTorch      | `nn.Linear`, `autograd` | [pytorch.org/.../nn](https://pytorch.org/docs/stable/nn.html)                                          |
| scikit-learn | `cross_val_score`       | [scikit-learn.org/.../cross_validation](https://scikit-learn.org/stable/modules/cross_validation.html) |

## 📖 Textbook Chapters

| Sách         | Chương | Tại sao đọc             |
| ------------ | ------ | ----------------------- |
| D2L (d2l.ai) | Ch.3   | Derivation chuẩn + code |
| Bishop PRML  | Ch.3.1 | Bayesian perspective    |

## 🎥 Video

| Video                   | Tác giả     | Nên xem khi   |
| ----------------------- | ----------- | ------------- |
| [Neural Networks](link) | 3Blue1Brown | Cần trực giác |
| [Backprop](link)        | Karpathy    | Cần hiểu code |

## 📝 Blog Posts

- [Tên bài](link) — tóm tắt 1 dòng

## 🏆 Competition Resources

- [Kaggle notebook](link) — winning solution
- [aichallenge.ptit.edu.vn](https://aichallenge.ptit.edu.vn) — luyện tập
```

---

## olympiad_transfer.md Template

```markdown
# Olympiad Transfer: [Tên Concept]

## Nhận diện trong đề

Dấu hiệu nào cho thấy nên dùng kiến thức này?

- VD: "Nếu đề nói 'dự đoán nhãn liên tục' → regression"
- VD: "Nếu đề cho ảnh + bbox annotations → detection pipeline"

## Baseline tối thiểu

- Cái gì đơn giản nhất nộp được điểm?
- Mất bao lâu? (ước lượng phút)

## Metric & Validation phù hợp

- Metric đề thường dùng? (accuracy, mAP, F1, RMSE...)
- Validation: k-fold hay hold-out? Stratified?

## Failure modes thường gặp

1. ...
2. ...
3. ...

## Sau baseline, thử gì?

- Bước 1: ...
- Bước 2: ...
- Bước 3 (nếu còn thời gian): ...

## Phân bổ thời gian

### Vòng Sơ loại (4 giờ: 3h Public + 1h Private)

| Giai đoạn    | Thời gian             | Việc |
| ------------ | --------------------- | ---- |
| 0-20 phút    | Đọc đề, EDA nhanh     |
| 20-60 phút   | Baseline chạy được    |
| 60-150 phút  | Improve + experiments |
| 150-180 phút | Nộp Public Test       |
| 180-240 phút | Private Test → nộp    |

### Vòng Chung kết (6 giờ: 5h Public + 1h Private)

| Giai đoạn    | Thời gian              | Việc |
| ------------ | ---------------------- | ---- |
| 0-30 phút    | Đọc đề, EDA            |
| 30-90 phút   | Baseline pipeline      |
| 90-200 phút  | Improve model          |
| 200-300 phút | Experiments + ensemble |
| 300-320 phút | Cleanup + nộp Public   |
| 320-360 phút | Private Test → FINAL   |

## Bài thi thực tế liên quan

| Bài | Nguồn            | Concept chính | Difficulty |
| --- | ---------------- | ------------- | ---------- |
| ... | IOAI 2025        | ...           | ⭐⭐⭐     |
| ... | OlpAI SV         | ...           | ⭐⭐       |
| ... | aichallenge.ptit | ...           | ⭐⭐       |
```
