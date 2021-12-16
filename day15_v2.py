import numpy as np
from datetime import datetime
from heapq import heappop, heappush

def adjacent(x, y, v, w):
    """Get valid adjacent coordinates to the input coordinate"""
    # Can move up, down, left, right
    directions = np.array([[1,0], [0,1], [-1,0], [0,-1]])

    coords = directions + np.array([x,y])

    return [(x,y) for (x,y) in coords if (x >= 0) & (y >= 0) & (x < v) & (y < w)]


with open("data/day15.txt") as f:
    data = f.read()
    raw = data.splitlines()

    arrays = [[int(i) for i in row] for row in raw]
    # Cells represent (equal) edge lengths to adjacent nodes
    edges = np.array(arrays)


def find_min_cost(edges):
    start = datetime.now()
    v, w = edges.shape

    # Shortest distances from origin
    # Initialize as infinite
    dist = np.full(edges.shape, np.Inf)
    # If each node is checked or not
    q = np.full(edges.shape, True) # True if unvisited
    
    # prev = {(i,j):None for i in range(v) for j in range(w)}
    # Only needed if tracking the path

    # Initialize a priority queue, shorter distances are checked first
    # Avoids expensive lookups for minimum distance in the dist matrix
    # See v1
    h = []

    dist[0,0] = 0
    for i,j in adjacent(0,0,v,w):
        dist[i,j] = edges[i,j]
        heappush(h, (edges[i,j], (i,j)))

    while h:
        cur_dist, cur = heappop(h)
        q[cur] = False # Node is now checked
        
        cur_adj = adjacent(*cur, *dist.shape)

        for i,j in cur_adj:
            # For each adjacent cells not marked as "checked"
            if q[i,j]:
                # If a shorter path is found, update distance
                # Add new node to queue
                best = cur_dist + edges[i,j]
                if best < dist[i,j]:
                    dist[i,j] = best
                    # prev[i,j] = cur
                    heappush(h, (best, (i,j)))

    end = datetime.now()
    print("Distance to bottom:", dist[v-1,w-1])
    print("Execution time:", end-start)

find_min_cost(edges)

# Part 2

# Constructing the block as explained
dim_x, dim_y = 5, 5
blocks = {0:edges}

for i in range(1, dim_x+dim_y):
    cur_block = blocks[i-1] + 1
    blocks[i] = np.where(cur_block == 10, 1, cur_block)

bigger = np.block([[blocks[i+j] for i in range(dim_x)] for j in range(dim_y)])

# Improvement! From ~5min to ~3sec
find_min_cost(bigger)