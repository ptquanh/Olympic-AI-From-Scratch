# Bài tập: Fine-tuning Patterns

## Tầng 1: Understand

1. Một layer Linear có kích thước đầu vào $d=1024$ và đầu ra $k=1024$. Nếu dùng LoRA với rank $r=8$, số lượng tham số cần huấn luyện là bao nhiêu? Số lượng tham số của Linear gốc là bao nhiêu?
2. Tại sao ta không khởi tạo cả A và B bằng 0?
3. Tại sao biến `scaling = alpha / r` lại cần thiết?

## Tầng 2: Implement

1. Mở `01_from_scratch.ipynb`. Hoàn thiện class `LoRALinear` dựa trên kiến thức đã học.
2. Viết một script nhỏ so sánh tốc độ và bộ nhớ VRAM sử dụng giữa Full Fine-tuning một mạng nhỏ (2 layers) và LoRA Fine-tuning mạng đó. (Nếu bạn không có GPU, in số lượng tham số có requires_grad=True).

## Tầng 3: Experiment

1. Trong `03_experiments.ipynb`, thử thay đổi rank $r \in \{1, 4, 16, 64\}$. Quan sát tốc độ giảm loss trên một tập dataset phân loại văn bản nhỏ. Có phải rank càng cao thì hội tụ càng nhanh?
2. Thử áp dụng LoRA cho các ma trận khác của Transformer (chỉ apply vào `query` vs apply vào cả `query, key, value`). Đánh giá sự khác biệt.

## Tầng 4: Transfer

1. LoRA được thiết kế cho Linear layer. Bạn có thể tự custom một `LoRAConv2d` cho các bài toán Computer Vision không?
   _Gợi ý: Ma trận Conv2d có shape `(out_c, in_c, kernel, kernel)`. Có thể reshape nó thành `(out_c, in_c _ kernel _ kernel)` rồi áp dụng LoRA._

## Tầng 5: Olympiad

1. Bài toán: Phân loại sắc thái bình luận (Tích cực/Tiêu cực) dùng mô hình phobert-base.
   Yêu cầu: Dùng thư viện `peft` để fine-tune chỉ với LoRA.
   Giới hạn: Chạy được với 4GB VRAM. (Thời gian: 45 phút).
