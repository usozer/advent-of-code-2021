import numpy as np

with open("data/day4.txt") as f:
    data = f.read()
    bingo = data.splitlines()

draw = [int(x) for x in bingo[0].split(',')]

no_boards = (len(bingo)-1) // 6
boards = []
statuses = []
for i in range(no_boards):
    current = []
    for row in range(5):
        current.append(bingo[2+ 6*i +row].split())
    
    boards.append(np.array(current).astype(int))
    statuses.append(np.full((5,5), False))

def check_bingo(board_status):
    rowsum = (board_status.sum(axis=0) == 5).any()
    colsum = (board_status.sum(axis=1) == 5).any()

    return (rowsum or colsum)

# Part 1
cur = 0
turn = -1
winner = -1
cont = False

while not cont:
    turn += 1
    cur = draw[turn]
    for i in range(no_boards):
        check = boards[i] == draw[turn]
        statuses[i] = np.logical_or(check, statuses[i])
    
    cont = any(map(check_bingo, statuses))
    if cont:
        winner = list(map(check_bingo, statuses)).index(True)

print((boards[winner] * ~statuses[winner]).sum() * cur)

# Part 2

statuses = []
for i in range(no_boards):
    statuses.append(np.full((5,5), False))

cur = 0
turn = -1
last = -1
cont = False

while not cont:
    turn += 1
    cur = draw[turn]
    for i in range(no_boards):
        check = boards[i] == draw[turn]
        statuses[i] = np.logical_or(check, statuses[i])

        cont = all(map(check_bingo, statuses))
        if cont:
            last = i
            break

print((boards[last] * ~statuses[last]).sum() * cur)