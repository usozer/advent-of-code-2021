with open("data/day1.txt") as f:
    data = f.read()
    depths_raw = data.splitlines()
    depths = list(map(int, depths_raw))

# Part 1
larger = 0
for i in range(1, len(depths)):
    larger += int(depths[i] > depths[i-1])

print(larger)

# Part 2
windows = []
for i in range(len(depths)-2):
    windows.append(sum([depths[i], depths[i+1], depths[i+2]]))

larger = 0
for i in range(1, len(windows)):
    larger += int(windows[i] > windows[i-1])

print(larger)