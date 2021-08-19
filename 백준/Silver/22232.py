# 가희와 파일 탐색기
import sys
from collections import defaultdict


N, M = map(int, sys.stdin.readline().split())
temp = []
ext = defaultdict()
for _ in range(N):
    name, extention = sys.stdin.readline().rstrip().split('.')
    ext[extention] = 'zzzzzzzzz'
    temp.append([name, extention])

for _ in range(M):
    ext[sys.stdin.readline().rstrip()] = 'a'

file = []
for name, extention in temp:
    file.append([name, ext[extention], extention])
file.sort()

for a, _, b in file:
    print(a + '.' + b)
