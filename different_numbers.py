with open("input.txt") as file:
    dlina = int(file.readline())
    seq = [int(x) for x in file.readline().split()]
seq = sorted(seq)
different = []

for x in range(0, dlina - 1):
    if x == dlina - 2:
        different.append(seq[dlina - 1])
        if different.count(seq[dlina - 2]) == 0:
            different.append((seq[dlina - 2]))
        break
    if seq[x] == seq[x + 1]:
        continue
    if seq[x] != seq[x + 1]:
        different.append(seq[x])
print(different)
file = open("output.txt", "w")
file.write(str(len(different)))
file.close()
