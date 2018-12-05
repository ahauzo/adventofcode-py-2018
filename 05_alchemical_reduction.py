def reduce(polymer):
    chars = []
    matchFound = True

    for i in polymer:
        chars.append(i)

    while matchFound:
        matchFound = False
        for idx, val in enumerate(chars[:-1]):
            if chars[idx].swapcase() == chars[idx+1]:
                matchFound = True
                chars.pop(idx)
                chars.pop(idx)
                break
    return(len(chars))


results = {}

inputval = 'dabAcCaCBAcCcaDA'
print(reduce(inputval))

for idx, val in enumerate(['a', 'b', 'c', 'd']):
    results[val] = reduce(inputval.replace(
        val, "").replace(val.swapcase(), ""))

print(min(results.values()))
