N = int(input())
k = 100000
if N < 1.0 or N > 100.0:
    N = int(input())
for i in range(1, N+1):
    p, g = map(float, input().split())
    if p < 0 or p > 1000.0:
        p, g = map(float, input().split())
    if g < 1.0 or g > 1000.0:
        p, g = map(float, input().split())
    pkg = (p/g) * 1000
    if pkg < k:
        k = pkg
print('%.2f' % k)