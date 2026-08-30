# Multimodal (Vision-Language Models)

> **Thời gian học ước tính:** 2.5 giờ (theory: 1h, code: 0.5h, exercises: 1h)
> **Loại:** Concept Lesson
> **Track:** Foundation ⚡ | Contest 📖

## Prerequisite Check

Trước khi bắt đầu, bạn cần trả lời được:

1. Mô hình CNN hoặc ViT trích xuất đặc trưng ảnh như thế nào?
2. Mô hình Transformer (LLM) xử lý text token như thế nào?

Nếu chưa → quay lại CNN Architectures (Module 03) và Language Modeling (Module 05).

## Learning Outcomes

Sau chương này, bạn sẽ có thể:

- [ ] Giải thích được cơ chế ghép nối (alignment) giữa Image Encoder và Text Decoder.
- [ ] Load và sử dụng một pre-trained VLM (Vision-Language Model) qua HuggingFace.
- [ ] Xử lý ảnh và text cùng lúc để hỏi đáp về hình ảnh (Visual Question Answering).

## Concept Map

```text
[Finetuning Patterns] --> [MULTIMODAL VLM]
                                 │
                                 └── Kết hợp [CNN/ViT] và [Language Modeling]
```

## 1. Intuition — Tại Sao Cần Multimodal?

Thay vì chỉ đọc text, con người sử dụng cả mắt để nhìn và tai để nghe. Trí tuệ nhân tạo cũng đang chuyển dịch theo hướng này.
Multimodal AI có thể nhận đầu vào là (Ảnh + Câu hỏi) và sinh ra câu trả lời text.
Ví dụ:

- Input: Ảnh 1 con mèo trên bàn phím + "Con gì đang cản trở tôi code?"
- Output: "Một con mèo."

## 2. Kiến Trúc Cơ Bản Của VLM (Vision-Language Model)

Các mô hình VLM hiện đại (như LLaVA, BLIP, Qwen-VL) thường gồm 3 thành phần chính:

1. **Vision Encoder:** Thường là CLIP (Dùng ViT) để biến bức ảnh thành các patch embeddings.
2. **LLM (Text Decoder):** Thường là các LLM mã nguồn mở (như Llama, Mistral, Qwen) để sinh văn bản.
3. **Projection Layer (Connector):** Một lớp mạng Neural nhỏ (VD: MLP 2 lớp) làm nhiệm vụ "dịch" các vector đặc trưng của ảnh sang cùng không gian vector của Text, để LLM có thể hiểu được ảnh như là một dãy các "từ".

## 3. Visual Question Answering (VQA)

Đây là bài toán cốt lõi của Multimodal.
Quy trình:

1. Ảnh đi qua Vision Encoder $\rightarrow$ Image Features.
2. Text đi qua Tokenizer $\rightarrow$ Text Embeddings.
3. Image Features đi qua Projection Layer $\rightarrow$ Projected Image Features.
4. LLM nhận đầu vào là chuỗi kết hợp: `[Projected Image Features] + [Text Embeddings]` và sinh ra từ tiếp theo một cách Autoregressive.

## 4. Common Mistakes & Misconceptions

> ❌ **Sai:** VLM "nhìn" bức ảnh giống như con người nhìn.
> ✅ **Đúng:** VLM chỉ thấy một chuỗi các con số (vectors) đại diện cho ảnh. LLM thực chất đang xử lý bức ảnh như là một đoạn văn bản rất dài bằng một "ngôn ngữ lạ" đã được Connector dịch lại.

> ❌ **Sai:** Cứ ném ảnh chất lượng 4K vào VLM thì nó trả lời càng đúng.
> ✅ **Đúng:** Vision Encoder thường sẽ resize ảnh về độ phân giải cố định (VD: 224x224 hoặc 336x336). Ảnh 4K sẽ bị bóp méo hoặc nén mất chi tiết. Muốn đọc chi tiết nhỏ (như OCR), cần các kỹ thuật cắt ảnh (tiling) chuyên dụng.
