def calculaPeso (alelos, dados):
  """
  Função que conta o peso total em dado array de alelos.
  """
  pesoFinal = 0

  for i in range (len(alelos)):
    if alelos[i] == 1:
      pesoFinal += dados["itens"][i]["peso"]

  return pesoFinal

def calculaValor (alelos, dados):
  """
  Função que conta o valor total em dado array de alelos.
  """
  valorFinal = 0

  for i in range (len(alelos)):
    if alelos[i] == 1:
      valorFinal += dados["itens"][i]["valor"]

  return valorFinal

def fitness (alelos, dados):
  """
  Função que conta a utilidade total em dado array de alelos.
  """
  utilidade = 0

  for i in range (len(alelos)):
    if alelos[i] == 1:
      utilidade += dados["itens"][i]["utilidade"]

  return utilidade

def avaliacao (P):
  """
  Função de avaliação: caso a sequencia de alelos possua um peso ou valor maiores que o limite, o respectivo indivíduo é deletado da população.
  """
  i = 0
  cont = 0

  while i < len(P):
    if P[i]["peso"] > 30:
      del(P[i])
      i -= 1
      cont += 1
    elif P[i]["valor"] > 100:
      del(P[i])
      i -= 1
      cont += 1
    
    if P == None:
      break
    
    i += 1
  
  return