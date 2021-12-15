import re

import numpy as np

with open("data/day13.txt") as f:
    data = f.read()
    raw = data.split("\n\n")

dots_list = raw[0].splitlines()
folds_list = raw[1].splitlines()

dots = []
for pair in dots_list:
    numbers = re.search("(\d+),(\d+)", pair)
    dots.append((int(numbers.group(2)), int(numbers.group(1))))

folds = []
for fold in folds_list:
    directions = re.search("fold along (\w)=(\d+)", fold)
    if directions.group(1) == "x":
        folds.append((int(directions.group(2)), "ver"))
    elif directions.group(1) == "y":
        folds.append((int(directions.group(2)), "hor"))


# Part 1
xmax = max([i[0] for i in dots])
ymax = max([i[1] for i in dots])

grid = np.zeros((xmax+1, ymax+1))

for dot in dots:
    grid[dot] = 1

if folds[0][1] == "ver":
    half1 = grid[:, 0:folds[0][0]]
    half2 = np.flip(grid[:, (folds[0][0]+1):], 1)
    
    folded = half1 + half2
    print(np.count_nonzero(folded))
elif folds[0][1] == "hor":
    half1 = grid[0:folds[0][0], :]
    half2 = np.flip(grid[(folds[0][0]+1):, :], 0)
    
    folded = half1 + half2
    print(np.count_nonzero(folded))

# Part 2
folded = grid.copy()

for fold in folds:
    if fold[1] == "ver":
        half1 = folded[:, 0:fold[0]]
        half2 = np.flip(folded[:, (fold[0]+1):], 1)
        
        folded = half1 + half2
    elif fold[1] == "hor":
        half1 = folded[0:fold[0], :]
        half2 = np.flip(folded[(fold[0]+1):, :], 0)
        
        folded = half1 + half2

print(np.where(folded > 0, 1, "."))