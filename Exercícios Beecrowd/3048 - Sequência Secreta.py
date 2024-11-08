N = int(input())
soma = 0
consec = 0
if N < 3 or N > 500:
    N = int(input())
for i in range(1, N+1):
    j = int(input())
    if j < 1 or j >2:
        j = int(input())
    if j != soma:
        consec += 1
        soma = j
print(consec)