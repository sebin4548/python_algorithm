import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())


adj = {}
visisted = {}
for _ in range(m):
		a,b = map(int, input().split())
		if a not in adj:
				adj[a] = {b}
				visisted[a] = True
		elif a in adj:
				adj[a].add(b)
		if b not in adj:
				visisted[b] = True
				adj[b] = {a}
		elif b in adj:
				adj[b].add(a)

def bfs(key, adj,visisted):
		travel = deque()
		travel.append(key)
		while(travel):
				a = travel.popleft()
				for next in adj[a]:
						if visisted[next] == True:
								travel.append(next)
								visisted[next] = False
count = 0																		
for key in adj:
		if visisted[key] == True:				
				visisted[key] = False
				bfs(key, adj, visisted)
				count += 1
not_connected = n - len(adj)
print(count + not_connected)
