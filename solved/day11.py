import numpy as np

with open("day11.txt") as f:
    data = f.read()
    raw = data.splitlines()

    arrays = [[int(i) for i in row] for row in raw]
    grid = np.array(arrays)

def adjacent(x, y, v, w):
    """Get valid adjacent coordinates to the input coordinate"""
    directions = np.array([[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]])

    coords = directions + np.array([x,y])

    return [(x,y) for (x,y) in coords if (x >= 0) & (y >= 0) & (x < v) & (y < w)]

# Part 1

def simulate(grid, steps=100):
    input_grid = grid.copy()
    
    v, w = input_grid.shape
    flash_count = 0
    
    for _ in range(steps):
        # No octopi flashing
        flashing = []
        # Increase all energy by 1
        input_grid += 1
        
        # Save which octopi flashed
        flashing += np.argwhere(input_grid > 9).tolist()
        flash_count += len(flashing)

        # Loop when there are octopi that flashed but not yet influenced its environment
        while flashing:
            x,y = flashing.pop()
            # Check if there are any octopi around that hasn't flashed
            look = [(x,y) for (x,y) in adjacent(x, y, v, w) if input_grid[x,y]<=9]
            
            # Each octopi that newly flashed
            for i,j in look:
                # Increase energy by 1
                input_grid[i,j] += 1

                # If flashed, add them to consideration list
                if input_grid[i,j] > 9:
                    flashing.append([i,j])
                    flash_count += 1
        
        # Set all octopi that flashed in this step to energy level 0
        input_grid = np.where(input_grid <= 9, input_grid, 0)
    return flash_count

print(simulate(grid, 100))

# Part 2

def simulate_sync(grid, steps=100):
    input_grid = grid.copy()
    
    v, w = input_grid.shape
    
    for t in range(1, steps):
        # No octopi flashing
        flashing = []
        # Increase all energy by 1
        input_grid += 1
        
        # Save which octopi flashed
        flashing += np.argwhere(input_grid > 9).tolist()

        # Loop when there are octopi that flashed but not yet influenced its environment
        while flashing:
            x,y = flashing.pop()
            # Check if there are any octopi around that hasn't flashed
            look = [(x,y) for (x,y) in adjacent(x, y, v, w) if input_grid[x,y]<=9]
            
            # Each octopi that newly flashed
            for i,j in look:
                # Increase energy by 1
                input_grid[i,j] += 1
                # If flashed, add them to consideration list
                if input_grid[i,j] > 9:
                    flashing.append([i,j])
        
        # Set all octopi that flashed in this step to energy level 0
        input_grid = np.where(input_grid <= 9, input_grid, 0)

        # If all octopi flashed, end loop and return time
        if all((input_grid == 0).flatten()):
            return t
    
    # If no sync occurred, return 0
    return 0

print(simulate_sync(grid, 100000))

