import collections

import matplotlib.pyplot as plt
import numpy as np


with open("plotexamples/data_kieu.txt", mode="r", encoding="utf-8") as fin:
    lines = fin.readlines()

words = [w  for line in lines for w in line.strip().split()
         if not w.startswith("(") and not w.endswith(")")]
counter = collections.Counter(words)

most_common_words = counter.most_common(10)
input("=== Phân tích truyện Kiều của Nguyễn Du ===")
input(f"Số chữ tổng cộng: {len(words)}")
input(f"Số chữ khác nhau: {len(counter)}")
input(f"Mười chữ xuất hiện nhiều nhất: {most_common_words}")
input("Xem minh họa biểu đồ...")

keys = [x[0] for x in most_common_words]
values = [x[1] for x in most_common_words]
indexes = np.arange(len(keys))
width = 0.7
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.3, keys)
plt.show()