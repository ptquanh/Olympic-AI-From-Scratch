# References: JupyterLab Workflow — Kernel sạch và bài nộp tái lập

## 📚 Official Documentation

| Thư viện/chủ dự án | Đọc gì                             | Link trực tiếp                                                                    |
| ------------------ | ---------------------------------- | --------------------------------------------------------------------------------- |
| Quản lý kernel     | `Running panel → Shut Down`        | [Trang trực tiếp](https://jupyterlab.readthedocs.io/en/stable/user/running.html)  |
| Thao tác notebook  | `Restart Kernel and Run All Cells` | [Trang trực tiếp](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) |
| Terminal           | `Launcher → Terminal`              | [Trang trực tiếp](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html) |

API được dùng trong environment của repo; các trang stable có thể mới hơn phiên bản đã khóa. Ưu tiên contract trong notebook đã chạy và [constraints](../../../envs/constraints-py310.txt).

## 📖 Textbook Chapters

| Sách                                                                | Chương                                     | Tại sao đọc                                            |
| ------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------ |
| HOML, 3rd ed.                                                       | Ch.2 — Get the Data / Create the Workspace | Tổ chức workspace cho thí nghiệm.                      |
| [D2L](https://d2l.ai/chapter_linear-regression/generalization.html) | 3.6 — Generalization                       | Phân biệt fit dữ liệu hiện có với dự đoán dữ liệu mới. |

## 🎥 Video

| Video/nguồn có video                                                                         | Tác giả         | Nên xem khi nào                                     |
| -------------------------------------------------------------------------------------------- | --------------- | --------------------------------------------------- |
| [JupyterLab video overview](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) | Project Jupyter | Xem video nhúng trên trang khi chưa quen các panel. |

## 📝 Blog/Tutorial

- [Bài đọc trực tiếp](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) — đối chiếu quy trình và các failure mode được dùng trong chương; đây là nguồn của phương pháp, không phải nguồn dataset của lab.

## 🏆 Competition Resources

- [AI Challenge PTIT](https://aichallenge.ptit.edu.vn) — tìm đề luyện tập và schema của từng bài; không suy diễn quy chế từ lab synthetic.
- [Competition profiles của giáo trình](../../../docs/COMPETITION_PROFILES.md) — nơi phân biệt quy chế theo kỳ/năm.
- Lab hiện tại là bài mô phỏng tự biên soạn, không phải đề hoặc winning solution chính thức. Chuyển giao theo bài T-1 trong [exercises](exercises.md).

## Provenance & môi trường

Nội dung và dữ liệu synthetic được tạo cho giáo trình. Không cần tải dataset, checkpoint hoặc dùng Internet để chạy notebook. Code dùng Python stdlib, NumPy, pandas, scikit-learn, Matplotlib và joblib khi có import; quyền dùng thư viện ở cuộc thi thật phải đối chiếu profile đúng kỳ. Ngày đối chiếu tài liệu phương pháp: 2026-09-15; chưa xác nhận luật mới cho một kỳ thi cụ thể.
