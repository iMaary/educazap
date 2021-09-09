# count_msg is the message state to be sent
global count_msg
count_msg = 0

def plus_count(value):
    global count_msg
    count_msg += value

def get_count(): 
    return count_msg

def set_count(value): 
    global count_msg
    count_msg = value

# module_fase is the status of study subject
global module_fase
module_fase = 0

def plus_fase(value):
    global module_fase
    module_fase += value

def get_fase(): 
    return module_fase

def set_fase(value): 
    global module_fase
    module_fase = value

# title material modules
global modules
modules = {
'geometria': 
['Identificar a localização/movimentação de objeto em mapas, croquis e outras representações gráficas.', 
'Identificar propriedades comuns e diferenças entre figuras bidimensionais e tridimensionais, relacionando-as com as suas planificações.',
'Identificar propriedades de triângulos pela comparação de medidas de lados e ângulos.',
'Resolver problema utilizando relações métricas no triângulo retângulo. + exercício'],
'grandezas e medidas': 
['Resolver problema envolvendo perímetro de figuras planas.',
'Resolver problema envolvendo área de figuras planas.',
'Resolver problema envolvendo a área total e/ou volume de um sólido (prisma, pirâmide, cilindro, cone, esfera)'],
'números e operações, álgebra e funções':
['Identificar a localização de números inteiros na reta numérica.',
'Efetuar cálculos com números inteiros, envolvendo as operações (adição, subtração, multiplicação, divisão, potenciação).',
'Resolver problemas utilizando frações equivalentes.',
'Identificar uma equação ou inequação do 1º grau que expressa um problema.'],
'estatística, probabilidade e combinatória': 
['Resolver problema envolvendo probabilidade de um evento.',
'Resolver problema envolvendo informações apresentadas em tabelas e/ou gráficos.']
}

def get_module(value : str, index):
    return modules[value][index]

def length_module(value : str): 
    return len(modules[value])

