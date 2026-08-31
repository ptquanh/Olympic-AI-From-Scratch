# Bài tập: Fine-tuning Patterns

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

1. Một layer Linear có kích thước đầu vào $d=1024$ và đầu ra $k=1024$. Nếu dùng LoRA với rank $r=8$, số lượng tham số cần huấn luyện là bao nhiêu? Số lượng tham số của Linear gốc là bao nhiêu?
2. Tại sao ta không khởi tạo cả A và B bằng 0?
3. Tại sao biến `scaling = alpha / r` lại cần thiết?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

1. Mở `01_from_scratch.ipynb`. Hoàn thiện class `LoRALinear` dựa trên kiến thức đã học.
2. Viết một script nhỏ so sánh tốc độ và bộ nhớ VRAM sử dụng giữa Full Fine-tuning một mạng nhỏ (2 layers) và LoRA Fine-tuning mạng đó. (Nếu bạn không có GPU, in số lượng tham số có requires_grad=True).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

1. Trong `03_experiments.ipynb`, thử thay đổi rank $r \in \{1, 4, 16, 64\}$. Quan sát tốc độ giảm loss trên một tập dataset phân loại văn bản nhỏ. Có phải rank càng cao thì hội tụ càng nhanh?
2. Thử áp dụng LoRA cho các ma trận khác của Transformer (chỉ apply vào `query` vs apply vào cả `query, key, value`). Đánh giá sự khác biệt.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.

## T-1 — Transfer

**Learning outcome:** Chuyển kỹ thuật sang dữ liệu mới mà không leakage, dùng metric và failure mode phù hợp.

1. LoRA được thiết kế cho Linear layer. Bạn có thể tự custom một `LoRAConv2d` cho các bài toán Computer Vision không?
   _Gợi ý: Ma trận Conv2d có shape `(out_c, in_c, kernel, kernel)`. Có thể reshape nó thành `(out_c, in_c _ kernel _ kernel)` rồi áp dụng LoRA._

**Kết quả mong đợi:** Pipeline chạy trên dữ liệu/bối cảnh mới, metric phù hợp và phân tích ít nhất một failure mode.

## O-1 — Olympiad

**Learning outcome:** Dựng baseline theo đúng competition profile, timebox và artifact nộp có thể chạy lại.

1. Bài toán: Phân loại sắc thái bình luận (Tích cực/Tiêu cực) dùng mô hình phobert-base.
   Yêu cầu: Dùng thư viện `peft` để fine-tune chỉ với LoRA.
   Giới hạn: Chạy được với 4GB VRAM. (Thời gian: 45 phút).

**Kết quả mong đợi:** Baseline tái lập được trong timebox, validation đúng, metric và checklist file cần nộp.
