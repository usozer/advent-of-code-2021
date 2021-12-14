import numpy as np
from collections import Counter

with open("day6.txt") as f:
    data = f.read()
    raw = data.split(",")

fish = np.array(raw, "int")

def simulate(fish, no_days):
    day = 0

    for _ in range(no_days):
        birth = np.where(fish == 0)[0]
        np.put(fish, birth, 7)

        fish = np.append(fish, np.full(np.size(birth), 9))
        day += 1
        fish -= 1
    
    return np.size(fish)

# Part 1
print(simulate(fish, 80))

# Part 2
def simulate2(fish, no_days):
    begin = Counter(fish)
    totals = np.full(9, 0)

    for key in begin.keys():
        totals[key] = begin[key]

    day = 0
    for _ in range(no_days):
        day += 1
        totals = np.roll(totals, -1)
        totals[6] += totals[8]
    
    return sum(totals)

print(simulate2(fish, 80))
print(simulate2(fish, 256))