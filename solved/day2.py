import re

with open("day2.txt") as f:
    data = f.read()
    pos = data.splitlines()

# Part 1
vertical = 0
horizontal = 0

for i in pos:
    cur = re.match(r"(\w+) (\d+)", i)
    if cur.group(1) == "forward":
        horizontal += int(cur.group(2))
    elif cur.group(1) == "up":
        vertical -= int(cur.group(2))
    elif cur.group(1) == "down":
        vertical += int(cur.group(2))

print(vertical * horizontal)

# Part 2
# Part 1
vertical = 0
horizontal = 0
aim = 0

for i in pos:
    cur = re.match(r"(\w+) (\d+)", i)
    if cur.group(1) == "forward":
        horizontal += int(cur.group(2))
        vertical += aim * int(cur.group(2))
    elif cur.group(1) == "up":
        aim -= int(cur.group(2))
    elif cur.group(1) == "down":
        aim += int(cur.group(2))

print(vertical * horizontal)