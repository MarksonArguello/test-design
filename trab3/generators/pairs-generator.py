arcos = ['1-2', '1-3', '3-4', '4-5', '4-6', '6-7', '7-8', '7-10', '8-9', '8-10', '9-7', '10-11', '10-12', '11-15', '12-13', '12-15', '13-15', '15-4']

pares = []

for i in range(len(arcos) - 1):
    for j in range(i + 1, len(arcos)):
        pares.append(f'({arcos[i]}, {arcos[j]})')

for i, par in enumerate(pares):
    endl = ', '
    if (i+1) % 8 == 0:
        endl = ',\n'
    print(par,end=endl)