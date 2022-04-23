import sys
from math import inf
from itertools import combinations
input = sys.stdin.readline
l,c = map(int,input().split())
lis = input().split()
lis.sort()

dic = {}
for nc in lis:
		if nc == 'a' or nc == 'e'or nc == 'i'or nc == 'o'or nc == 'u':
				dic[nc] = 'mo'
		else: 
				dic[nc] = 'ja'
comb = combinations(lis, l)
for word in comb:
		moe, jae = 0,0
		for char in word:
				if dic[char] == 'mo':
						moe += 1
				elif dic[char] == 'ja':
						jae += 1
		if moe >= 1 and jae >= 2:
				for char in word:
						print(char, end = '')
				print()
