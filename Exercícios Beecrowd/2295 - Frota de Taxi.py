pa, pg, ka, kg = map(float, input().split())
ca = (ka / pa)
cg = (kg / pg)
if ca > cg:
    print('A')
if cg > ca:
    print('G')
elif cg == ca:
    print('G')