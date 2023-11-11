def banco(C, N, L):
  caixalist = [0] * C
  result = 0
  for ccc in L:
    valor = min(caixalist)
    indice = caixalist.index(valor)  
    caixalist[indice] += ccc[1]
    if valor - ccc[0] >= 20:
      result += 1
  return result