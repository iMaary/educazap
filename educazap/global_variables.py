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
['Identificar propriedades comuns e diferenças entre figuras bidimensionais e tridimensionais, relacionando-as com as suas planificações. $ https://www.youtube.com/watch?v=M5wjj50Qpug', 
'Resolver problema que envolva razões trigonométricas no triângulo retângulo (seno, cosseno, tangente). $ https://www.youtube.com/watch?v=4sTUs4ll3dI'],
['Identificar propriedades de triângulos pela comparação de medidas de lados e ângulos. $ https://www.youtube.com/watch?v=QXv5gS3kos8',
'Identificar a localização de pontos no plano cartesiano. $ https://www.youtube.com/watch?v=GEacaND5sU4'],
['Resolver problema utilizando relações métricas no triângulo retângulo + exercício. $ https://www.youtube.com/watch?v=Sk4KxSLUrZc',
'Reconhecer, dentre as equações do 2º grau com duas incógnitas, as que representam circunferências. $ https://www.youtube.com/watch?v=tu81HCPl4mU']
],
'grandezas e medidas':
[
['Resolver problema envolvendo perímetro de figuras planas. $ https://www.youtube.com/watch?v=a6AJyCgt-uM',
'Resolver problema envolvendo perímetro de figuras planas $ https://www.youtube.com/watch?v=a6AJyCgt-uM'],
['Resolver problema envolvendo área de figuras planas $ https://www.youtube.com/watch?v=th5k6bzSDTA',
'Resolver problema envolvendo área de figuras planas $ https://www.youtube.com/watch?v=th5k6bzSDTA'],
['Resolver problemas utilizando relações entre diferentes unidades de medida. $ https://www.youtube.com/watch?v=q3UhYH8kiSE',
'Resolver problema envolvendo a área total e/ou volume de um sólido (prisma, pirâmide, cilindro, cone, esfera) $ https://www.youtube.com/watch?v=3iWl-Liuw5s']   
],
'números e operações, álgebra e funções':
[
['Identificar a localização de números inteiros na reta numérica. $ https://www.youtube.com/watch?v=om-YnS1OUeE',
'Identificar a localização de números inteiros na reta numérica. $ https://www.youtube.com/watch?v=om-YnS1OUeE'],
['Efetuar cálculos com números inteiros, envolvendo as operações (adição, subtração, multiplicação, divisão, potenciação). $ https://www.youtube.com/watch?v=ziKpOLmLj4A',
'Reconhecer o gráfico de uma função polinomial de 1º grau por meio de seus coeficientes. $ https://www.youtube.com/watch?v=R8UZRBFWJXY'],
['Resolver problemas utilizando frações equivalentes. $ https://www.youtube.com/watch?v=JlNHHvmNCgg',
'Identificar gráficos de funções trigonométricas (seno, cosseno, tangente) reconhecendo suas propriedades. $ https://www.youtube.com/watch?v=4plf0z3skCQ'],
['Identificar uma equação ou inequação do 1º grau que expressa um problema. $ https://www.youtube.com/watch?v=LsX-0I5w9UE',
'Determinar a solução de um sistema linear problema. $ https://www.youtube.com/watch?v=9ATZyBcgq4g'] 
],
'estatística, probabilidade e combinatória':
[
['Resolver problemas envolvendo probabilidade de um evento. $ https://www.youtube.com/watch?v=AZH67sWDW5w',
'Resolver problemas envolvendo probabilidade de um evento. $ https://www.youtube.com/watch?v=AZH67sWDW5w'],
['Resolver problemas envolvendo informações apresentadas em tabelas e/ou gráficos. $ https://www.youtube.com/watch?v=XzZGAwfKs_k',
'Resolver problemas envolvendo informações apresentadas em tabelas e/ou gráficos. $ https://www.youtube.com/watch?v=XzZGAwfKs_k']
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
['Identificar o tema central de um texto. $ https://www.youtube.com/watch?v=AiOpVoblBYQ',
'Localizar informação explícita em um texto. $ https://www.youtube.com/watch?v=PUzoSsOYVoM'],
['Localizar informação explícita em um texto. $ https://www.youtube.com/watch?v=PUzoSsOYVoM',
'Inferir o sentido de uma palavra ou expressão. $ https://www.youtube.com/watch?v=m-Mr8sM5RwU'],
['Distinguir fato de opinião relativa a fato. $ https://www.youtube.com/watch?v=fdHA2rhDasU',
'(AULA 3) $ https://AULA3']
],
'Implicações do suporte, do gênero e/ou do enunciador na compreensão do texto':
[
['(AULA 1) $ https://AULA1',
'(AULA 1) $ https://AULA1'],
['(AULA 2) $ https://AULA2',
'(AULA 2) $ https://AULA2'],
['(AULA 3) $ https://AULA3',
'(AULA 3) $ https://AULA3']
],
'relações entre textos':
[
['Reconhecer semelhanças e/ou diferenças de ideias e opiniões na comparação entre textos que tratem da mesma temática. $ https://www.youtube.com/watch?v=RxMfvyONZfg',
'(AULA 1) $ https://AULA3'],
['(AULA 2) $ https://AULA2',
'(AULA 2) $ https://AULA2'],
['(AULA 3) $ https://AULA3',
'(AULA 3) $ https://AULA3']
],
'coesão e coerência':
[
['Reconhecer as relações entre partes de um texto, identificando os recursos coesivos que contribuem para sua continuidade. $ https://www.youtube.com/watch?v=O6L1a0LRVm0',
'Diferenciar as partes principais das secundárias em um texto. $ https://www.youtube.com/watch?v=rUFthCR7NY4'],
['Diferenciar as partes principais das secundárias em um texto. $ https://www.youtube.com/watch?v=rUFthCR7NY4',
'(AULA 2) $ https://AULA2'],
['Identificar a tese de um texto. $ https://www.youtube.com/watch?v=QgzgrAwmJZI',
'(AULA 3) $ https://AULA3'],
['Estabelecer relação de causa e consequência entre partes do texto $ https://www.youtube.com/watch?v=u3pbYzIJvCY.',
'(AULA 4) $ https://AULA4']
],
'relação entre recursos expressivos e efeitos de sentido':
[
['Identificar efeitos de sentido decorrente do uso de pontuação e outras notações. $ https://www.youtube.com/watch?v=7hzDytthua4',
'Identificar efeitos de sentido decorrente do uso de pontuação e outras notações. $ https://www.youtube.com/watch?v=7hzDytthua4'],
['(AULA 2) $ https://AULA2',
'Reconhecer o efeito de sentido decorrente do emprego de recursos estilísticos e morfossintáticos. $ https://www.youtube.com/watch?v=gafUCYsVs1w']
]
} 

def get_portuguese_module(value : str, i, j):
    return portuguese_modules[value][i][j]

def length_portuguese_module(value : str): 
    return len(portuguese_modules[value])


class_challenge = {
"coesao e coerencia":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Coes%C3%A3o%20e%20Coer%C3%AAncia.png?token=AKZWNKQPNUDJSVI6Z5GZEPDBNGQZ6",
"compreensao do texto":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Compreens%C3%A3o%20do%20texto.png?token=AKZWNKRBWM4GL6J4K4CUAJDBNGQ4K",
"estatistica, probabilidade e combinatoria":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Estat%C3%ADstica%2C%20probabilidade%20e%20combinat%C3%B3ria.png?token=AKZWNKTCL3ITJXHX4AGVMATBNGRAU",
"grandezas e medidas":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Grandezas%20e%20Medidas%20EF.png?token=AKZWNKSQ2GRBHJAD6ZG4QTLBNGRFI",
"numeros, algebra e funcoes":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/N%C3%BAmeros%2C%20%C3%A1lgebra%20e%20fun%C3%A7%C3%B5es.png?token=AKZWNKTHIXX6DLMM7UBJJXLBNGRHU",
"praticas de leitura":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Pr%C3%A1ticas%20de%20leitura.png?token=AKZWNKUIZVLKMBHBEMS6TETBNGRNU",
"relacoes entre textos":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Rela%C3%B5es%20emtre%20textos%20do%20texto.png?token=AKZWNKUA4A5ST6XBMGDMP5TBNGRRE",
"variacao linguistica":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/Varia%C3%A7%C3%A3o%20Lingu%C3%ADstica.png?token=AKZWNKX2KFOXYIY2C65UVS3BNGRYE",
"geometria":
"https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/_Geometria%20EF.png?token=AKZWNKRP5GXCMPI77X3IRA3BNGR26"
}

global menu_class_challenge
menu_class_challenge = False

def invert_menu():
    global menu_class_challenge
    menu_class_challenge = not menu_class_challenge

def consult_menu():
    return menu_class_challenge

dangeons_lunari = {
"matematica": 
[
"https://forms.gle/dzgULZnSZDJ67QZJ6",
"https://forms.gle/ZKzzDEdW5hLqHaUf8"    
],
"portugues":
[
"https://forms.gle/Lhk4xk5GASQUJw7NA",
"https://forms.gle/MwMGKUYY3fpPhCCB7"
]
}

global menu_class_lunari
menu_class_lunari = False

def invert_lunari_verify():
    global menu_class_lunari
    menu_class_lunari = not menu_class_lunari

def consult_lunari_verify():
    return menu_class_lunari

global count_lunari_images
count_lunari_images = 0

def plus_lunari_count_img(value):
    global count_lunari_images
    count_lunari_images += value

def consult_lunari_count():
    return count_lunari_images


global current_subject_lunari
current_subject_lunari = ''

def define_lunari_subject(value):
    global current_subject_lunari
    current_subject_lunari = value

def consult_lunari_subject():
    return current_subject_lunari
