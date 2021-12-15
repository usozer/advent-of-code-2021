import re
from collections import Counter

with open("data/day12.txt") as f:
    data = f.read()
    raw = data.splitlines()

# Get all unique cave names
cave_names = set()
for x in raw:
    cur = re.search("(\w+)-(\w+)", x)
    cave_names = cave_names | {cur.group(1), cur.group(2)}

# Construct graph
# No vertex can go back to start
# end has no connections
graph = {cave:[] for cave in cave_names}

for connection in raw:
    cur = re.search("(\w+)-(\w+)", connection)

    graph[cur.group(1)].append(cur.group(2))
    if cur.group(1) != "start":
        graph[cur.group(2)].append(cur.group(1))
graph["end"] = []

# Part 1
paths = [[]]

def traverse(graph, current, visited):
    """Get all paths from a graph"""
    visited.append(current)
    for vertex in graph[current]:
        # If small cave not in visit list or it is a large cave
        if (vertex not in visited) or (vertex.isupper()):
            traverse(graph, vertex, visited.copy())
    paths.append(visited)

traverse(graph, "start", [])

# Only valid paths are ones that end at "end"
valid = [path for path in paths if (len(path) > 0) and (path[-1] == "end")]
print(len(valid))

# Part 2
def check_validity(vertex, visited):
    valid = False

    # Can visit if it's large cave
    if vertex.isupper():
        valid = True
    # If it is a small cave
    else:
        counts = Counter(visited)
        small = [counts[key] for key in counts.keys() if key.islower()]
        # Check if any small cave was visited twice
        if 2 not in small:
            valid = True
        # If there's one small cave visited twice, only visit if it hasn't been visited
        else:
            if vertex not in visited:
                valid = True
        
    return valid


paths = [[]]

def traverse(graph, current, visited):
    """Get all paths from a graph"""
    visited.append(current)
    for vertex in graph[current]:
        if check_validity(vertex, visited):
            traverse(graph, vertex, visited.copy())
    paths.append(visited)

traverse(graph, "start", [])

valid = [path for path in paths if (len(path) > 0) and (path[-1] == "end")]
print(len(valid))