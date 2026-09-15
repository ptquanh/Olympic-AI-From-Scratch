# References: Public Test — Pseudo-labeling và Test-Time Augmentation

## 📚 Official Documentation

| Thư viện/chủ dự án | Đọc gì                   | Link trực tiếp                                                                                                           |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Confidence mask    | `np.max(p, axis=1)`      | [Trang trực tiếp](https://numpy.org/doc/stable/reference/generated/numpy.max.html)                                       |
| Gộp góc nhìn       | `np.mean(views, axis=0)` | [Trang trực tiếp](https://numpy.org/doc/stable/reference/generated/numpy.mean.html)                                      |
| Self-training API  | `SelfTrainingClassifier` | [Trang trực tiếp](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html) |

API được dùng trong environment của repo; các trang stable có thể mới hơn phiên bản đã khóa. Ưu tiên contract trong notebook đã chạy và [constraints](../../../envs/constraints-py310.txt).

## 📖 Textbook Chapters

| Sách                                                                | Chương                       | Tại sao đọc                                            |
| ------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------ |
| D2L                                                                 | Ch.14.1 — Image Augmentation | Phân biệt biến đổi giữ nhãn và thay đổi ngữ nghĩa.     |
| [D2L](https://d2l.ai/chapter_linear-regression/generalization.html) | 3.6 — Generalization         | Phân biệt fit dữ liệu hiện có với dự đoán dữ liệu mới. |

## 🎥 Video

| Video/nguồn có video                                                                      | Tác giả            | Nên xem khi nào                                                                        |
| ----------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------- |
| [Scikit-learn MOOC — video bài giảng](https://inria.github.io/scikit-learn-mooc/toc.html) | Inria/scikit-learn | Chọn video về evaluation, preprocessing hoặc ensemble khi cần nhìn pipeline thực hành. |

## 📝 Blog/Tutorial

- [Bài đọc trực tiếp](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html) — đối chiếu quy trình và các failure mode được dùng trong chương; đây là nguồn của phương pháp, không phải nguồn dataset của lab.

## 🏆 Competition Resources

- [AI Challenge PTIT](https://aichallenge.ptit.edu.vn) — tìm đề luyện tập và schema của từng bài; không suy diễn quy chế từ lab synthetic.
- [Competition profiles của giáo trình](../../../docs/COMPETITION_PROFILES.md) — nơi phân biệt quy chế theo kỳ/năm.
- Lab hiện tại là bài mô phỏng tự biên soạn, không phải đề hoặc winning solution chính thức. Chuyển giao theo bài T-1 trong [exercises](exercises.md).

## Provenance & môi trường

Nội dung và dữ liệu synthetic được tạo cho giáo trình. Không cần tải dataset, checkpoint hoặc dùng Internet để chạy notebook. Code dùng Python stdlib, NumPy, pandas, scikit-learn, Matplotlib và joblib khi có import; quyền dùng thư viện ở cuộc thi thật phải đối chiếu profile đúng kỳ. Ngày đối chiếu tài liệu phương pháp: 2026-09-15; chưa xác nhận luật mới cho một kỳ thi cụ thể.
