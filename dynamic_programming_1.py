import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lis = [1 for _ in range(len(arr))]

for i in range(n):
		for j in range(i):
				if arr[i]> arr[j]:
						lis[i] = max(lis[j] + 1, lis[i] )
						
print(max(lis))
