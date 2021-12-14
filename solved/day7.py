import numpy as np

with open("day7.txt") as f:
    data = f.read()
    raw = data.split(",")

pos = np.array(raw, "int")

median = np.median(pos)

print(np.sum(np.abs(pos-median)))

# Part 2

low = np.floor(pos.mean())
high = np.ceil(pos.mean())

low_dist = np.sum((np.abs(pos-low)*(np.abs(pos-low)+1))/2)
high_dist = np.sum((np.abs(pos-high)*(np.abs(pos-high)+1))/2)

print(np.min([low_dist, high_dist]))
