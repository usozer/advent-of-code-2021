import numpy as np
from datetime import datetime

def adjacent(x, y, v, w):
    """Get valid adjacent coordinates to the input coordinate"""
    directions = np.array([[1,0], [0,1], [-1,0], [0,-1]])

    coords = directions + np.array([x,y])

    return [(x,y) for (x,y) in coords if (x >= 0) & (y >= 0) & (x < v) & (y < w)]


with open("data/day15.txt") as f:
    data = f.read()
    raw = data.splitlines()

    arrays = [[int(i) for i in row] for row in raw]
    edges = np.array(arrays)

def find_min_cost(edges):
    start = datetime.now()
    v, w = edges.shape

    dist = np.full(edges.shape, np.Inf)
    q = np.full(edges.shape, True) # True if unvisited
    #prev = {(i,j):None for i in range(v) for j in range(w)}

    dist[0,0] = 0
    for i,j in adjacent(0,0,v,w):
        dist[i,j] = edges[i,j]

    while (np.flatnonzero(q).size > 0):
        dist_nonzero = np.where(dist*q != 0, dist*q, np.Inf)

        cur = np.unravel_index(np.argmin(dist_nonzero, axis=None), dist_nonzero.shape)
        #print(cur)
        q[cur] = False
        
        cur_adj = adjacent(*cur, *dist.shape)

        for i,j in cur_adj:
            if q[i,j]:
                best = dist[cur] + edges[i,j]
                if best < dist[i,j]:
                    dist[i,j] = best
                    #prev[i,j] = cur
        
        # if (cur == (v-1,w-1)):
        #     print("Distance to bottom:", dist[v-1,w-1])
        #     return
    end = datetime.now()
    print("Distance to bottom:", dist[v-1,w-1])
    print("Execution time:", end-start)

find_min_cost(edges)

# Part 2

dim_x, dim_y = 5, 5

blocks = {0:edges}

for i in range(1, dim_x+dim_y):
    cur_block = blocks[i-1] + 1
    blocks[i] = np.where(cur_block == 10, 1, cur_block)

bigger = np.block([[blocks[i+j] for i in range(dim_x)] for j in range(dim_y)])

find_min_cost(bigger)