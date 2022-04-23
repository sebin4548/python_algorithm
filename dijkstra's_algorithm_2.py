import sys

input = sys.stdin.readline
from math import inf
from heapq import heappush, heappop, heapify

n = int(input())
m = int(input())
adj = {}
dist = [0]
dist += [inf for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in adj:
        adj[a] = {b: c}
    elif a in adj:
        if b in adj[a]:
            adj[a][b] = min(c, adj[a][b])
        else:
            adj[a][b] = c

a, b = map(int, input().split())
dist[a] = 0
dist_heap = [(0, a)]
heapify(dist_heap)
while dist_heap:
    dist_now, now = heappop(dist_heap)
    if now in adj:
        for x in adj[now]:
            if dist[x] == inf:
                dist[x] = dist_now + adj[now][x]
                heappush(dist_heap, (dist[x], x))

            elif dist[x] > (dist_now + adj[now][x]):
                dist[x] = dist_now + adj[now][x]
                heappush(dist_heap, (dist[x], x))
print(dist[b])

