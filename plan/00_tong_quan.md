# 📚 Olympic AI From Scratch — Tổng Quan Giáo Trình

## Mục Tiêu

> Xây dựng giáo trình AI tiếng Việt, open-source và có thể tái lập, giúp người không biết hoặc biết ít AI có thể nắm vững và chuyên sâu kiến thức để thi tốt các kỳ thi Olympic AI — bao gồm **OlpAI Sinh viên**, **Olympic AI PTIT**, **VOAI**, **IOAI**, và các kỳ thi quốc tế liên quan.

Giáo trình bám sát:
- **Lộ trình 5 chặng** trong Cẩm nang Olympic AI (Phần 04)
- **Đề cương ôn luyện chính thức** (Phần 15): ML/DL + CV + NLP + Audio
- **Lộ trình 8 module đào tạo** của Meta Ecom Uni × PTIT (Phần 18)
- **IOAI 2026 Syllabus** và **OlimpiadaAI/szkolenia** (Ba Lan)

---

## Bốn Tiêu Chí Thành Công

| Tiêu chí | Nghĩa là |
| --- | --- |
| **Đúng** | Công thức, code, tài liệu tham khảo và kết quả đều được kiểm chứng |
| **Dễ học** | Có prerequisite, learning outcomes, worked examples và lộ trình rõ |
| **Giúp thi tốt** | Có bài tập chuyển giao, đề thật, timed practice và postmortem |
| **Luyện code tay** | Mỗi chương có code patterns cần nhớ, bài tập code không nhìn tài liệu, và link docs chính thức để tự research |

---

## Đối Tượng

| Nhóm | Mô tả | Track |
|-------|--------|-------|
| **Người mới** | Chưa biết hoặc biết ít ML/DL, muốn xây nền tảng bài bản | 🟢 Foundation Track |
| **Đã có cơ bản** | Biết Python + ML cơ bản, muốn luyện thi trực tiếp | 🔴 Contest Track |

---

## Cấu Trúc Plan (Tách File)

| File | Nội dung |
|------|----------|
| [`00_tong_quan.md`](00_tong_quan.md) | **Bạn đang đây** — mục tiêu, đối tượng, tổng quan |
| [`01_phuong_phap_su_pham.md`](01_phuong_phap_su_pham.md) | Learner journey, 3 loại chương, bài tập phân tầng, mastery gates |
| [`02_noi_dung_giao_trinh.md`](02_noi_dung_giao_trinh.md) | Cấu trúc repo, danh sách modules & chapters, dependency graph |
| [`03_timeline_va_tien_do.md`](03_timeline_va_tien_do.md) | Timeline 10 tuần, quỹ thời gian, quality gates, versioning |
| [`04_templates.md`](04_templates.md) | Templates cho README, code_notes, references, olympiad_transfer |
| [`05_tai_lieu_tham_khao.md`](05_tai_lieu_tham_khao.md) | Nguồn tham khảo uy tín, docs links, quy ước commit |

---

## Vai Trò Của Tác Giả

Tác giả (bạn) vừa học vừa soạn. Nhưng sản phẩm cuối phải phục vụ **người học**, không phải ghi lại quá trình học của tác giả. Mỗi chương phải đọc được bởi sinh viên không quen biết bạn.

---

## Ánh Xạ Với Cẩm Nang Olympic AI

| Phần Cẩm nang | Nội dung | Ảnh hưởng đến giáo trình |
|---------------|----------|--------------------------|
| **Phần 04** — Lộ trình 5 chặng | Nền tảng → ML → DL → GenAI/LLM → Thực chiến | Thứ tự module bám theo 5 chặng |
| **Phần 07** — Môi trường thi | JupyterLab, GPU H100, 200GB, offline | Module 05 cần có JupyterLab workflow |
| **Phần 08** — Thư viện cho phép | torch, sklearn, xgboost, transformers, cv2, re, os... | Chỉ dạy thư viện được phép dùng trong thi |
| **Phần 09** — LLM trong thi | 2000 tokens/phiên, chỉ giai đoạn Public Test | Module 05 cần có chiến thuật dùng LLM |
| **Phần 10** — Nộp bài | FINAL/ → best_model.pt + submission.zip + notebook | Module 07 cần có notebook checklist + FINAL template |
| **Phần 12** — Chiến thuật thi | Chia thời gian, baseline first, ensemble cuối | Olympiad transfer files phải bám sát |
| **Phần 15** — Đề cương ôn luyện | ML/DL + CV + NLP + Audio | **Nguồn chính** để thiết kế nội dung module |
| **Phần 18** — Lộ trình 8 module | M0–M7, 38 buổi | Tham khảo thứ tự và phân bổ thời gian |

---

## Trạng Thái Hiện Tại

- **Đội thi:** Đã có đội 2-3 người
- **Tiến độ:** Đang chốt plan. Chưa scaffold code.
- **Kỳ thi gần nhất:** OlpAI Vòng Khu Vực — 01/11/2026
