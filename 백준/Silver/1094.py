N = int(input())
print(list(map(int, list(bin(N)[2:]))).count(1))
