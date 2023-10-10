sym = ["x", "y"]
operadores = ['>', '<', '=']

requisitos = []
for s in sym:
    for i in range(2): # 0 e 1
        for j in range(2): # segundo 0 e 1
            linha = []
            for op in operadores:
               linha.append(f"{s}'_{i} {op} {s}''_{j}")
            requisitos.append(linha)
            
            
pairs = []
for i in range(len(requisitos)):
    for j in range(i+1, len(requisitos)):
        for k in range(3):
            for l in range(3):
                pairs.append(f"({requisitos[i][k]},{requisitos[j][l]})")
                
for i in range(len(pairs)):
    print(pairs[i], end=',')
    if i > 0 and (i+1) % 3 == 0:
        print(' \\\\')
    



