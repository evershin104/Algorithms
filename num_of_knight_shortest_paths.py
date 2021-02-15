import collections
# Make queue
q = collections.deque()

# Init chess area
with open("input.txt") as file:
    n = int(file.readline())

if n == 2:
    with open("output.txt", "w") as file:
        file.write(str(0))

if n == 1:
    with open("output.txt", "w") as file:
        file.write(str(1))


area = [[0] * n for i in range(0, n)]
area[0][0] = 1

# All knight's moves combinations
moves = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

# Area of number of moves to defined point
d = [[0] * n for j in range(0, n)]

# Find adjacent vertices for (i, j) point
def AdjVerts(i, j):
    adjacent = []
    for k in range(0, len(moves)):
        if (i + moves[k][0] in range(0, n)) and (j + moves[k][1] in range(0, n)):
            adjacent.append([i + moves[k][0], j + moves[k][1]])
    return adjacent

# Main program
q.append([0, 0])
while len(q) != 0:
    [i, j] = q.popleft()
    # [x1, x2] adjacent vertex for i, j point
    for [x1, x2] in AdjVerts(i, j):
        # BFS with counter
        if d[x1][x2] == 0:
            area[x1][x2] = area[i][j]
            d[x1][x2] = 1 + d[i][j]
            q.append([x1, x2])
        else:
            if d[x1][x2] == d[i][j] + 1:
                area[x1][x2] += area[i][j]
            else:
                d[x1][x2] = min(d[x1][x2], d[i][j] + 1)

with open("output.txt", "w") as file:
    file.write(str(area[n - 1][n - 1]))
