from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from global_variables import get_math_module, length_math_module, print_text_module
# from msgs_treatment import separate_messages
from global_variables import *


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    incoming_msg = request.values.get('Body', '').lower().strip()

    if "menu" in incoming_msg or "oi" in incoming_msg:
        msg.body('Olá! Bem vindo ao EducaZap, um espaço desenvolvido pela Cordel junto com a GRE Metro Sul para te ajudar no estudo através do WhatsApp. Vamos iniciar a aventura? 🤓\n Me fala, qual seu ano no colégio?\n 1️⃣ - 9° ano, Ensino Fundamental.\n 2️⃣ - 3° ano, Ensino Médio.')
    elif "1" == incoming_msg or '9 ano' in incoming_msg or '9' == incoming_msg or '9º ano' in incoming_msg:        
        msg.body('## O código para o 9º ano é 1! ##\n Junte a inicial da matéria desejada + o código do seu ano para proseguir:\n Ok, vamos nessa!\n 💡 Por qual disciplina você deseja iniciar?\n 🧮 M1 - Matematica\n 📖 P2 - Português')
    elif "2" == incoming_msg or '3 ano' in incoming_msg or '3' == incoming_msg or '3º ano' in incoming_msg:  
        msg.body('*## O código para o 3º ano é 2! ##*\n Junte a inicial da matéria desejada + o código do seu ano para proseguir:\n Ok, vamos nessa!\n 💡 Por qual disciplina você deseja iniciar?\n 🧮 M2 - Matematica\n 📖 P2 - Português')
    elif "m1" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 0, 0, 'M12', 0))
    elif "m12" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 1, 0, 'M13', 0))
    elif "m13" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 2, 0, 'M14', 0))
    elif "m14" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 0, 0, 'M15', 0))
    elif "m15" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 1, 0, 'M16', 0))
    elif "m16" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 2, 0, 'M17', 0))
    elif "m17" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 0, 0, 'M18', 0))
    elif "m18" == incoming_msg:
            msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 1, 0, 'M19', 0))
    elif "m19" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 2, 0, 'M111', 0))
    elif "m111" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 3, 0, 'M112', 0))
    elif "m112" == incoming_msg:
        msg.body(print_text_module(4, 'matematica', 'estatística, probabilidade e combinatória', 1, 0, 'M113', 0))
    elif "m113" == incoming_msg:
        msg.body(print_text_module(4, 'matematica', 'estatística, probabilidade e combinatória', 2, 0, 'MENU', 0))
    elif "m2" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 0, 1, 'M22', 0))    
    elif "m22" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 1, 1, 'M23', 0))
    elif "m23" == incoming_msg:
        msg.body(print_text_module(1, 'matematica', 'geometria', 2, 1, 'M24', 0))
    elif "m24" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 0, 1, 'M25', 0))
    elif "m25" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 1, 1, 'M26', 0))
    elif "m26" == incoming_msg:
        msg.body(print_text_module(2, 'matematica', 'grandezas e medidas', 2, 1, 'M27', 0))
    elif "m27" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 0, 1, 'M28', 0))
    elif "m28" == incoming_msg:
            msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 1, 1, 'M29', 0))
    elif "m29" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 2, 1, 'M211', 0))
    elif "m211" == incoming_msg:
        msg.body(print_text_module(3, 'matematica', 'números e operações, álgebra e funções', 3, 1, 'M212', 0))
    elif "m212" == incoming_msg:
        msg.body(print_text_module(4, 'matematica', 'estatística, probabilidade e combinatória', 1, 1, 'M213', 0))
    elif "m213" == incoming_msg:
        msg.body(print_text_module(4, 'matematica', 'estatística, probabilidade e combinatória', 2, 1, 'MENU', 0))


    elif "p1" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 0, 0, 'P12', 0))
    elif "p12" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 1, 0, 'P13', 0))
    elif "p13" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 2, 0, 'P14', 0))
    elif "p14" == incoming_msg:
        msg.body(print_text_module(2, 'portugues', 'relações entre textos', 1, 0, 'P15', 1))
    elif "p15" == incoming_msg:
        msg.body(print_text_module(3, 'portugues', 'coesão e coerência', 0, 0, 'P16', 0))
    elif "p16" == incoming_msg:
        msg.body(print_text_module(3, 'portugues', 'coesão e coerência', 1, 0, 'P17', 0))
    elif "p17" == incoming_msg:
        msg.body(print_text_module(3, 'portugues', 'coesão e coerência', 2, 0, 'P18', 0))
    elif "p18" == incoming_msg:
        msg.body(print_text_module(3, 'portugues', 'coesão e coerência', 3, 0, 'P19', 0))
    elif "p19" == incoming_msg:
        msg.body(print_text_module(4, 'portugues', 'relação entre recursos expressivos e efeitos de sentido', 0, 0, 'MENU', 1))
   
    elif "p2" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 0, 1, 'P22', 0))
    elif "p22" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 1, 1, 'P23', 0))
    elif "p23" == incoming_msg:
        msg.body(print_text_module(1, 'portugues', 'práticas de leitura', 2, 0, 'P24', 0))
    elif "p24" == incoming_msg:
        msg.body(print_text_module(2, 'portugues', 'relações entre textos', 1, 0, 'P25', 1))
    elif "p25" == incoming_msg:
        msg.body(print_text_module(3, 'portugues', 'coesão e coerência', 0, 0, 'P26', 1))
    elif "p26" == incoming_msg:
        msg.body(print_text_module(4, 'portugues', 'relação entre recursos expressivos e efeitos de sentido', 0, 1, 'P27', 0))
    elif "p27" == incoming_msg:
        msg.body(print_text_module(4, 'portugues', 'relação entre recursos expressivos e efeitos de sentido', 1, 1, 'MENU', 0))
   
    elif 'desafio na aula' in incoming_msg:
        text_menu = '''
                        *Escolha o tema*
                        \nA - Geometria\nB - Estatística, probabilidade e combinatória\nC - Grandezas e Medidas\nD - Números, algebra e funções
                        \nE - Coesão e Coerência\nF - Compreensão do texto\nG - Práticas de leitura\nH - Relações entre textos\nI - Variação Linguística          
                    '''
        msg.body(text_menu)
    elif "geometria" in incoming_msg or 'a' == incoming_msg:
        msg.media(class_challenge["geometria"])
        msg.body('Geometria')
    elif "coesao e coerencia" in incoming_msg or "coesão e coerência" in incoming_msg or 'e' == incoming_msg:
        msg.media(class_challenge["coesao e coerencia"])
        msg.body('Coesão e Coerência')
    elif "compreensao do texto" in incoming_msg or "compreesão do texto" in incoming_msg or 'f' == incoming_msg:
        msg.media(class_challenge["compreensao do texto"])
        msg.body('Compreensão do texto')
    elif "probabilidade" in incoming_msg or "combinatoria" in incoming_msg or "estatistica" in incoming_msg or 'b' == incoming_msg:
        msg.media(class_challenge["estatistica, probabilidade e combinatoria"])
        msg.body('Estatística, probabilidade e combinatória')
    elif "grandezas e medidas" in incoming_msg or 'c' == incoming_msg:
        msg.media(class_challenge["grandezas e medidas"])
        msg.body('Grandezas e Medidas')
    elif "algebra e funções" in incoming_msg or "algebra e funcoes" in incoming_msg or 'd' == incoming_msg:
        msg.media(class_challenge["numeros, algebra e funcoes"])
        msg.body('Algebra e Funções')
    elif "relacoes entre textos" in incoming_msg or "relações entre textos" in incoming_msg or 'h' == incoming_msg:
        msg.media(class_challenge["relacoes entre textos"])
        msg.body('Relações entre textos')
    elif "variacao linguistica" in incoming_msg or "variação linguística" in incoming_msg or 'i' == incoming_msg:
        msg.media(class_challenge["variacao linguistica"])
        msg.body('Variação Linguística')


    elif 'dl capítulo 1' in incoming_msg or 'dl capitulo 1' in incoming_msg:
        msg.body("Para saber mais sobre a Jornada Dageons Lunari, digite: Info Jornada Dangeons");
    elif 'info jornada dangeons' in incoming_msg:
        msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL2.png?token=AKZWNKRRE3LJ6CTBG3XYKU3BNXWX4")
        msg.body('Vamos entender as instruções antes de prosseguir?\n Depois de terminar a leitura digite "Quero Sabe Mais"')
    elif 'quero saber mais' in incoming_msg:
        msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL1.png?token=AKZWNKX255GO3OA6ZI3IBD3BNXWNS")
        msg.body('Agora, você está preparado? Calma vamo ver só mais algumas informações! Digita "só mais uma" vai...')
    elif 'so mais uma' in incoming_msg or 'só mais uma' in incoming_msg:
        msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL3.png?token=AKZWNKTJUROMGZBWISYMEDDBNXW6E")
        msg.body("Essa é o último passo!\n*Quando estiver concluído indique a jornada correta*\n + DL M1\n + DL M2\n + DL P1\n + DL P2")
    elif 'dl m1' in incoming_msg:
        msg.body(f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["matematica"][0]}! Que os jogos conhecem 🥅')
    elif 'dl m2' in incoming_msg:
        msg.body(f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["matematica"][1]}! Que os jogos conhecem 🥅')
    elif 'dl p1' in incoming_msg:
        msg.body(f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["portugues"][0]}! Que os jogos conhecem 🥅')
    elif 'dl p2' in incoming_msg:
        msg.body(f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["portugues"][1]}! Que os jogos conhecem 🥅')
    
    else:
        msg.body('\n\nDesculpe, não entendi sua resposta. Por favor, tente novamente ou diga *"Menu"*\n\n')

    return str(resp)
