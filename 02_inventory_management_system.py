import sys
from collections import Counter

two_count = 0
three_count = 0
boxes = []
answer = ""

for line in sys.stdin:
    boxes.append(line)
    counter = Counter(line)
    if len({k: v for k, v in counter.items() if v == 2}) > 0:
        two_count += 1
    if len({k: v for k, v in counter.items() if v == 3}) > 0:
        three_count += 1

print(two_count * three_count)

for i in range(len(boxes)):
    if len(answer) > 0:
        break
    for j in range(i+1, len(boxes)):
        if sum(a != b for a, b in zip(boxes[i], boxes[j])) == 1:
            u = zip(boxes[i], boxes[j])
            for i, j in u:
                if i == j:
                    answer = answer + i
            break

print(answer)
