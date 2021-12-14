import numpy as np

with open("data/day9.txt") as f:
    data = f.read()
    raw = data.splitlines()

    arrays = [[int(i) for i in row] for row in raw]
    grid = np.array(arrays)

# Part 1
def adjacent(x, y, v, w):
    """Get valid adjacent coordinates to the input coordinate"""
    directions = np.array([[1,0], [0,1], [-1,0], [0,-1]])

    coords = directions + np.array([x,y])

    return [(x,y) for (x,y) in coords if (x >= 0) & (y >= 0) & (x < v) & (y < w)]

v, w = grid.shape

lows = []
for i in range(v):
    for j in range(w):
        look = adjacent(i, j, v, w)
        evals = [grid[x,y] > grid[i,j] for x,y in look]
        if all(evals):
            lows.append((grid[i,j], i, j))

print(sum([x[0]+1 for x in lows]))

# Part 2

# Initialize a new grid with borders (9) defined
basins = np.where(grid!=9, 0, -1)

z = 1

for i in range(v):
    for j in range(w):
        # Queue of coordinates to consider
        consider = []

        # Only check if it hasn't been checked
        if basins[i,j] == 0:
            # Add coordinate to list
            consider.append((i,j))
            # Loop while there are coordinates to check
            while consider:
                x,y = consider.pop()
                # Mark current coordinate with basin number
                basins[x,y] = z

                # Determine unchecked adjacent cells
                look = [(x,y) for (x,y) in adjacent(x, y, v, w) if basins[x,y]==0]
                # Add coordinates to consideration
                consider += look

            # When basin is exhausted, increase basin number by 1
            z += 1
        else:
            pass

# Sizes of each basin number
sizes = [np.count_nonzero(basins == i) for i in range(1, z)]
sizes.sort(reverse=True)

print(sizes[0]*sizes[1]*sizes[2])