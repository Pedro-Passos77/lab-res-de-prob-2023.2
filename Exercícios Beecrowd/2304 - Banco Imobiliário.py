Q, jogos = map(int, input().split())
D = E = F = Q

for _ in range(jogos):
    operacao = list(map(str, input().split()))
    operacao[-1] = int(operacao[-1])

    if operacao[0] == 'C':
        if operacao[1] == 'D':
            D -= operacao[2]
        elif operacao[1] == 'E':
            E -= operacao[2]
        elif operacao[1] == 'F':
            F -= operacao[2]

    elif operacao[0] == 'V':
        if operacao[1] == 'D':
            D += operacao[2]
        elif operacao[1] == 'E':
            E += operacao[2]
        elif operacao[1] == 'F':
            F += operacao[2]

    elif operacao[0] == 'A':
        if operacao[1] == 'D':
            if operacao[2] == 'E':
                D += operacao[3]
                E -= operacao[3]
            elif operacao[2] == 'F':
                D += operacao[3]
                F -= operacao[3]
        elif operacao[1] == 'E':
            if operacao[2] == 'D':
                E += operacao[3]
                D -= operacao[3]
            elif operacao[2] == 'F':
                E += operacao[3]
                F -= operacao[3]
        elif operacao[1] == 'F':
            if operacao[2] == 'D':
                F += operacao[3]
                D -= operacao[3]
            elif operacao[2] == 'E':
                F += operacao[3]
                E -= operacao[3]

print(D, E, F)
