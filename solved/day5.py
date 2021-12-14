import numpy as np
import re

with open("day5.txt") as f:
    data = f.read()
    coords = data.splitlines()

matches = [re.match(r"(\d+),(\d+) -> (\d+),(\d+)", x) for x in coords]
lines = [[int(x.group(i)) for i in range(1,5)] for x in matches]

# Part 1
straight = list(filter(lambda x: ((x[0] == x[2]) or x[1] == x[3]), lines))

pts = []
for fault in straight:
    start = np.array([fault[0], fault[1]])
    dist = np.array([fault[2]-fault[0], fault[3] - fault[1]])

    for i in range(np.abs(sum(dist))+1):
        pts.append((i*(dist/np.abs(sum(dist))) + start).astype(int))

status = np.full((1000,1000), 0)
for pt in pts:
    status[tuple(pt)] += 1

print(np.sum(status > 1, axis=None))


# Part 2
pts = []
for fault in lines:
    start = np.array([fault[0], fault[1]])
    dist = np.array([fault[2]-fault[0], fault[3] - fault[1]])
    
    length = np.abs(dist).max()
    for i in range(length+1):
        pts.append((i*(dist/length) + start).astype(int))

status = np.full((1000,1000), 0)
for pt in pts:
    status[tuple(pt)] += 1

print(np.sum(status > 1, axis=None))