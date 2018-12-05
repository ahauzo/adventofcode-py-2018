import sys
import re
from collections import Counter

matrix = Counter()

for line in sys.stdin:
    input_data = re.match(
        r'#(?P<rownumb>\d+) @ (?P<xcoord>\d+),(?P<ycoord>\d+): (?P<width>\d+)x(?P<height>\d+)', line)
    inputs = list(map(int, list(input_data.groups())))
    for i in range(inputs[3]):
        for j in range(inputs[4]):
            matrix[(inputs[2]+j, inputs[1]+i)] += 1

# Part 1 solution
print(len({k: v for k, v in matrix.items() if v > 1}.keys()))
