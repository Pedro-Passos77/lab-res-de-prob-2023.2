x = int(input())
y = 0
for i in range(x):
    L,C = map(int, input().split())
    if L <= C:
        y += 0
    else:
        y += C
print(y)