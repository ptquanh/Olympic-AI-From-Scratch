# Bài tập: Document AI

## U-1 — Understand

**Learning outcome:** Giải thích đúng khái niệm, giả định và giới hạn bằng lập luận kiểm chứng được.

Vì sao OCR text → BERT có thể kém layout-aware model trên hóa đơn? Nêu một trường hợp mà text-only vẫn đủ.

**Kết quả mong đợi:** Giải thích mất tọa độ/reading order; text-only có thể đủ khi tài liệu tuyến tính và schema không phụ thuộc vị trí.

## I-1 — Implement

**Learning outcome:** Cài đặt phần cốt lõi, nêu input/output và vượt qua shape/edge-case tests.

Viết hàm chuẩn hóa box `[x1,y1,x2,y2]` từ trang `width×height` sang `[0,1000]`. Validate thứ tự tọa độ và clip biên.

**Kết quả mong đợi:** Box `[10,20,50,60]` trên trang `100×200` thành `[100,100,500,300]`; box sai thứ tự bị từ chối.

## E-1 — Experiment

**Learning outcome:** Thiết kế thí nghiệm một biến, tái lập được và giải thích kết quả bằng evidence.

Cho hai tập OCR tokens/boxes: bản sạch và bản dịch box theo trục x 10%. Đo tỷ lệ cặp key–value còn cùng dòng và trong khoảng cách cho phép.

**Kết quả mong đợi:** Bảng clean/shifted với metric layout-pair accuracy; phân tích lỗi do coordinate shift thay vì đổ lỗi chung cho encoder.
