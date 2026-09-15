# References: Debugging ML — Tìm lỗi bằng kiểm chứng nhỏ

## 📚 Official Documentation

| Thư viện/chủ dự án | Đọc gì                      | Link trực tiếp                                                                                         |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------ |
| BCE ổn định        | `np.logaddexp(0, logits)`   | [Trang trực tiếp](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html)               |
| Đo sai số          | `np.linalg.norm(g - g_num)` | [Trang trực tiếp](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)             |
| Finite differences | `scipy.optimize.check_grad` | [Trang trực tiếp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.check_grad.html) |

API được dùng trong environment của repo; các trang stable có thể mới hơn phiên bản đã khóa. Ưu tiên contract trong notebook đã chạy và [constraints](../../../envs/constraints-py310.txt).

## 📖 Textbook Chapters

| Sách                                                                | Chương                                                 | Tại sao đọc                                            |
| ------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| D2L                                                                 | Ch.3.4 — Linear Regression Implementation from Scratch | Đối chiếu training loop và cập nhật tham số.           |
| [D2L](https://d2l.ai/chapter_linear-regression/generalization.html) | 3.6 — Generalization                                   | Phân biệt fit dữ liệu hiện có với dự đoán dữ liệu mới. |

## 🎥 Video

| Video/nguồn có video                                                                                      | Tác giả         | Nên xem khi nào                            |
| --------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------ |
| [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Andrej Karpathy | Khi cần nhìn từng bước backward và update. |

## 📝 Blog/Tutorial

- [Bài đọc trực tiếp](https://cs231n.github.io/neural-networks-3/) — đối chiếu quy trình và các failure mode được dùng trong chương; đây là nguồn của phương pháp, không phải nguồn dataset của lab.

## 🏆 Competition Resources

- [AI Challenge PTIT](https://aichallenge.ptit.edu.vn) — tìm đề luyện tập và schema của từng bài; không suy diễn quy chế từ lab synthetic.
- [Competition profiles của giáo trình](../../../docs/COMPETITION_PROFILES.md) — nơi phân biệt quy chế theo kỳ/năm.
- Lab hiện tại là bài mô phỏng tự biên soạn, không phải đề hoặc winning solution chính thức. Chuyển giao theo bài T-1 trong [exercises](exercises.md).

## Provenance & môi trường

Nội dung và dữ liệu synthetic được tạo cho giáo trình. Không cần tải dataset, checkpoint hoặc dùng Internet để chạy notebook. Code dùng Python stdlib, NumPy, pandas, scikit-learn, Matplotlib và joblib khi có import; quyền dùng thư viện ở cuộc thi thật phải đối chiếu profile đúng kỳ. Ngày đối chiếu tài liệu phương pháp: 2026-09-15; chưa xác nhận luật mới cho một kỳ thi cụ thể.
