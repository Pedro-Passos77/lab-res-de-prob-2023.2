m1, m2, r1, r2 = map(int, input().split())
c1 = m1 - r1
if c1 < 0:
    c1 = -1 * c1
c2 = m2 - r2
if c2 < 0:
    c2 = -1 * c2
tot_cruzamentos = c1 + c2
print(tot_cruzamentos)