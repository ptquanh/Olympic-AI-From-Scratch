# FINAL Folder Template

Template này minh họa cách đóng gói khi thể lệ yêu cầu thư mục `FINAL/` và nhiều tác vụ. Tên folder/file cụ thể phải đối chiếu thông báo chính thức của kỳ thi trước khi nộp.

```text
FINAL/
├── TACVU1/
│   ├── generate_result.ipynb
│   ├── best_model.*
│   ├── config.json
│   └── README.md
├── TACVU2/
│   ├── generate_result.ipynb
│   ├── best_model.*
│   ├── config.json
│   └── README.md
└── technical_report.md
```

## README của mỗi tác vụ

Phải đủ ngắn để reviewer chạy được ngay:

```markdown
# TACVU1

Environment: <profile/version>
Input: <relative path>
Run: Restart kernel -> Run All generate_result.ipynb
Output: <relative path + expected schema>
Model artifact: best_model.*
Expected runtime: <measured time>
```

## Trước khi zip

- [ ] Xóa checkpoint/model thử nghiệm không dùng.
- [ ] Không đóng gói dataset nếu thể lệ không yêu cầu.
- [ ] Không có cache, `.ipynb_checkpoints`, log lớn, secret/token.
- [ ] Notebook chỉ tham chiếu relative path.
- [ ] Giải nén bản zip vào thư mục mới và chạy lại smoke test.

Nếu thể lệ chỉ yêu cầu source code hoặc format khác, bỏ template này và làm theo profile chính thức.
