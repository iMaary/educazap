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

global portuguese_modules
portuguese_modules = {
'práticas de leitura':
[ 
['Identificar o tema central de um texto. $ https://www.youtube.com/watch?v=AiOpVoblBYQ',
'Localizar informação explícita em um texto. $ https://www.youtube.com/watch?v=PUzoSsOYVoM'],
['Localizar informação explícita em um texto. $ https://www.youtube.com/watch?v=PUzoSsOYVoM',
'Inferir o sentido de uma palavra ou expressão. $ https://www.youtube.com/watch?v=m-Mr8sM5RwU'],
['Distinguir fato de opinião relativa a fato. $ https://www.youtube.com/watch?v=fdHA2rhDasU',
'<Descritor Indisponível> $ https://somoscordel.com.br']
],
'Implicações do suporte, do gênero e/ou do enunciador na compreensão do texto':
[
['<Descritor Indisponível> $ https://somoscordel.com.br',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['<Descritor Indisponível> $ https://somoscordel.com.br',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['<Descritor Indisponível> $ https://somoscordel.com.br',
'<Descritor Indisponível> $ https://somoscordel.com.br']
],
'relações entre textos':
[
['Reconhecer semelhanças e/ou diferenças de ideias e opiniões na comparação entre textos que tratem da mesma temática. $ https://www.youtube.com/watch?v=RxMfvyONZfg',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['<Descritor Indisponível> $ https://somoscordel.com.br',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['<Descritor Indisponível> $ https://somoscordel.com.br',
'<Descritor Indisponível> $ https://somoscordel.com.br']
],
'coesão e coerência':
[
['Reconhecer as relações entre partes de um texto, identificando os recursos coesivos que contribuem para sua continuidade. $ https://www.youtube.com/watch?v=O6L1a0LRVm0',
'Diferenciar as partes principais das secundárias em um texto. $ https://www.youtube.com/watch?v=rUFthCR7NY4'],
['Diferenciar as partes principais das secundárias em um texto. $ https://www.youtube.com/watch?v=rUFthCR7NY4',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['Identificar a tese de um texto. $ https://www.youtube.com/watch?v=QgzgrAwmJZI',
'<Descritor Indisponível> $ https://somoscordel.com.br'],
['Estabelecer relação de causa e consequência entre partes do texto $ https://www.youtube.com/watch?v=u3pbYzIJvCY.',
'<Descritor Indisponível> $ https://somoscordel.com.br']
],
'relação entre recursos expressivos e efeitos de sentido':
[
['Identificar efeitos de sentido decorrente do uso de pontuação e outras notações. $ https://www.youtube.com/watch?v=7hzDytthua4',
'Identificar efeitos de sentido decorrente do uso de pontuação e outras notações. $ https://www.youtube.com/watch?v=7hzDytthua4'],
['<Descritor Indisponível> $ https://somoscordel.com.br',
'Reconhecer o efeito de sentido decorrente do emprego de recursos estilísticos e morfossintáticos. $ https://www.youtube.com/watch?v=gafUCYsVs1w']
]
} 

def get_math_module(value : str, i, j):
    return math_modules[value][i][j]

def length_math_module(value : str): 
    return len(math_modules[value])

def get_portuguese_module(value : str, i, j):
    return portuguese_modules[value][i][j]

def length_portuguese_module(value : str): 
    return len(portuguese_modules[value])


def print_text_module(module_num, materia, key : str, i, j, new_code, verify):

    if 'portugues' in materia:    
        texts = get_portuguese_module(key, i, j).split('$')
        length = length_portuguese_module(key)
    else:
        texts = get_math_module(key, i, j).split('$')
        length = length_math_module(key)
    
    text = f'''Módulo {module_num}: {key.upper()} - AULA {i+1}/{length if (verify == 0) else verify} 📐🚀                                                                    
                            \nÓtimo, nessa aula você vai descobrir como _*"{texts[0]}"*_, assista sua aula em: {texts[1]}
                            \nQuando concluir a aula, mande um *{new_code}*                                                               
                            \nNão esqueça de:\n- Fazer exercícios.\n- Estudar os conteúdos.'''
    return text


class_challenge = {
"coesao e coerencia":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Coes%C3%A3o%20e%20Coer%C3%AAncia.png?token=AKZWNKR44YB2CWN46PSG7A3BN6BKI",
"compreensao do texto":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Compreens%C3%A3o%20do%20texto.png?token=AKZWNKXFLQ3BNURS5AWJZA3BN6BLS",
"estatistica, probabilidade e combinatoria":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Estat%C3%ADstica%2C%20probabilidade%20e%20combinat%C3%B3ria.png?token=AKZWNKUSNAOPVVCVUAGFN6DBN6BMO",
"grandezas e medidas":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Grandezas%20e%20Medidas%20EF.png?token=AKZWNKURFK6FTOOPDTWOUOLBN6BOC",
"numeros, algebra e funcoes":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/N%C3%BAmeros%2C%20%C3%A1lgebra%20e%20fun%C3%A7%C3%B5es.png?token=AKZWNKWUFOORI67E27RMXV3BN6BUO",
"praticas de leitura":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Pr%C3%A1ticas%20de%20leitura.png?token=AKZWNKUK7URDZPK5KFUT6ELBN6BVK",
"relacoes entre textos":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Rela%C3%B5es%20emtre%20textos%20do%20texto.png?token=AKZWNKVZI7LYJ5ZZN24PL2DBN6BXM",
"variacao linguistica":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/Varia%C3%A7%C3%A3o%20Lingu%C3%ADstica.png?token=AKZWNKSIEEDETFKCIQU477TBN6BX6",
"geometria":
"https://raw.githubusercontent.com/iMaary/educazap/main/educazap/static/DESAFIO_NA_AULA/_Geometria%20EF.png?token=AKZWNKU5P6JG3WZ7GMSC2I3BN6BYW"
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
