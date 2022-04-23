import sys
from math import inf
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

n, e = map(int, input().split())
adj = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    if a not in adj:
        #adj[a] = {(b, c)}
        adj[a] = {b:c}
    elif a in adj:
    		if b not in adj[a]:
    				adj[a][b] = c
    		elif b in adj[a]:
    				adj[a][b] = min(adj[a][b], c)
    if b not in adj:
        #adj[a] = {(b, c)}
        adj[b] = {a:c}
    elif b in adj:
    		if a not in adj[b]:
    				adj[b][a] = c
    		elif a in adj[b]:
    				adj[b][a] = min(adj[b][a], c)    		
        #adj[a].add((b, c))
v1,v2 = map(int, input().split())




def dij(a,b):
    answer = [0]
    answer += list(inf for num in range(n))
    answer[a] = 0
    lis = [(0, a)]
    heapify(lis)
    #print(lis)
    while lis:
        nex = heappop(lis)
        if nex[1] in adj:
            for nextt in adj[nex[1]].items():
                if answer[nextt[0]] == inf:
                    answer[nextt[0]] = nex[0] + nextt[1]
                    heappush(lis, (answer[nextt[0]], nextt[0]))
                elif answer[nex[1]] + nextt[1] < answer[nextt[0]]:
                    answer[nextt[0]] = answer[nex[1]] + nextt[1]
                    heappush(lis, (answer[nextt[0]], nextt[0]))
    	                
    return answer[b]
			#return answer[b]


dap1 = dij(1,v1) + dij(v1,v2) + dij(v2, n)
dap2 = dij(1,v2) + dij(v2,v1) + dij(v1, n)


if dap1 == inf and dap2 == inf:
		print(-1)
else:
		print(min(dap1, dap2))

