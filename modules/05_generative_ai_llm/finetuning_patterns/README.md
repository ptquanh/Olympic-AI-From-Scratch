# Fine-tuning Patterns: LoRA & PEFT

> **Thời gian học ước tính:** 4 giờ (theory: 1.5h, code: 1.5h, exercises: 1h)
> **Loại:** Core Chapter
> **Track:** Foundation ⚡ | Contest ⭐

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Matrix multiplication: Khi nhân ma trận (m x r) với ma trận (r x n), kết quả có kích thước bao nhiêu?
2. Pre-trained weights là gì và tại sao ta thường "đóng băng" (freeze) chúng?
3. Gradient descent cập nhật trọng số như thế nào dựa trên loss?

Nếu chưa → quay lại Linear Regression, Backpropagation (Module 02) và CNN Architectures (Module 03).

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Giải thích được nguyên lý toán học của Low-Rank Adaptation (LoRA).
- [ ] Implement một custom LoRA layer từ con số 0 bằng PyTorch.
- [ ] Cấu hình và sử dụng thư viện `peft` của HuggingFace để fine-tune LLM.

## Concept Map

```text
[Prompt Engineering] --> [FINE-TUNING PATTERNS] --> [Multimodal]
                              │
                              └── ứng dụng trong [Text/Audio/Vision Classification]

```

## 1. Intuition — Tại Sao Cần PEFT/LoRA?

Các mô hình ngôn ngữ lớn (LLM) hiện nay có từ hàng tỷ đến hàng trăm tỷ tham số.

- **Vấn đề:** Nếu dùng Full Fine-tuning (cập nhật toàn bộ tham số), ta cần rất nhiều VRAM (có khi cần cụm GPU A100).
- **Giải pháp:** Parameter-Efficient Fine-Tuning (PEFT). Thay vì huấn luyện tất cả, ta chỉ huấn luyện một phần rất nhỏ tham số, hoặc thêm vào một số tham số mới, trong khi vẫn "đóng băng" (freeze) mô hình gốc.

**LoRA (Low-Rank Adaptation)** là phương pháp PEFT phổ biến nhất hiện nay.

## 2. Math & Derivation: Nguyên lý LoRA

Giả sử trong kiến trúc Transformer có một lớp Linear layer: $h = W_0 x$
Trong đó $W_0 \in \mathbb{R}^{d \times k}$ là trọng số gốc (pre-trained).

Khi fine-tuning, trọng số sẽ được cập nhật một lượng $\Delta W$:
$$ h = (W_0 + \Delta W)x = W_0 x + \Delta W x $$

**Ý tưởng của LoRA:** Thay vì học toàn bộ ma trận $\Delta W$ (rất lớn), ta phân rã (decompose) $\Delta W$ thành tích của 2 ma trận nhỏ hơn:
$$ \Delta W = B A $$
Trong đó:

- $B \in \mathbb{R}^{d \times r}$
- $A \in \mathbb{R}^{r \times k}$
- $r \ll \min(d, k)$ gọi là **Rank** (thường r = 8, 16, 32).

Lúc này layer trở thành:
$$ h = W_0 x + BA x $$

**Khởi tạo:**

- Ma trận $A$ được khởi tạo ngẫu nhiên (thường dùng phân phối chuẩn).
- Ma trận $B$ được khởi tạo bằng 0.
  $\Rightarrow$ Tại bước đầu tiên, $\Delta W = BA = 0$, nghĩa là đầu ra ban đầu hoàn toàn giống với pre-trained model.

## 3. Shape Analysis

- Đầu vào $x$: `(batch, seq, k)`
- Trọng số gốc $W_0$: `(d, k)`
- $A$: `(r, k)`
- $B$: `(d, r)`
- Số tham số của $W_0$: $d \times k$.
- Số tham số cần huấn luyện trong LoRA: $r \times k + d \times r = r(k + d)$.
- **Ví dụ:** $d=4096, k=4096, r=8$.
  - Full: $4096 \times 4096 = 16.7$ triệu tham số.
  - LoRA: $8 \times 4096 + 4096 \times 8 = 65.5$ ngàn tham số.
    $\Rightarrow$ Giảm hàng trăm lần!

## 4. Worked Example: LoRA Update

Giả sử $k = 4, d = 4$. Layer gốc $W_0$:
$$ W_0 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

Chọn rank $r=1$.
Ma trận $A \in \mathbb{R}^{1 \times 4}$, khởi tạo ngẫu nhiên: $A = [0.1, 0.2, 0.1, 0.2]$.
Ma trận $B \in \mathbb{R}^{4 \times 1}$, khởi tạo zero: $B = [0, 0, 0, 0]^T$.

Tại bước feed-forward đầu tiên với input $x = [1, 1, 1, 1]^T$:

- $W_0 x = [1, 1, 1, 1]^T$
- $Ax = 0.6$
- $B(Ax) = [0, 0, 0, 0]^T$
- Tổng: $[1, 1, 1, 1]^T$.
  Đầu ra không bị ảnh hưởng. Sau khi loss đi ngược lại qua Backprop, $B$ và $A$ sẽ được cập nhật.

## 5. Common Mistakes & Misconceptions

> ❌ **Sai:** LoRA luôn làm inference chậm.
> ✅ **Đúng:** Có thể merge update vào base weight khi dtype/quantization và deployment cho phép. Nếu giữ adapter tách rời hoặc base quantized, overhead và khả năng merge phụ thuộc implementation.

> ❌ **Sai:** LoRA chỉ dùng cho LLM (Text).
> ✅ **Đúng:** LoRA có thể dùng cho mọi mạng Neural có layer Linear/Conv2d (như Vision Transformers, Diffusion Models, Audio encoders).

## ⑯ Time Estimate

Theory: ~2h · Code: ~2h · Exercises: ~1.5h
