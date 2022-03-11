import random
from roleta import roleta

def selecaoDosPais(P):
  """
  Função que seleciona os pais da próxima geração á partir da população atual por meio da técnica da roleta.
  """
  pais = roleta(P, len(P)) 
  
  return pais