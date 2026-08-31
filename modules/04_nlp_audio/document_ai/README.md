# Document AI

> **Track:** Foundation ⚡ | Contest ⭐

## ① Prerequisite Check

Bạn cần đọc được image tensor/channel, hiểu bounding box, tokenization và encoder Transformer. Nếu chưa, học Image Fundamentals, Text Preprocessing và Pre-trained Encoders.

## ② Learning Outcomes

- Vẽ được pipeline image/PDF → OCR tokens + boxes → layout model/KIE → structured output.
- Chuẩn hóa bounding box và giữ liên kết page–token–box.
- Chọn metric cho OCR, entity extraction, table structure và end-to-end output.
- Chẩn đoán lỗi scan, reading order, OCR và schema thay vì chỉ đổi model.

## ③ Concept Map

`Image cleanup + OCR + 2D layout + language encoder → KIE/table QA/structured document`

## ④ Intuition

Chuỗi text thuần làm mất layout. Trên hóa đơn, “Total” có ý nghĩa vì nằm cạnh một con số; trên biểu mẫu, cùng token có nghĩa khác tùy vùng. Document AI giữ cả nội dung, tọa độ và đôi khi pixel features.

## ⑤ Worked Example

Giả sử OCR trả `[("Total", [10,80,40,90]), ("100", [70,80,90,90])]` trên trang `100×100`. Reading order và khoảng cách theo trục y cho thấy hai token cùng dòng. Khi model yêu cầu box trong `[0,1000]`, nhân mọi tọa độ x/y lần lượt với `1000/width` và `1000/height`; clip về biên và giữ nguyên ánh xạ token.

## ⑧ Framework / Lab

Lab dùng dữ liệu token/box nhỏ để minh họa shape. OCR engines như Tesseract/EasyOCR không nằm trong danh sách PTIT 2026 của PDF; chỉ dùng trong learning profile khi đã cài hợp lệ, không giả định có trong phòng thi.

## ⑩ Misconceptions

- ❌ **Sai:** OCR accuracy cao nghĩa là KIE tốt. → ✅ Reading order/boxes/schema vẫn có thể sai.
- ❌ **Sai:** Resize ảnh nhưng giữ box cũ. → ✅ Pixel và box phải dùng cùng transform.
- ❌ **Sai:** Random split từng trang luôn hợp lệ. → ✅ Các trang cùng document/customer có thể gây leakage.

## ⑮ Mastery Check

Tạo được schema output, validation theo document và error analysis tách OCR/layout/KIE.

## ⑯ Time Estimate

Theory: ~1.5h · Code: ~1.5h · Exercises: ~1h
