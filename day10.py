with open("data/day10.txt") as f:
    data = f.read()
    raw = data.splitlines()

    processed = [list(x) for x in raw]

def check_signal(order):
    signals = []
    valid = True

    valid_pairs = [("{", "}"), ("(", ")"), ("<", ">"), ("[", "]")]

    scores = {")":3, "]":57, "}":1197, ">":25137}

    for i in range(len(order)):
        if order[i] in ("(", "[", "<", "{"):
            signals.append(order[i])
        elif order[i] in (")", "]", ">", "}"):
            opener = signals.pop()
            
            if not ((opener, order[i]) in valid_pairs):
                valid=False
                return valid, scores[order[i]]
    
    return valid, 0, signals

# Part 1
totals = []
for signallist in processed:
    cur = check_signal(signallist)
    totals.append(cur[1])

print(sum(totals))

# Part 2
completions = []
vals = {"(":1, "[":2, "{":3, "<":4}

for signallist in processed:
    score = 0
    cur = check_signal(signallist)
    if cur[0]:
        autocomplete = reversed(cur[2])

        for i in autocomplete:
            score = (score * 5) + vals[i]
        completions.append(score)

print(sorted(completions)[int((len(completions)/2)-0.5)])
