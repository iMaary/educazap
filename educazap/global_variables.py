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

# module_item is the status of study module
global module_item
module_item = 0

def plus_item(value):
    global module_item
    module_item += value

def get_item(): 
    return module_item

def set_item(value): 
    global module_item
    module_item = value

# subject is a status to choose the material
global subject
subject = None

def get_subject(): 
    return subject

def set_subject(value): 
    global subject
    subject = value

# subject is a status to choose the material
global school_level
school_level = None

def get_level(): 
    return school_level

def set_level(value): 
    global school_level
    school_level = value

# title material modules
global math_modules
math_modules = {
'geometria':
[
['Identificar propriedades comuns e diferenças entre figuras bidimensionais e tridimensionais, relacionando-as com as suas planificações.', 
'Resolver problema que envolva razões trigonométricas no triângulo retângulo (seno, cosseno, tangente).'],
['Identificar propriedades de triângulos pela comparação de medidas de lados e ângulos.',
'Identificar a localização de pontos no plano cartesiano.'],
['Resolver problema utilizando relações métricas no triângulo retângulo. + exercício',
'Reconhecer, dentre as equações do 2º grau com duas incógnitas, as que representam circunferências.']
],
'grandezas e medidas':
[
['Resolver problema envolvendo perímetro de figuras planas',
'Resolver problema envolvendo perímetro de figuras planas'],
['Resolver problema envolvendo área de figuras planas',
'Resolver problema envolvendo área de figuras planas'],
['Resolver problemas utilizando relações entre diferentes unidades de medida.',
'Resolver problema envolvendo a área total e/ou volume de um sólido (prisma, pirâmide, cilindro, cone, esfera)']   
],
'números e operações, álgebra e funções':
[
['Identificar a localização de números inteiros na reta numérica.',
'Identificar a localização de números inteiros na reta numérica.'],
['Efetuar cálculos com números inteiros, envolvendo as operações (adição, subtração, multiplicação, divisão, potenciação).',
'Reconhecer o gráfico de uma função polinomial de 1º grau por meio de seus coeficientes.'],
['Resolver problemas utilizando frações equivalentes.',
'Identificar gráficos de funções trigonométricas (seno, cosseno, tangente) reconhecendo suas propriedades.'],
['Identificar uma equação ou inequação do 1º grau que expressa um problema.',
'Determinar a solução de um sistema linear problema.'] 
],
'estatística, probabilidade e combinatória':
[
['Resolver problemas envolvendo probabilidade de um evento.',
'Resolver problemas envolvendo probabilidade de um evento.'],
['Resolver problemas envolvendo informações apresentadas em tabelas e/ou gráficos.',
'Resolver problemas envolvendo informações apresentadas em tabelas e/ou gráficos.']
]
}

def get_math_module(value : str, i, j):
    return math_modules[value][i][j]

def length_math_module(value : str): 
    return len(math_modules[value])

global portuguese_modules
portuguese_modules = {
'práticas de leitura':
[ 
['Identificar o tema central de um texto.',
'Localizar informação explícita em um texto.'],
['Localizar informação explícita em um texto.',
'Inferir o sentido de uma palavra ou expressão.'],
['Distinguir fato de opinião relativa a fato.',
'(AULA 3)']
],
'Implicações do suporte, do gênero e/ou do enunciador na compreensão do texto':
[
['(AULA 1)',
'(AULA 1)'],
['(AULA 2)',
'(AULA 2)'],
['(AULA 3)',
'(AULA 3)']
],
'relações entre textos':
[
['Reconhecer semelhanças e/ou diferenças de ideias e opiniões na comparação entre textos que tratem da mesma temática.',
'(AULA 1)'],
['(AULA 2)',
'(AULA 2)'],
['(AULA 3)',
'(AULA 3)']
],
'coesão e coerência':
[
['Reconhecer as relações entre partes de um texto, identificando os recursos coesivos que contribuem para sua continuidade.',
'Diferenciar as partes principais das secundárias em um texto.'],
['Diferenciar as partes principais das secundárias em um texto.',
'(AULA 2)'],
['Identificar a tese de um texto.',
'(AULA 3)'],
['Estabelecer relação de causa e consequência entre partes do texto.',
'(AULA 4)']
],
'relação entre recursos expressivos e efeitos de sentido':
[
['Identificar efeitos de sentido decorrente do uso de pontuação e outras notações',
'Identificar efeitos de sentido decorrente do uso de pontuação e outras notações.'],
['(AULA 2)',
'Reconhecer o efeito de sentido decorrente do emprego de recursos estilísticos e morfossintáticos.']
]
} 

def get_portuguese_module(value : str, i, j):
    return portuguese_modules[value][i][j]

def length_portuguese_module(value : str): 
    return len(portuguese_modules[value])
