# Lời giải: Object Detection

<details><summary><b>Tầng 1: Understand</b></summary>
Mô hình sẽ sinh ra rất nhiều box chồng chéo lên nhau quanh chiếc xe hơi (vì nhiều ô lưới cùng tự tin rằng nó chứa xe hơi). NMS sẽ duyệt qua các box này, nó giữ lại box có độ tự tin cao nhất, sau đó "xóa sổ" toàn bộ các box khác bị trùng lặp (có IoU với box xịn > Threshold). 
</details>

<details><summary><b>Tầng 2: Implement</b></summary>

```python
def compute_iou(boxA, boxB):
    # Tìm tọa độ phần giao
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # Diện tích giao (nếu không giao, hàm max sẽ ép về 0)
    interArea = max(0, xB - xA) * max(0, yB - yA)

    # Diện tích 2 box
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # Tránh chia cho 0
    iou = interArea / float(boxAArea + boxBArea - interArea + 1e-6)
    return iou
```

</details>

<details><summary><b>Tầng 3: Experiment</b></summary>

```python
import torch
import torchvision.ops as ops

boxes = torch.tensor([[100, 100, 210, 210],
                      [105, 105, 215, 215],
                      [300, 300, 400, 400]], dtype=torch.float)
scores = torch.tensor([0.9, 0.75, 0.85])

# Với threshold 0.5:
keep_idx = ops.nms(boxes, scores, 0.5)
print("Keep Index (0.5):", keep_idx)
# Output: [0, 2]. Box 1 bị loại vì trùng Box 0.

# Với threshold 0.9 (Rất khắt khe, phải trùng 90% mới loại):
keep_idx_high = ops.nms(boxes, scores, 0.9)
print("Keep Index (0.9):", keep_idx_high)
# Output: [0, 2, 1]. Box 1 được giữ lại vì IoU của Box 0 và 1 chưa đạt 90%.
```

</details>

<details><summary><b>Tầng 4: Transfer</b></summary>

```python
def yolo_to_voc(yolo_box, W, H):
    x_c, y_c, w, h = yolo_box

    # Giải chuẩn hóa
    x_c, w = x_c * W, w * W
    y_c, h = y_c * H, h * H

    # Tính góc trái trên và phải dưới
    x1 = x_c - w / 2
    y1 = y_c - h / 2
    x2 = x_c + w / 2
    y2 = y_c + h / 2

    return [x1, y1, x2, y2]
```

</details>
