def sobrevivem (P, taxaSobrevivencia):
  """
  Função que implementa a sobrevivência dos melhores da população, os mesmos irão ser inseridos na próxima geração. Apenas 'taxaSobrevivencia'% dos melhores sobreviverão.
  """
  #Ordenando a populacao de indivíduos do mais útil ao menos útil
  P = sorted(P, key=lambda i:i['utilidade'], reverse=True)

  P = P[:taxaSobrevivencia]
  return P