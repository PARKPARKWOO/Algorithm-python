from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in sorted(list(product(arr, repeat=m))):
    print(*i)