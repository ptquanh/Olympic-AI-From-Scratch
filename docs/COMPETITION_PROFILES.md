# Competition profiles

> **Trạng thái:** Technical Review Beta · **Ngày kiểm chứng:** 2026-08-31

Tài liệu này tách kiến thức dùng chung khỏi luật của từng kỳ thi. `curriculum.yml` là nguồn máy đọc được; trang này là bản giải thích cho người học. Thông báo chính thức mới hơn luôn được ưu tiên so với cẩm nang hoặc ghi chú cũ.

## General

Không giả định thời lượng, Internet, GPU, package, model, LLM hay định dạng submission. Chiến thuật chung dùng tỷ lệ timebox thay vì mốc giờ tuyệt đối. Trước khi thi, tạo profile từ thông báo chính thức đúng kỳ và đúng năm.

## Olympic AI PTIT 2026

| Thuộc tính   | Giá trị đã kiểm chứng                                                    |
| ------------ | ------------------------------------------------------------------------ |
| Phạm vi      | Vòng sơ loại 4 giờ cho bảng Sinh viên PTIT; vòng chung kết 6 giờ         |
| Giai đoạn    | Phần lớn thời gian dùng train/public test; 1 giờ cuối dùng private test  |
| Mạng/package | Không có Internet mở; chỉ thư viện cài sẵn                               |
| LLM          | Môi trường kiểm soát, chỉ giai đoạn đầu, tối đa 2.000 token mỗi phiên    |
| Lưu ý        | Lịch đã từng được điều chỉnh; kiểm tra thông báo mới nhất trước ngày thi |

Nguồn công khai: [mô tả môi trường PTIT 2026](https://ai.ptit.edu.vn/olympic-ai-ptit-2026-dong-cong-dang-ky-cac-doi-buoc-vao-giai-doan-chuan-bi-cho-vong-so-loai/) và [thông báo điều chỉnh lịch PTIT 2026](https://ai.ptit.edu.vn/thong-bao-dieu-chinh-lich-thi-olympic-ai-ptit-2026/). Cẩm nang PDF bên thứ ba chỉ được dùng làm tài liệu đối chiếu cục bộ và không được phân phối trong repository.

## OlpAI

Tên này có thể được dùng cho các chương trình/nhóm đối tượng khác nhau. Beta không gắn một bộ luật OlpAI cụ thể khi chưa có văn bản chính thức xác định mùa thi. Không kế thừa mốc PTIT, VOAI hay IOAI.

## VOAI 2026

Thông báo chính thức nêu vòng sơ loại trắc nghiệm 180 phút ngày 23/04/2026 và vòng chung kết lập trình AI 6 giờ ngày 16–17/05/2026. Đây là luật VOAI 2026, không phải cấu trúc chung của Olympic AI. Quyền dùng LLM và môi trường package phải lấy từ thông báo kỹ thuật mới nhất.

Nguồn: [Thông báo VOAI của Hội Tin học Việt Nam](https://www.olp.vn/olympic-ai-cho-h%E1%BB%8Dc-sinh/th%C3%B4ng-b%C3%A1o-voai).

## IOAI 2026

IOAI công bố syllabus và contest rules theo từng mùa. Curriculum dùng syllabus để định hướng chủ đề, nhưng không suy diễn thời lượng hay công cụ từ PTIT/VOAI. Trước mỗi mùa phải khóa URL, phiên bản và ngày kiểm chứng.

Nguồn: [IOAI 2026 contest rules](https://ioai-official.org/2026-contest-rules/), [IOAI 2026 syllabus](https://ioai-official.org/2026-syllabus/), [IOAI regulations](https://ioai-official.org/regulations/).

## Thứ tự ưu tiên nguồn

1. Quy chế và thông báo chính thức mới nhất.
2. PDF cẩm nang của Ban tổ chức.
3. Official documentation và paper gốc.
4. Textbook/course uy tín.
5. Bài kỹ thuật có tác giả rõ ràng, chỉ đóng vai trò tham khảo.

Khi hai nguồn mâu thuẫn, ghi lại cả hai trong review record, áp dụng nguồn chính thức mới hơn và cập nhật `verified` trong `curriculum.yml`.
