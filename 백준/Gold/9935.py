import sys
import time

# String = sys.stdin.readline().rstrip()
# target = sys.stdin.readline().rstrip()

String = 'a' * 500000 + 'b' * 500000
target = 'ab'

length = len(target)
stack = []
start = time.time()

for i in range(length - 1):
    stack.append(String[i])
idx = length - 1

while idx < len(String):
    stack.append(String[idx])
    idx += 1

    k = len(stack) - length
    if stack[k:] == list(target):
        stack = stack[:-length]

print(time.time() - start)
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))