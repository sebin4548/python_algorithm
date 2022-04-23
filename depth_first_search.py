from collections import deque
n, m, k = map(int, input().split())
graph = {}
for _ in range(m):
		a = list(map(int, input().split()))
		
		if a[0] not in graph:
				graph[a[0]] = [a[1]]
		elif a[0] in graph:
				graph[a[0]].append(a[1])
				graph[a[0]].sort()
		if a[1] not in graph:
				graph[a[1]] = [a[0]]
		elif a[1] in graph:
				graph[a[1]].append(a[0])
				graph[a[1]].sort()
			
def dfs(graph, v, visited):
		visited[v] = True
		print(v, end = ' ')
		for i in graph[v]:
				if not visited[i]:
						dfs(graph, i, visited)
						
def bfs(graph,start, visited):
		queue = deque([start])
		visited[start] = True
		while queue:
				v = queue.popleft()
				print(v, end = ' ')
				for i in graph[v]:
						if not visited[i]:
								queue.append(i)
								visited[i] = True		
visited = [False] * (n + 1)
visit = [False] * (n + 1)
if k not in graph:
		print(k)
		print(k)
else:
	
		dfs(graph, k, visited)
		print()
		bfs(graph, k, visit)


