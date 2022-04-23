import sys
input = sys.stdin.readline
import heapq
from heapq import heapify, heappop, heappush

n, m = map(int, input().split())

adj = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a not in adj:
        adj[a] = {b}
    elif a in adj:
        adj[a].add(b)
    if b not in adj:
        adj[b] = {a}
    elif b in adj:
        adj[b].add(a)

timedd = []
heapify(timedd)


for j in range(1, n + 1):

    ad = [j]
    turn = 0
    hap = 0
    history = [j]
    while ad:
        turn += 1
        next, ad = ad, []
        #print(next)
        for play in next:
            hap += turn
            #print(adj[play])
            for player in adj[play]:
                #print(player)
                if player not in history:
                    history.append(player)
                    ad.append(player)

    heappush(timedd, (hap, j))
a,b = (heappop(timedd))
print(b)
