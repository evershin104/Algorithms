# Первый обход в глубину с заполнением стека
def dfs1(vertex):
    visited[vertex] = True
    for adj in graph[vertex]:
        if not visited[adj - 1]:
            dfs1(adj - 1)
    stack.append(vertex + 1)

# Обход в глубину инвертированного графа с заполнением КСС
def dfs2(v, k):
    visited[v] = True
    Components[v] = k
    for adj in transposed[v]:
        if not visited[adj - 1]:
            dfs2(adj - 1, k)


# Input data
with open("input.txt", "r") as In:
    n, m = map(int, In.readline().split())
    graph = [[] for j in range(n)]
    transposed = [[] for j in range(n)]
    for i in range(0, m):
        data = In.readline().split()
        graph[int(data[0]) - 1].append(int(data[1]))
        transposed[int(data[1]) - 1].append(int(data[0]))


Components = [0] * n
stack = []
visited = [False] * n

# Первый обход
for i in range(0, n):
    if not visited[i]:
        dfs1(i)

visited = [False] * n
k = 0
# Второй обход
while len(stack) != 0:
    v = stack.pop() - 1
    if not visited[v]:
        k += 1
        dfs2(v, k)


with open("output.txt", "w") as Out:
    Out.write(str(max(Components)) + "\n")
    Out.write(str(Components).replace(",", "").replace("[", "").replace("]", ""))
