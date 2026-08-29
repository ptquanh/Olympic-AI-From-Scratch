# Lời giải: Regex & Data Handling

<details><summary><b>Tầng 1: Understand</b></summary>

Greedy (Tham lam) sẽ match đoạn dài nhất có thể, tức là nó sẽ match từ dấu `<` đầu tiên đến dấu `>` CUỐI CÙNG trong chuỗi.
Non-greedy (`.*?`) sẽ match đoạn ngắn nhất có thể, tức là nó sẽ match từ `<` đến dấu `>` GẦN NHẤT.

</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
import re

text = "Hello, world! Email me at test@example.com."
# Lấy danh sách từ
words = re.findall(r'\b\w+\b', text)
print("Words:", len(words))

# Rút trích email
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Emails:", emails)
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

Để đọc hàng nghìn file CSV nhanh chóng:

```python
import glob
import pandas as pd

# Liệt kê tất cả file CSV
csv_files = glob.glob('data_folder/*.csv')

# Đọc và gộp thành 1 dataframe
df_list = [pd.read_csv(f) for f in csv_files]
final_df = pd.concat(df_list, ignore_index=True)
```

</details>
