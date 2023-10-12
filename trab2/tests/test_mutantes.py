# Testes para matar os mutantes restantes

import sys
sys.path.append('../')

from src.batida import colisao

def test_retangulos_iguais_colados_um_ao_lado_do_outro():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 2
  y3 = 0
  x4 = 4
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

def test_retangulos_iguais_separados_alturas_diferentes():
  # Retângulo 1
  x1 = 2
  y1 = 2
  x2 = 4
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 5
  x4 = 2
  y4 = 6
  
  valor_esperado = 0

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

