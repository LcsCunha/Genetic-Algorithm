import random

def roleta (P, tamSelecao):
  """
  Função que implementa a técnica da roleta.
  """
  #Ordenando a populacao de indivíduos do mais útil ao menos útil
  P = sorted(P, key=lambda i:i['utilidade'], reverse=True)
  #

  buffer = P

  #Dividindo o vetor população atual ordenado em 5
  tam1 = int(len(P)*0.35)
  tam2 = int(len(P)*0.25)
  tam3 = int(len(P)*0.20)
  tam4 = int(len(P)*0.15)
  tam5 = int(len(P)*0.05)

  pedaco1 = buffer[:tam1]
  buffer = buffer[tam1:]
  
  pedaco2 = buffer[:tam2]
  buffer = buffer[tam2:]
  
  pedaco3 = buffer[:tam3]
  buffer = buffer[tam3:]
  
  pedaco4 = buffer[:tam4]
  buffer = buffer[tam4:]
  
  pedaco5 = buffer[:tam5]
  buffer = buffer[tam5:]
  #

  selecao = []

  #Efetuando a seleção de indivíduos de forma randômica
  for i in range(tamSelecao):
    seed = random.randint(0, 100)

    #Chance de seleção
    if seed < 35: #35% de chance para os melhores
      valor = random.randint(0, tam1 - 1)
      selecao.append(pedaco1[valor])
    elif seed < 60: #25% de chance para os segundos
      valor = random.randint(0, tam2 - 1)
      selecao.append(pedaco2[valor])
    elif seed < 80: #20% de chance para os terceiros
      valor = random.randint(0, tam3 - 1)
      selecao.append(pedaco3[valor])
    elif seed < 95: #15% de chance para os quartos
      valor = random.randint(0, tam4 - 1)
      selecao.append(pedaco4[valor])
    else: #5% de chance para os piores
      valor = random.randint(0, tam5 - 1)
      selecao.append(pedaco5[valor])
    #
  #
    
  return selecao