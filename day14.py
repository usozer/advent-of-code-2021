import re
from collections import Counter

import numpy as np

with open("data/day14.txt") as f:
    data = f.read()
    raw = data.splitlines()

first = np.array(list(raw[0]))

rules = {}
for rule in raw[2:]:
    cur = re.search("(\w\w) -> (\w)", rule)
    rules[cur.group(1)] = cur.group(2)

# Part 1
starter = first.copy()

for _ in range(10):
    # Split polymer into its dimers
    dimers = [starter[i-1]+starter[i] for i in range(1,len(starter))]

    # Translate polymers to what it would yield
    new_monomer = [rules[dimer] for dimer in dimers]

    # Insert new monomers
    starter = np.insert(starter, range(1,len(starter)), new_monomer)

elements = Counter(starter)

values = sorted(elements.values(), reverse=True)

print(values[0]-values[-1])

# Part 2
translations = {}

# Translate each dimer into its two output dimers (rules dictionary)
for dimer in rules.keys():
    components = list(dimer)
    results = [components[0]+rules[dimer], rules[dimer]+components[1]]
    translations[dimer] = results

# Split starter into dimers
starter = [first[i-1]+first[i] for i in range(1,len(first))]

# Add how many of each dimer
polymer = {dimer:0 for dimer in translations.keys()}
for dimer in starter:
    polymer[dimer] += 1

for _ in range(40):
    progress = polymer.copy()

    # Add two output dimers into total count, then remove all the previous dimers
    for dimer in polymer.keys():
        for output in translations[dimer]:
            progress[output] += polymer[dimer]
        progress[dimer] -= polymer[dimer]
    
    polymer = progress.copy()

# Decoding, counting how many of monomers exist based on counts of dimers
monomers = {}

# Add one monomer for each monomer in each dimer
for dimer in polymer.keys():
    components = list(dimer)

    for monomer in components:
        monomers[monomer] = monomers.get(monomer, 0) + polymer[dimer]

# Remove end monomers which won't change
monomers[first[0]] -= 1
monomers[first[-1]] -= 1

# Each monomer was counted twice because of how it's modeled,
# divide counts by 2
monomers = {x:monomers[x]/2 for x in monomers.keys()}

# Re-add end monomers which won't change
monomers[first[0]] += 1
monomers[first[-1]] += 1

values = sorted(monomers.values(), reverse=True)

print(values[0]-values[-1])