class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0]* self.V for i in range(self.V)]
        self.level = [0] * self.V

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    def minDistance(self, dist, sptSet, low, high):
        minimum =  float('Inf')
        for u in range(self.V):
            if dist[u] < minimum and sptSet[u] == False:
                minimum = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src, low, high):
        dist = [float('Inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for v in range(self.V):
            u = self.minDistance(dist, sptSet, low, high)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print(f'Distance from {src}')
        for v in range(self.V):
            print(f'{v}:\t{dist[v]}')







m, n = [int(i) for i in input().split()]
g = Graph(n+1)
for itemNum in range(1, n+1):
    p, l, x = [int(i) for i in input().split()]
    g.addEdge(0, itemNum, p)
    g.level[itemNum] = l
    for _ in range(x):
        t, v = [int(i) for i in input().split()]
        g.addEdge(t, itemNum, v)

print(g.graph)
print(g.level)
ans = float('Inf')
for low_level in range(g.level[1] - m, g.level[1] + 1):
    ans = min(ans, g.dijkstra(0, low_level, low_level+m))
