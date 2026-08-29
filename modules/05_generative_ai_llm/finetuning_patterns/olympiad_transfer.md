# Olympiad Transfer: PEFT & LoRA

## 1. Nhận diện trong đề

- Khi đề cung cấp một LLM rất lớn (7B, 14B tham số) và yêu cầu fine-tune với dữ liệu domain-specific (y tế, pháp luật).
- Khi có giới hạn nghiêm ngặt về phần cứng (VD: chỉ cấp 1 GPU T4 16GB VRAM) mà bắt fine-tune LLM.
- Bất cứ khi nào bạn dùng pre-trained model và không đủ VRAM để train.

## 2. Baseline tối thiểu

Tích hợp `peft` vào mô hình gốc. Dùng `LoraConfig` với rank $r=8$ và alpha=16. Thường chỉ áp dụng vào các ma trận Attention (`q_proj`, `v_proj`). Mã nguồn baseline này chỉ mất 5 phút để viết.

## 3. Metric & Validation

- Đánh giá trực tiếp trên metric của bài toán downstream (F1-score cho text classification, ROUGE cho summarization).
- Cần chú ý validation loss: nếu loss hội tụ cực nhanh rồi đi ngang, có thể tăng rank $r$.

## 4. Failure modes

- **Quên đặt padding side = 'left' cho Decoder-only LM:** Gây lỗi khi sinh text.
- **Model không học được:** Do quên đặt `target_modules` hoặc đặt sai tên layer. Sử dụng `model.print_trainable_parameters()` để đảm bảo có > 0% tham số được train.
- **Save sai cách:** Chỉ dùng `peft_model.save_pretrained()`. Đừng save toàn bộ mô hình gốc (rất nặng).

## 5. Sau baseline

1. **Tăng số lượng target_modules:** Apply LoRA vào cả `k_proj`, `o_proj`, và các layer MLP.
2. **QLoRA:** Dùng Quantization 4-bit (`bitsandbytes`) cho base model rồi áp dụng LoRA. Giảm VRAM xuống mức thấp nhất.
3. **Tăng rank r:** Nâng r lên 16, 32, 64 nếu bài toán phức tạp và vẫn còn VRAM.

## 6. Phân bổ thời gian

- **Vòng Sơ loại (4h):**
  - Thường bài NLP cỡ lớn sẽ không thi ở vòng 4h, hoặc chỉ dùng BERT (BERT có thể full fine-tune). Nếu bắt buộc dùng PEFT, hãy cấu hình chuẩn LoRA trong 30 phút đầu.
- **Vòng Chung kết (6h):**
  - 1h: Cấu hình môi trường, load model 4-bit, gắn QLoRA.
  - 3h: Chạy training loop và đánh giá.
  - 2h: Thử nghiệm target_modules khác nhau và merge weight để sinh kết quả nộp.
