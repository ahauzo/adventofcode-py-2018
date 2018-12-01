import sys
import itertools

total = 0
items = []
freqs_count = {}
freq = 0
first_repeating_freq = 0

for line in sys.stdin:
    items.append(int(line))


print(sum(items))  # Part 1 answer

freqs_count[0] = 1
for element in itertools.cycle(items):
    freq = freq + element
    freqs_count[freq] = freqs_count[freq] + 1 if freq in freqs_count else 1
    if freqs_count[freq] > 1:
        first_repeating_freq = freq
        break

print(first_repeating_freq)  # Part 2 answer
