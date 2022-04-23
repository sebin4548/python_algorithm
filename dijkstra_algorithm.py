import sys
from math import inf
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

n, m = map(int, input().split())
num = int(input())
adj = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a not in adj:
        #adj[a] = {(b, c)}
        adj[a] = {b:c}
    elif a in adj:
    		if b not in adj[a]:
    				adj[a][b] = c
    		elif b in adj[a]:
    				adj[a][b] = min(adj[a][b], c)
    		
        #adj[a].add((b, c))
#print(adj)

answer = [0]
answer += list(inf for num in range(n))
answer[num] = 0


def dij(a):
    lis = [(answer[a], a)]
    heapify(lis)
    #print(lis)
    while lis:
        nex = heappop(lis)
        if nex[1] in adj:
		        for nextt in adj[nex[1]].items():
		                #			nextt[0] is next node to go, nex[1] is before node
		            if answer[nextt[0]] == inf:
		                answer[nextt[0]] = nex[0] + nextt[1]
		                #print("inf became", answer[nextt[0]])
		                heappush(lis, (answer[nextt[0]], nextt[0]))
		            elif answer[nex[1]] + nextt[1] < answer[nextt[0]]:
		                answer[nextt[0]] = answer[nex[1]] + nextt[1]
		                heappush(lis, (answer[nextt[0]], nextt[0]))
		            #print(answer)
		            #print(lis)
		        

dij(num)
for x in answer[1:]:
		if x == inf:
				print("INF")
		else:
				print(x)
