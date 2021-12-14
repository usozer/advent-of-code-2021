import re

with open("data/day8.txt") as f:
    data = f.read()
    raw = data.splitlines()

# Part 1
total = 0
for line in raw:
    match = re.search('(?<=\| )(.*)', line)

    unique = [i for i in match.group(1).split() if len(i) in (2, 3, 4, 7)]
    total += len(unique)

print(total)

# Part 2
decoder = []
code = []

for line in raw:
    match = re.search('(.*) \| (.*)', line)

    decoder.append(match.group(1).split())
    code.append(match.group(2).split())

def decode(signal):
    
    digits = [set(list(digit)) for digit in signal]
    
    solved = {}
    fives = []
    sixes = []

    for x in digits:
        size = len(x)
        if size == 2:
            solved[1] = x
        elif size == 3:
            solved[7] = x
        elif size == 4:
            solved[4] = x
        elif size == 5:
            fives.append(x)
        elif size == 6:
            sixes.append(x)
        elif size == 7:
            solved[8] = x
    
    inters = fives[0] & fives[1] & fives[2]

    solved[3] = inters | solved[1]
    solved[9] = inters | solved[4]

    solved[0] = solved[8] - (inters & solved[4])
    
    solved[6] = [set for set in sixes if set not in (solved[0], solved[9])][0]

    solved[5] = solved[6] & solved[9]
    solved[2] = [set for set in fives if set not in (solved[3], solved[5])][0]

    return solved

numbers = []

for i in range(len(decoder)):
    rosetta = decode(decoder[i])

    digits = []
    for digit in code[i]:
        digits += [x for x in rosetta.keys() if rosetta[x]==set(list(digit))]

    numbers.append(1000*digits[0] + 100*digits[1] + 10*digits[2] + digits[3])

print(sum(numbers))