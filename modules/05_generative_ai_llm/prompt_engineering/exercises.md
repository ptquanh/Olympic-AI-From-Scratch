# Bài tập: Prompt Engineering

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

1. Bạn gửi cho LLM prompt sau: "1+1=2. 2+2=4. 3+3=". Đây là kỹ thuật prompting nào?
2. Nếu một profile cho phép 2.000 token mỗi phiên, vì sao copy 5.000 dòng code là chiến thuật không hợp lệ và khó kiểm chứng? Nêu rõ profile nào đang được giả định.
3. Tại sao prompt "Viết code huấn luyện CNN" lại kém hiệu quả hơn "Viết PyTorch training loop cho mô hình ResNet18 trên tập CIFAR10"?

**Kết quả mong đợi:** Một lập luận ngắn nêu giả định, các bước suy luận và kết luận kiểm chứng được.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

1. (Không cần notebook, có thể thử trực tiếp trên ChatGPT/Gemini). Viết một đoạn Chain-of-Thought prompt yêu cầu mô hình giải một bài toán đố mẹo (VD: "Có 5 con ếch ngồi trên lá sen, 3 con quyết định nhảy. Hỏi còn mấy con trên lá?"). Yêu cầu nó giải thích kỹ trước khi chốt đáp án.
2. Viết một prompt yêu cầu mô hình trích xuất Tên, Tuổi, và Số điện thoại từ đoạn văn bản tự do, và **bắt buộc** trả về định dạng JSON (không có chữ nào khác).

**Kết quả mong đợi:** Code chạy được với test/shape mô tả trong đề; nêu rõ input và output.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

1. Dùng bất kỳ một public API LLM nào (Gemini API, OpenAI API - nếu có), gửi một yêu cầu phân loại cảm xúc văn bản bằng Zero-shot. Sau đó thử lại với Few-shot (3 ví dụ). Đánh giá xem Few-shot có giúp API trả về kết quả ổn định hơn (ít bị sinh thêm chữ thừa) không.

**Kết quả mong đợi:** Bảng hoặc biểu đồ kết quả cho từng cấu hình, kèm observation và giải thích nguyên nhân.
