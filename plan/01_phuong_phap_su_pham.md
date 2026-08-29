# 📐 Phương Pháp Sư Phạm

> [← Quay lại Tổng Quan](00_tong_quan.md)

---

## Learner Journey — Luồng Mỗi Chương

> [!IMPORTANT]
> Đây là trải nghiệm người đọc khi mở một chương. Không phải mọi chương cần mọi bước — nhưng luồng này là thiết kế chuẩn.

```
┌──────────────────────────────────────────────────────────┐
│  ① Prerequisite Check (3-5 câu tự kiểm tra)             │
│  ② Learning Outcomes (có thể quan sát & đo)             │
│  ③ Concept Map (nối với kiến thức trước/sau)             │
│  ④ Intuition (tại sao cần? giải quyết gì?)              │
│  ⑤ Math & Derivation (derive, không chỉ ghi)            │
│  ⑥ Worked Example (hoàn chỉnh, trước khi giao bài)      │
│  ⑦ From-Scratch Implementation                           │
│  ⑧ Framework Implementation (+ so sánh)                  │
│  ⑨ Controlled Experiments (+ observations)               │
│  ⑩ Common Mistakes / Misconception Box                   │
│  ⑪ Code Notes (patterns cần nhớ + bài luyện code tay)   │
│  ⑫ Exercises by Difficulty (5 tầng)                      │
│  ⑬ Olympiad Transfer                                     │
│  ⑭ References & Docs (link chính thức để tự research)   │
│  ⑮ Mastery Checkpoint                                    │
│  ⑯ Time Estimate (cho người đọc, không phải soạn)       │
└──────────────────────────────────────────────────────────┘
```

---

## 3 Loại Chương

### 📘 Core Chapter

**Dùng cho:** Kiến thức nền tảng cần hiểu sâu + từng bước implement from scratch.

**Luồng đầy đủ ①–⑯. Bắt buộc from-scratch.**

```
topic/
├── README.md              # Theory: prerequisite, outcomes, concept map,
│                          #   intuition, math, worked example, misconceptions
├── 01_from_scratch.ipynb  # Zero library imports cho thuật toán đang học
├── 02_framework.ipynb     # Library + compare output/speed
├── 03_experiments.ipynb   # Controlled experiments + observations + "why"
├── code_notes.md          # Code patterns cần nhớ + bài luyện code tay
├── exercises.md           # 5 tầng bài tập
├── solutions.md           # Lời giải kiểm chứng được
├── olympiad_transfer.md   # Chuyển giao sang bài thi
└── references.md          # Docs chính thức + tài liệu tự research
```

**Ví dụ:** Linear Regression, Logistic Regression, Backprop, Convolution, Attention, Transformer, IoU/NMS/AP

### 📗 Concept Lesson

**Dùng cho:** Kiến thức cần biết dùng đúng + debug — không bắt buộc from-scratch.

**Luồng rút gọn: ①②③④⑩⑪⑫⑭⑮⑯.**

```
topic/
├── README.md      # Theory + worked example + misconceptions
├── lab.ipynb      # Demo tương tác
├── code_notes.md  # API patterns cần nhớ (cheat sheet)
├── exercises.md   # Bài tập (ít nhất 3 tầng)
└── references.md  # Docs links + further reading
```

**Ví dụ:** Activations, Metrics, Augmentation, Tokenization, Regularization, Regex, Data Loading

### 📙 Competition Lab

**Dùng cho:** Task-oriented — giải bài thực tế, rèn pipeline.

**Luồng: problem → baseline → improve → postmortem.**

```
topic/
├── README.md        # Problem analysis, approach, metric, validation
├── starter.ipynb    # Bộ khung cho người học tự làm
├── solution.ipynb   # Reference solution
├── code_notes.md    # Pipeline patterns cần nhớ
├── rubric.md        # Tiêu chí chấm: baseline → good → excellent
├── postmortem.md    # Sai ở đâu, học được gì, cải thiện thế nào
└── references.md    # Docs + kaggle + related solutions
```

**Ví dụ:** EDA pipeline, Validation workflow, Image Classification competition, mỗi bài Olympic

---

## Bài Tập Phân Tầng (exercises.md)

Mỗi chương có bài tập chia **5 tầng**:

| Tầng | Tên | Mô tả | Ví dụ |
| --- | --- | --- | --- |
| 1 | **Understand** | Giải thích, derive, dự đoán | "Tại sao QKᵀ có variance tăng theo dk?" |
| 2 | **Implement** | Hoàn thành hoặc sửa code | "Thêm causal mask vào attention" |
| 3 | **Experiment** | Thiết kế thí nghiệm, giải thích kết quả | "Bỏ sqrt(dk), plot softmax — gì xảy ra?" |
| 4 | **Transfer** | Áp dụng vào dữ liệu/bài toán mới | "Dùng attention cho time series" |
| 5 | **Olympiad** | Bài thật hoặc mô phỏng có giới hạn thời gian | "Giải IOAI task X trong 90 phút" |

> [!TIP]
> Concept Lesson chỉ cần tầng 1-3. Competition Lab chỉ cần tầng 3-5.

---

## Olympiad Transfer — Phần Khiến Giáo Trình Này Khác

> [!IMPORTANT]
> Đây không phải "link tới đề thi". Đây là **năng lực chuyển giao** từ kiến thức sang bài thi.

Mỗi Core Chapter cần `olympiad_transfer.md` trả lời:

1. **Nhận diện trong đề** — dấu hiệu nào cho thấy cần dùng kiến thức này?
2. **Baseline tối thiểu** — cái gì nộp nhanh nhất? Mất bao lâu?
3. **Metric & Validation** — đề thường dùng metric gì? K-fold hay hold-out?
4. **Failure modes** — lỗi thường gặp khi áp dụng?
5. **Sau baseline** — bước 1, 2, 3 để tăng điểm?
6. **Phân bổ thời gian 4h/6h** — kế hoạch chi tiết theo giai đoạn

Template đầy đủ: xem [`04_templates.md`](04_templates.md)

---

## Mastery Gates

### Core Chapters — cần pass ít nhất 4/6

| Gate | Cách verify |
|------|-------------|
| 🗣️ **Explain** | Đóng tài liệu, giải thích 5-10 phút |
| ✍️ **Derive** | Viết công thức chính trên giấy trắng |
| 💻 **Re-implement** | Code lại từ notebook trống |
| 🔮 **Predict** | Dự đoán kết quả experiment trước khi chạy |
| 🐛 **Diagnose** | Tìm bug trong implementation cài lỗi |
| 🆕 **Apply** | Giải 1 bài chưa từng thấy dùng concept này |

### Concept Lessons — cần pass ít nhất 2/3

| Gate | Cách verify |
|------|-------------|
| 🗣️ **Explain** | Biết khi nào dùng, khi nào không |
| 🐛 **Debug** | Nhận ra failure modes phổ biến |
| 🆕 **Apply** | Dùng đúng trong pipeline thực tế |

---

## Hai Lộ Trình

### 🟢 Foundation Track

```
Chặng 1: Python + Toán nền tảng → NumPy, Pandas, Regex, Data handling
Chặng 2: ML Core → Linear/Logistic Reg → Metrics → Validation → Trees/SVM
Chặng 3: DL Core → Training Loop → Backprop → CNN → NLP basics
Chặng 4: Advanced → Transformer → Fine-tuning → Transfer Learning
Chặng 5: Competition → Pipeline → Problems → Mocks
```

### 🔴 Contest Track

```
Diagnostic Test → Validation & Baselines → Gap Remediation
→ CV Task Labs → NLP Task Labs → ML Task Labs
→ Past Olympic Problems → Timed Mocks → Failure Remediation
```

### Đánh dấu trong mỗi module

Mỗi module ghi rõ:
- ⭐ **Bắt buộc** — phải học
- 📖 **Nên đọc lướt** — review nhanh
- ⏭️ **Bỏ qua** nếu pass diagnostic
- ⚡ **Nâng cao** — optional
