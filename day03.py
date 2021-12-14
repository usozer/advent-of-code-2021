with open("data/day3.txt") as f:
    data = f.read()
    power = data.splitlines()

bits = len(power[0])
counts = [0]*bits
total = len(power)

for i in power:
    for pos in range(bits):
        counts[pos] += int(i[pos])

gamma = list(map(lambda x: '1' if ((x/total) >= 0.5) else '0', counts))
epsilon = list(map(lambda x: '0' if ((x/total) >= 0.5) else '1', counts))

print(int(''.join(gamma), base=2) * int(''.join(epsilon), base=2))

# Part 2
search_o2 = power[:]
search_co2 = power[:]

index = 0
while len(search_o2) > 1:
    digits = [int(x[index]) for x in search_o2]
    most_common = 1 if sum(digits)/len(digits) >= 0.5 else 0
    search_o2 = list(filter(lambda x: x[index] == str(most_common), search_o2))
    index += 1

index = 0
while len(search_co2) > 1:
    digits = [int(x[index]) for x in search_co2]
    most_common = 0 if sum(digits)/len(digits) >= 0.5 else 1
    search_co2 = list(filter(lambda x: x[index] == str(most_common), search_co2))
    index += 1

print(int(search_o2[0], base=2) * int(search_co2[0], base=2))