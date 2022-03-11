import csv 
import random
import avaliacao as a

def readCSV (arquivoTabela):
  """
  Função criada com o intuito de ler um arquivo csv e
  retornar seus elementos (dados) como forma de lista de strings
  """
  with open(arquivoTabela, newline='') as f:
      reader = csv.reader(f)
      dados = list(reader)

  return dados

def pegaDados ():
  """
  Função utilizada para pegar os dados da tabela referente aos itens da feira, organizamos em um dicionário em que cada index do array "itens" é um dicionário referente a cada item da feira.
  """
  dados = readCSV ('tabela_feira.csv')
  feira = {
    "itens": [],
    "pesoTotal": 0,
    "valorTotal": 0,
    "utilidadeTotal": 0
  }

  for i in range(len(dados)):
    if i != 0:
      numero = int(dados[i][0])
      peso = int(dados[i][1])
      valor = float(dados[i][2])
      utilidade = int(dados[i][3])

      feira["itens"].append(
        dict([
          ('numero', numero), 
          ('peso', peso), 
          ('valor', valor),
          ('utilidade', utilidade)
        ])
      )
      feira["pesoTotal"] += peso
      feira["valorTotal"] += valor
      feira["utilidadeTotal"] += utilidade
      
  return feira

def geraAlelos (dados):
  """
  Função que gera os alelos de forma aleatória, cada array de alelos representa os itens da feira que estão sendo levados.
  """
  alelos = []
  for i in range(30):
    seed = random.randint(0, 100)
    if seed < 30:
      alelos.append(1)
    else:
      alelos.append(0)

  return alelos

def iniciaPopulacao():
  """
  Função que inicia a população, cada população representa uma série de diferentes combinações de itens que são representados pelos seus respectivos alelos.
  """
  populacao = []
  feira = pegaDados()
  
  for i in range(2000):
    alelos = geraAlelos(feira)
    populacao.append(
      dict([
          ('alelos', alelos), 
          ('peso', a.calculaPeso(alelos, pegaDados())), 
          ('valor', a.calculaValor(alelos, pegaDados())),
          ('utilidade', a.fitness(alelos, pegaDados()))
      ])
    )
  
  return populacao