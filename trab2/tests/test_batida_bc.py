# Casos de Testes: ase choice

import sys
sys.path.append('../')

from src.batida import colisao


# Caso 1: Retângulos iguais no mesmo lugar
def test_retangulos_iguais_no_mesmo_lugar():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 2: Retângulos de coordenada x1 e x3 diferente sobrepostos
def test_retangulos_de_coordenada_x1_e_x3_diferente_sobrepostos():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 1
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 3: Retângulos de coordenada x1 e x3 diferente sobrepostos invertido
def test_retangulos_de_coordenada_x1_e_x3_diferente_sobrepostos_invertido():
  # Retângulo 1
  x1 = 1
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 4: Retângulos de coordenada x2 e x4 diferente sobreposto
def test_retangulos_de_coordenada_x2_x4_diferente_sobreposto():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 3
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 5: Retângulos de coordenada x2 e x4 diferente sobreposto invertido
def test_retangulos_de_coordenada_x2_x4_diferente_sobreposto_invertido():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 3
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 6: Retângulos de coordenada y1 e y3 diferente sobreposto
def test_retangulos_de_coordenada_y1_y3_diferente_sobreposto():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 2

  # Retângulo 2
  x3 = 0
  y3 = 1
  x4 = 2
  y4 = 2
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 7: Retângulos de coordenada y1 e y3 diferente sobreposto invertido
def test_retangulos_de_coordenada_y1_y3_diferente_sobreposto_invertido():
  # Retângulo 1
  x1 = 0
  y1 = 1
  x2 = 2
  y2 = 2

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 2
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 8: Retângulos de coordenada y2 e y4 diferente sobreposto
def test_retangulos_de_coordenada_y2_y4_diferente_sobreposto():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 1

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 2
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado

# Caso 9: Retângulos de coordenada y2 e y4 diferente sobreposto invertido
def test_retangulos_de_coordenada_y2_y4_diferente_sobreposto_invertido():
  # Retângulo 1
  x1 = 0
  y1 = 0
  x2 = 2
  y2 = 2

  # Retângulo 2
  x3 = 0
  y3 = 0
  x4 = 2
  y4 = 1
  
  valor_esperado = 1

  retorno = colisao(x1, y1, x2, y2, x3, y3, x4, y4)
  
  assert retorno == valor_esperado