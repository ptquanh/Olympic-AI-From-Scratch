# Bài tập: Prompt Engineering

## Tầng 1: Understand

1. Bạn gửi cho LLM prompt sau: "1+1=2. 2+2=4. 3+3=". Đây là kỹ thuật prompting nào?
2. Nếu bạn copy paste 5000 dòng code vào ChatGPT trong phòng thi (giới hạn 2000 tokens), điều gì sẽ xảy ra?
3. Tại sao prompt "Viết code huấn luyện CNN" lại kém hiệu quả hơn "Viết PyTorch training loop cho mô hình ResNet18 trên tập CIFAR10"?

## Tầng 2: Implement

1. (Không cần notebook, có thể thử trực tiếp trên ChatGPT/Gemini). Viết một đoạn Chain-of-Thought prompt yêu cầu mô hình giải một bài toán đố mẹo (VD: "Có 5 con ếch ngồi trên lá sen, 3 con quyết định nhảy. Hỏi còn mấy con trên lá?"). Yêu cầu nó giải thích kỹ trước khi chốt đáp án.
2. Viết một prompt yêu cầu mô hình trích xuất Tên, Tuổi, và Số điện thoại từ đoạn văn bản tự do, và **bắt buộc** trả về định dạng JSON (không có chữ nào khác).

## Tầng 3: Experiment

1. Dùng bất kỳ một public API LLM nào (Gemini API, OpenAI API - nếu có), gửi một yêu cầu phân loại cảm xúc văn bản bằng Zero-shot. Sau đó thử lại với Few-shot (3 ví dụ). Đánh giá xem Few-shot có giúp API trả về kết quả ổn định hơn (ít bị sinh thêm chữ thừa) không.
