import avaliacao as a
from iniciaPopulacao import pegaDados
import random

def muta(P, index):
  """
  Função que efetua a mutação de dada sequência de alelos. Por padrão próprio do nosso código, no máximo 3 alelos de cada sequência podem ser modificados. Caso a mutação afete as restrições de forma a serem desobedecidas, um alelo 1 é transformado em 0 e a mutação termina.
  """
  alelos = P[index]["alelos"]
  mutados = 0

  for i in range(30):
    seed = random.randint(0, 29)

    if alelos[seed] == 0:
      alelos[seed] = 1
      mutados += 1
      peso = a.calculaPeso(alelos, pegaDados())
      valor = a.calculaValor(alelos, pegaDados())
      if (peso > 30) or (valor > 100):
        alelos[seed] = 0
        break

    if mutados == 3:
      break

  #Transformando definitivamente o indivíduo na população
  P[index] = dict([
          ('alelos', alelos), 
          ('peso', a.calculaPeso(alelos, pegaDados())), 
          ('valor', a.calculaValor(alelos, pegaDados())),
          ('utilidade', a.fitness(alelos, pegaDados()))
  ])
  #
  
  return P

def mutacao(P, tamSelecao):
  """
  Função que implementa a mutação de alelos, neste caso apenas os 'tamSelecao'% dos piores da população serão mutados.
  """
  #Ordenando a população do indivíduo menos útil ao mais útil.
  P = sorted(P, key=lambda i:i['utilidade']) 

  mutantes = P[:tamSelecao] #Mutando os piores individuos

  for i in range (0, len(mutantes)):
    mutantes = muta(mutantes, i)
  
  return mutantes
  