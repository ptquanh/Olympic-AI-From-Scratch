# Rubric: Text Classification Competition

Tổng 100 điểm. Baseline bắt buộc là TF–IDF + Logistic Regression chạy offline; Transformer là cải tiến tùy profile.

| Hạng mục        | Điểm | Evidence bắt buộc                                                                                |
| --------------- | ---: | ------------------------------------------------------------------------------------------------ |
| Data & EDA      |   15 | Schema, label balance, duplicate/empty text, độ dài văn bản                                      |
| Split & leakage |   15 | Split tái lập/stratified; vectorizer chỉ fit trên train; duplicate groups không đi qua hai split |
| Baseline        |   20 | TF–IDF + linear model chạy end-to-end; Macro F1 và confusion matrix                              |
| Experiment      |   15 | Một thay đổi về n-gram/min_df/class weight/threshold; cùng split và seed                         |
| Error analysis  |   10 | Ít nhất 5 lỗi được nhóm theo failure mode, không chỉ liệt kê                                     |
| Infer & submit  |   15 | Preprocessing giống train; đúng ID/cột/số dòng/thứ tự; không NaN                                 |
| Reproducibility |   10 | Fast/offline pass; dependency khai báo; không tải model hoặc cài package ngầm                    |

Gate bắt buộc: leakage, fit TF–IDF trên cả test, submission sai schema hoặc pipeline không chạy khiến tổng điểm tối đa 50.
