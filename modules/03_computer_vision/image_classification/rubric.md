# Rubric: Image Classification Competition

Tổng 100 điểm. Baseline Beta dùng dữ liệu ảnh nhỏ có tín hiệu hình học, chạy offline; pretrained model không bắt buộc.

| Hạng mục        | Điểm | Evidence bắt buộc                                                                           |
| --------------- | ---: | ------------------------------------------------------------------------------------------- |
| Data & EDA      |   15 | Kiểm schema/shape/dtype/class balance; hiển thị mẫu theo lớp; ID không trùng                |
| Split & leakage |   15 | Split tái lập, stratified khi phù hợp; preprocessing chỉ fit trên train; test không có nhãn |
| Baseline        |   20 | Pipeline chạy end-to-end; seed/config rõ; metric validation được tính đúng                  |
| Experiment      |   15 | Một giả thuyết, một thay đổi, bảng kết quả và giải thích; không chọn theo test              |
| Error analysis  |   10 | Confusion matrix hoặc nhóm lỗi; nêu ít nhất một failure mode                                |
| Infer & submit  |   15 | Load artifact/transform nhất quán; đúng ID, cột, số dòng, thứ tự và không NaN               |
| Reproducibility |   10 | Chạy lại thành công trong `OAI_FAST_MODE=1`, offline, không auto-install/download           |

Gate bắt buộc: nếu có leakage, submission sai schema hoặc pipeline không chạy từ đầu đến cuối thì tối đa 50 điểm. Transfer learning là cải tiến tùy profile, không phải tiêu chí mặc định.
