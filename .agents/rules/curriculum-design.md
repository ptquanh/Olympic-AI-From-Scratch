---
trigger: always_on
---

# Rules: Thiết Kế Giáo Trình Olympic AI From Scratch

> Bộ quy tắc xuyên suốt khi soạn bất kỳ nội dung nào trong giáo trình. ĐỌC VÀ TUÂN THỦ TRƯỚC KHI VIẾT.

---

## R0. Bản Sắc Giáo Trình

### Mục tiêu

Giáo trình AI tiếng Việt, open-source, có thể tái lập, giúp người không biết hoặc biết ít AI nắm vững kiến thức để thi tốt Olympic AI (OlpAI SV, Olympic AI PTIT, VOAI, IOAI, và các kỳ thi quốc tế).

### 4 tiêu chí mọi nội dung phải đạt

1. **Đúng** — công thức, code, kết quả đều kiểm chứng được. Không copy-paste không nguồn.
2. **Dễ học** — prerequisite rõ, learning outcomes đo được, có worked example trước khi giao bài.
3. **Giúp thi tốt** — có olympiad transfer, bài tập chuyển giao, postmortem.
4. **Luyện code tay** — có code_notes.md, bài luyện không nhìn tài liệu, link docs chính thức.

### Ai đọc?

Sinh viên Việt Nam chưa quen tác giả. Viết cho NGƯỜI HỌC, không ghi lại quá trình học của mình.

---

## R1. Phân Loại Chương — Chọn Đúng Archetype

Trước khi soạn bất kỳ chương nào, XÁC ĐỊNH loại chương:

### 📘 Core Chapter (from-scratch bắt buộc)

**Khi nào:** Thuật toán nền tảng cần hiểu sâu, derive, implement từ zero.
**Files:** README.md, 01_from_scratch.ipynb, 02_framework.ipynb, 03_experiments.ipynb, code_notes.md, exercises.md, solutions.md, olympiad_transfer.md, references.md
**Ví dụ:** Linear Regression, Logistic Regression, Backprop, Convolution, Attention, Transformer, IoU/NMS/AP, Fine-tuning patterns

### 📗 Concept Lesson (biết dùng + debug)

**Khi nào:** Kiến thức cần biết dùng đúng, không bắt buộc from-scratch.
**Files:** README.md, lab.ipynb, code_notes.md, exercises.md, solutions.md, references.md
**Ví dụ:** Activations, Metrics, Augmentation, Tokenization, Regex, Optimization, Regularization

### 📙 Competition Lab (task-oriented)

**Khi nào:** Giải bài thực tế, rèn pipeline, bài Olympic.
**Files:** README.md, starter.ipynb, solution.ipynb, code_notes.md, rubric.md, postmortem.md, references.md
**Ví dụ:** EDA pipeline, Image Classification competition, mỗi bài Olympic

> **KHÔNG BAO GIỜ** ép mọi chương vào cùng một bộ file. Chọn archetype PHÙ HỢP.

---

## R2. Learner Journey — Luồng Bắt Buộc

Mỗi README.md phải đi theo luồng (bỏ bước nào thì ghi rõ tại sao):

```
① Prerequisite Check → ② Learning Outcomes → ③ Concept Map
→ ④ Intuition → ⑤ Math/Derivation → ⑥ Worked Example
→ ⑦ From-Scratch → ⑧ Framework → ⑨ Experiments
→ ⑩ Misconceptions → ⑪ Code Notes → ⑫ Exercises
→ ⑬ Olympiad Transfer → ⑭ References → ⑮ Mastery Check → ⑯ Time Estimate

```

### Quy tắc từng bước:

**① Prerequisite Check**

- 3-5 câu hỏi tự kiểm tra. Nếu không trả lời được → link tới chương cần đọc.
- KHÔNG viết "bạn cần biết Python". Viết CỤ THỂ: "Bạn cần giải thích được gradient descent update rule là gì?"

**② Learning Outcomes**

- Dùng động từ quan sát được: "derive", "implement", "predict", "diagnose", "explain".
- SAI: "Hiểu về CNN" → ĐÚNG: "Tự code conv2d forward pass mà không nhìn tài liệu"

**③ Concept Map**

- Vẽ text diagram: chương trước → CHƯƠNG NÀY → chương sau + ứng dụng.
- Giúp người đọc biết đang ở đâu trong hành trình.

**④ Intuition**

- Bắt đầu bằng VẤN ĐỀ, không bắt đầu bằng GIẢI PHÁP.
- SAI: "Attention là cơ chế cho phép..." → ĐÚNG: "Khi dịch câu 'The cat sat on the mat', từ 'sat' cần chú ý đến 'cat' hơn 'mat'. Làm sao để model biết?"
- Không dùng thuật ngữ chưa định nghĩa.

**⑤ Math & Derivation**

- DERIVE, không chỉ ghi công thức cuối.
- Mỗi bước giải thích "tại sao bước này" (không phải chỉ "áp dụng chain rule").
- Ghi rõ ký hiệu trước khi dùng.

**⑥ Worked Example**

- Hoàn chỉnh, tính tay được (số nhỏ). TRƯỚC khi giao bài.
- Bao gồm shape analysis nếu liên quan tensor.

**⑩ Misconceptions**

- Dùng format: ❌ **Sai:** ... → ✅ **Đúng:** ...
- Ít nhất 2-3 misconceptions phổ biến cho Core Chapter.

**⑯ Time Estimate**

- Ghi cho NGƯỜI ĐỌC, không phải thời gian soạn.
- Format: "Theory: ~Xh, Code: ~Xh, Exercises: ~Xh"

---

## R3. Notebook — Quy Tắc Viết Code

### Cell đầu tiên (mọi notebook)

```python
# === Setup ===
# Runtime: ~X phút trên Colab T4
# Hardware: CPU ok / Cần GPU
import random, numpy as np
random.seed(42); np.random.seed(42)
# torch.manual_seed(42) nếu dùng PyTorch

```

### From-scratch notebook (01_from_scratch.ipynb)

- **ZERO library imports** cho thuật toán đang học. Chỉ NumPy + math cơ bản.
- Mỗi function phải có docstring giải thích input/output shape.
- Comment "# WHY:" trước mỗi bước quan trọng.
- Kết thúc bằng cell so sánh output với library reference.

### Framework notebook (02_framework.ipynb)

- Import thư viện chính thức (sklearn, PyTorch, etc.)
- Bắt buộc so sánh kết quả và tốc độ với from-scratch.
- Chỉ dùng thư viện ĐƯỢC PHÉP TRONG THI (xem Cẩm nang Phần 08).

### Experiments notebook (03_experiments.ipynb)

- Mỗi experiment: **Hypothesis → Code → Result → Observation → Why**
- Yêu cầu người đọc DỰ ĐOÁN kết quả trước khi chạy cell.
- Plot phải có title, axis labels, legend. Không plot trần.

### Competition notebooks (starter/solution)

- Cấu trúc theo pipeline: Data → EDA → Preprocess → Model → Train → Evaluate → Submit
- starter.ipynb: có TODO comments, hướng dẫn rõ, code skeleton.
- solution.ipynb: reference hoàn chỉnh, giải thích lựa chọn.

### Quy tắc chung

- Không dùng đường dẫn tuyệt đối.
- Không commit data >10MB, checkpoints, model weights.
- Ghi `# Cẩm nang P08:` khi dùng thư viện đặc biệt để confirm nó được phép.

---

## R4. Code Notes — Luyện Code Tay

Mỗi chương phải có `code_notes.md` gồm:

### 🔑 Core Patterns

- Đoạn code ngắn gọn, chạy được, pattern cốt lõi phải nhớ.
- Dưới mỗi pattern: dòng **"Ghi nhớ:"** tóm 1 câu.

### 📋 API Cheat Sheet

- Bảng: `Việc cần làm | Code | Link Docs`
- Docs link phải trỏ đến ĐÚNG trang/function, không link trang chủ chung.

### 🏋️ Bài Luyện Code Tay

- Quy tắc: đóng tài liệu, mở notebook trống, hẹn giờ.
- Bảng: `# | Bài | Thời gian | Hint (ẩn)`
- Ít nhất 3 bài cho Core Chapter, 2 bài cho Concept Lesson.

### 🧠 Flashcards

- Bảng `Hỏi | Trả lời` — câu hỏi ngắn, trả lời 1-2 dòng.
- Ưu tiên câu hỏi về "tại sao" và "khi nào", không chỉ "cái gì".

---

## R5. References — Link Docs Rõ Ràng

Mỗi chương phải có `references.md` gồm:

1. **📚 Official Docs** — bảng: `Thư viện | Đọc gì | Link trực tiếp`
   - Link TRỰC TIẾP đến trang/function cần đọc, không link trang chủ.
2. **📖 Textbook Chapters** — sách + chương cụ thể + tại sao đọc.
3. **🎥 Video** — video hay nhất cho concept này + "nên xem khi nào".
4. **📝 Blog/Tutorial** — tóm tắt 1 dòng.
5. **🏆 Competition Resources** — Kaggle notebooks, aichallenge.ptit.edu.vn.

> **CHỈ dùng thư viện ĐƯỢC PHÉP TRONG THI** (Cẩm nang Phần 08). Không dạy thư viện ngoài danh sách trong phần competition-safe.

Nội dung học mở rộng có thể dùng thư viện khác nếu tách profile, khai báo dependency/license/network và ghi rõ không được giả định có trong phòng thi.

---

## R6. Exercises — 5 Tầng Bắt Buộc

| Tầng | Tên            | Core Chapter | Concept Lesson | Competition Lab |
| ---- | -------------- | ------------ | -------------- | --------------- |
| 1    | **Understand** | ✅           | ✅             | —               |
| 2    | **Implement**  | ✅           | ✅             | —               |
| 3    | **Experiment** | ✅           | ✅             | ✅              |
| 4    | **Transfer**   | ✅           | —              | ✅              |
| 5    | **Olympiad**   | ✅           | —              | ✅              |

Quy tắc:

- Mỗi bài tập phải có **output kỳ vọng rõ ràng** (đáp số, khoảng giá trị, hoặc hành vi).
- Tầng 5 (Olympiad) phải ghi rõ thời gian giới hạn.
- Solutions.md dùng `<details><summary>` để ẩn lời giải.

---

## R7. Olympiad Transfer — Năng Lực Chuyển Giao

Mỗi Core Chapter PHẢI có `olympiad_transfer.md` trả lời 6 câu:

1. **Nhận diện trong đề** — "Nếu đề nói X → dùng concept này"
2. **Baseline tối thiểu** — cái gì nộp nhanh nhất? bao lâu?
3. **Metric & Validation** — đề dùng metric gì? validation strategy?
4. **Failure modes** — top 3 lỗi thường gặp
5. **Sau baseline** — 3 bước cải thiện theo thứ tự
6. **Phân bổ thời gian** — bảng cho cả Vòng Sơ loại (4h: 3h Public + 1h Private) VÀ Chung kết (6h: 5h Public + 1h Private)

> Phần này BIẾN giáo trình AI thông thường thành giáo trình ôn Olympic. KHÔNG ĐƯỢC BỎ QUA.

---

## R8. Ngôn Ngữ & Giọng Văn

### Ngôn ngữ

- **Nội dung chính:** Tiếng Việt
- **Code, biến, comment code:** Tiếng Anh
- **Thuật ngữ kỹ thuật:** Giữ tiếng Anh gốc + giải thích tiếng Việt lần đầu xuất hiện.
  - SAI: "cơ chế chú ý" → ĐÚNG: "Attention (cơ chế chú ý)"

### Giọng văn

- Trực tiếp, rõ ràng, không học thuật xa vời.
- Xưng hô: "bạn" (người đọc), không xưng "tôi/mình" (tác giả).
- Không rào đón: "Như chúng ta đã biết..." → bỏ, vào thẳng.
- Không copy Wikipedia — derive, giải thích, cho ví dụ.

---

## R9. Reproducibility — Tái Lập

Mọi notebook phải:

- Chạy được **từ đầu đến cuối** bằng "Restart & Run All" trên Colab mới.
- Seed cố định: `random=42, numpy=42, torch=42`.
- Không dùng đường dẫn tuyệt đối.
- Dataset nhỏ: commit hoặc script download. Dataset lớn (>10MB): script.
- Ghi rõ runtime estimate và hardware requirements ở đầu.

> Cẩm nang Phần 08: "Mã nguồn phải chạy tuần tự từ đầu đến cuối... cố định seed... dùng đường dẫn tương đối."

---

## R10. Track Markers — Đánh Dấu Lộ Trình

Mỗi chương/module ghi rõ track guidance:

- ⭐ **Bắt buộc** — không bỏ qua
- 📖 **Nên đọc lướt** — review nhanh
- ⏭️ **Bỏ qua** nếu pass diagnostic
- ⚡ **Nâng cao** — optional, dành cho muốn học sâu

FORMAT trong README:

```markdown
> **Track:** Foundation ⭐ | Contest 📖
```

---

## R11. Quality Gate — Chương Chỉ "Done" Khi

```
Outlined → Drafted → Technically Reviewed → Learner Tested → Revised → Published

```

Một chương chỉ được gọi là **Drafted** khi:

- [ ] README.md có đủ ①-⑯ (hoặc ghi rõ bước nào bỏ và tại sao)
- [ ] Tất cả notebook chạy Restart & Run All không lỗi
- [ ] code_notes.md có ≥2 bài luyện code tay
- [ ] exercises.md có đúng số tầng theo loại chương
- [ ] references.md có ≥3 official docs links trỏ đúng trang

Một chương chỉ được gọi là **Published** khi thêm:

- [ ] Toán và code đã kiểm chứng (self hoặc peer review)
- [ ] Có nguồn cho mọi phát biểu quan trọng
- [ ] Learning outcomes khớp với exercises
- [ ] ≥1 người thuộc target audience đã học thử
- [ ] Misconceptions phổ biến đã ghi
- [ ] Thời gian học thực tế không lệch >50% so với ước tính

---

## R12. Commit Convention

```
feat(core): draft linear regression chapter
feat(concept): draft augmentation lesson
feat(comp): create image classification competition lab
feat(pipeline): build EDA template v1
solve(ioai25): baseline for task 2
postmortem(mock1): week 8 mock analysis
outline(transformer): skeleton with outcomes
review(linreg): fix gradient derivation
template(cv): update image classification pipeline
release(v0.1): tag pre-competition release

```

---

## R13. Thư Viện Được Phép (Cẩm nang Phần 08)

Chỉ dạy và sử dụng các thư viện sau trong notebook:

| Nhóm     | Thư viện                                                                                                                     |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Học sâu  | `torch`, `torchvision`, `pytorch_lightning`                                                                                  |
| NLP/LLM  | `transformers`, `sentence_transformers`, `datasets`, `evaluate`, `faiss`, `rank_bm25`, `spacy`, `nltk`, `gensim`, `fasttext` |
| CV       | `cv2`, `PIL`, `torchvision`, `skimage`                                                                                       |
| ML       | `sklearn`, `xgboost`, `catboost`, `lightgbm`                                                                                 |
| Data     | `numpy`, `pandas`, `scipy`                                                                                                   |
| Viz      | `matplotlib`, `seaborn`, `plotly`, `autoviz`, `tensorboard`                                                                  |
| Tiện ích | `tqdm`, `joblib`, `jupyter`                                                                                                  |
| Stdlib   | `pickle`, `os`, `glob`, `pathlib`, `json`, `csv`, `random`, `math`, `re`, `collections`, `itertools`                         |

> Nếu dùng thư viện NGOÀI danh sách này, PHẢI ghi chú rõ: "⚠️ Thư viện này KHÔNG được phép trong thi, chỉ dùng để minh họa."

---

## R14. Khi Được Yêu Cầu Soạn 1 Chương

Workflow bắt buộc:

1. **Xác định archetype** (Core / Concept / Competition)
2. **Đọc plan** tương ứng trong `plan/02_noi_dung_giao_trinh.md` → xác nhận scope
3. **Đọc template** tương ứng trong `plan/04_templates.md`
4. **Đọc references** trong `plan/05_tai_lieu_tham_khao.md` → xác nhận nguồn chính
5. **Tạo file theo đúng cấu trúc** archetype
6. **Kiểm tra R2-R11** trước khi gọi là xong

> KHÔNG BAO GIỜ bắt đầu viết code trước khi viết README.md (theory first).

---

## R15. Anti-Patterns — TUYỆT ĐỐI KHÔNG LÀM

- ❌ Copy công thức không derive
- ❌ Viết notebook không seed, không runtime estimate
- ❌ Giao bài tập mà không có worked example trước
- ❌ Link docs chung chung (link trang chủ sklearn thay vì link đúng function)
- ❌ Dùng thuật ngữ chưa giải thích
- ❌ Viết "như chúng ta đã biết", "hiển nhiên", "dễ thấy"
- ❌ Bỏ qua olympiad_transfer cho Core Chapter
- ❌ Dùng thư viện ngoài danh sách cho phép mà không ghi chú
- ❌ Viết cho mình đọc, không viết cho người học
- ❌ Tạo file chỉ để đủ bộ — không có nội dung thật thì chưa tạo
