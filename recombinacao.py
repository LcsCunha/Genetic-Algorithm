import random
from roleta import roleta
import avaliacao as a
from iniciaPopulacao import pegaDados

def cruzamento (pai, mae):
  """
  Função que efetua o cruzamento entre duas sequências de alelos, resultando em um filho entre eles.
  """
  seed = random.randint(0, 29)
  alelos = pai[:seed] + mae[seed:]

  filho = dict([
    ('alelos', alelos), 
    ('peso', a.calculaPeso(alelos, pegaDados())), 
    ('valor', a.calculaValor(alelos, pegaDados())),
    ('utilidade', a.fitness(alelos, pegaDados()))
  ])

  return filho
  
def recombinacao(P, tamSelecao):
  """
  Função que implementa a recombinação de alelos.
  """

  #Selecionando os pais da próxima geração por meio da técnica da roleta
  pais = roleta(P, tamSelecao)
  maes = roleta(P, tamSelecao)
  #
  
  selecao = []
  
  #Escolhendo de forma randômica os indivíduos a serem cruzados
  while (len(selecao) < tamSelecao): 
    pai = random.randint(0, len(pais) - 1)
    mae = random.randint(0, len(maes) - 1)
    alelosPai = pais[pai]["alelos"]
    alelosMae = maes[mae]["alelos"]
    selecao.append(cruzamento(alelosPai, alelosMae))
    a.avaliacao(selecao)
    #Caso o cruzamento não obedeça ao peso limite ou valor limite, o mesmo é removido da seleção e a recombinação continua
  #
  
  return selecao