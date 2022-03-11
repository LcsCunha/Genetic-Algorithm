from iniciaPopulacao import iniciaPopulacao
from avaliacao import avaliacao
from selecaoDosPais import selecaoDosPais
from recombinacao import recombinacao
from mutacao import mutacao
from sobrevivem import sobrevivem

def ag (maxGeracoes):
  """
  Função que implementa o algoritmo genético.
  """
  geracao = 0
  P = iniciaPopulacao()
  avaliacao(P)

  while (geracao != maxGeracoes):
    geracao += 1
    print("Geracao", geracao,"\n")

    P = selecaoDosPais(P)
    
    #92% da proxima geracao formada por recombinacao
    proxG = recombinacao(P, int(len(P)*0.93)) 
    #

    #1% da proxima geracao formada por mutação
    proxG += mutacao(P, int(len(P)*0.01))
    #

    #6% da proxima geracao formada por sobrevivência
    proxG += sobrevivem(P, int(len(P)*0.06))
    #

    P = proxG
  
  #Ordenando a populacao de indivíduos do mais útil ao menos útil
  P = sorted(P, key=lambda i:i['utilidade'], reverse=True)
  #
  
  print("Melhor resultado encontrado em", maxGeracoes, "geracoes:\n\n", P[0])
  
  return

  