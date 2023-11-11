# Casos de Testes: Edge Coverage

import sys
sys.path.append('../')

from src.banco_fila import banco


# Caso 1
def test_caso_1():
  # Clientes (N)
  n = 1

  # Caixas (C)
  c = 2

  # Tempos
  tempos = [[0, 5]]
  
  valor_esperado = 0

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado

# Caso 2
def test_caso_2():
  # Clientes (N)
  n = 1

  # Caixas (C)
  c = 1

  # Tempos
  tempos = [[0, 2]]
  
  valor_esperado = 0

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado

# Caso 3
def test_caso_3():
  # Clientes (N)
  n = 2

  # Caixas (C)
  c = 2

  # Tempos
  tempos = [[0, 4], [1, 5]]
  
  valor_esperado = 0

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado

# Caso 4
def test_caso_4():
  # Clientes (N)
  n = 3

  # Caixas (C)
  c = 2

  # Tempos
  tempos = [[0, 20], [0, 20], [21,20]]
  
  valor_esperado = 0

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado

# Caso 5
def test_caso_5():
  # Clientes (N)
  n = 2

  # Caixas (C)
  c = 1

  # Tempos
  tempos = [[0, 20], [0, 20]]
  
  valor_esperado = 1

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado

# Caso 6
def test_caso_6():
  # Clientes (N)
  n = 2

  # Caixas (C)
  c = 1

  # Tempos
  tempos = [[0, 19], [0, 19]]
  
  valor_esperado = 0

  retorno = banco(c, n, tempos)
  
  assert retorno == valor_esperado