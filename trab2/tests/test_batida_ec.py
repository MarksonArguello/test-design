# Casos de Testes: Each Choice

import sys
sys.path.append('../')

from src.batida import colisao

# Caso 1: Retângulos iguais separados na mesma altura
def test_retangulos_iguais_separados_mesma_altura():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 3
  y3 = 0
  x4 = 5
  y4 = 1

  valor_esperado = 0

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 2: Retângulos iguais separados em alturas diferentes
def test_retangulos_iguais_separados_alturas_diferentes():
  # Retângulo 1
  x1 = 3
  y1 = 2
  x2 = 5
  y2 = 3

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 0

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 3: Retângulos iguais colados um em cima do outro
def test_retangulos_iguais_colados_um_em_cima_do_outro():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 1
  x4 = 2
  y4 = 2
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 4: Retângulos iguais com intersecção em um ponto
def test_retangulos_iguais_interseccao_em_um_ponto():
  # Retângulo 1
  x1 = 2
  y1 = 1
  x2 = 4
  y2 = 2

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 5: Retângulos iguais com um lado na mesma vertical
def test_retangulos_iguais_com_um_lado_mesma_vertical():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 2
  y3 = 2
  x4 = 4
  y4 = 3
  
  valor_esperado = 0

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado