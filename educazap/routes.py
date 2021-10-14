from os import link
from app import app
from flask import request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from msgs_treatment import separate_messages
from global_variables import *


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    flow = separate_messages('messages.csv')
    incoming_msg = request.values.get('Body', '').lower()
    module_name = ''
    text = ''
    temp_count = 0
    current_module = None
    size_module = None

    if "dl capítulo 1" in incoming_msg or "dl capitulo 1" in incoming_msg or consult_lunari_verify():
        # reset modules data
        set_item(0)
        set_fase(0)
        set_count(0)

        if consult_lunari_count() == 0:
            invert_lunari_verify()
        plus_lunari_count_img(1)
        if consult_lunari_count() == 1:
            msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL2.png?token=AKZWNKRRE3LJ6CTBG3XYKU3BNXWX4")
            msg.body("Vamos entender as instruções antes de prosseguir?")
        elif consult_lunari_count() == 2:
            msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL1.png?token=AKZWNKX255GO3OA6ZI3IBD3BNXWNS")
            msg.body("Agora, você está preparado?")
        elif consult_lunari_count() == 3:
            msg.media("https://raw.githubusercontent.com/iMaary/educazap/chatbot-twilio/educazap/static/DANGEONS_LUNARI/DL3.png?token=AKZWNKTJUROMGZBWISYMEDDBNXW6E")
            msg.body(
                "Antes veja mais algumas informações interessantes!\n*Dê um _OK_ quando estiver concluído :)*")
        elif consult_lunari_count() == 4:
            msg.body("Chegou a hora de informar a matéria que você deseja!")
        elif consult_lunari_count() == 5:
            if not("matematica" in incoming_msg or "portugues" in incoming_msg or "matemática" in incoming_msg or "português" in incoming_msg):
                plus_lunari_count_img(-1)
                msg.body(
                    "Desculpe, não entendi!\n\n*OBS.:* essa resposta pode não estar de acordo com o solicitado...")
                return str(resp)
            define_lunari_subject(incoming_msg)
            msg.body("Em que ano você está mesmo?")
        else:
            if "9º ano" in incoming_msg or "9" in incoming_msg:
                level = 0
            elif "3º ano" in incoming_msg or "3" in incoming_msg:
                level = 1
            else:
                plus_lunari_count_img(-1)
                msg.body(
                    "Desculpe, não entendi!\n\n*OBS.:* essa resposta pode não estar de acordo com o solicitado...")
                return str(resp)

            if "matemática" in consult_lunari_subject() or "matemática" in consult_lunari_subject():
                msg.body(
                    f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["matematica"][level]}! Que os jogos conhecem 🥅')
            elif "portugues" in consult_lunari_subject() or "português" in consult_lunari_subject():
                msg.body(
                    f'A aventura vai começar! Preparado(a)? 🥌 🚀 🎮\nEntre no link: {dangeons_lunari["portugues"][level]}! Que os jogos conhecem 🥅')

            invert_lunari_verify()
            plus_lunari_count_img(-6)
            define_lunari_subject('')

    elif "desafio na aula" in incoming_msg or consult_menu():
        # reset modules data
        set_item(0)
        set_fase(0)
        set_count(0)

        # implements
        invert_menu()
        if consult_menu():
            text_menu = '''
                            *Escolha o tema*
                            \n1 - Geometria\n2 - Estatística, probabilidade e combinatória\n3 - Grandezas e Medidas\n4 - Números, algebra e funções
                            \n5 - Coesão e Coerência\n6 - Compreensão do texto\n7 - Práticas de leitura\n8 - Relações entre textos\n9 - Variação Linguística          
                        '''
            msg.body(text_menu)
        else:
            current_challenge_name = ''
            if "geometria" in incoming_msg:
                msg.media(class_challenge["geometria"])
                current_challenge_name = 'Geometria'
            elif "coesao e coerencia" in incoming_msg or "coesão e coerência" in incoming_msg:
                msg.media(class_challenge["coesao e coerencia"])
                current_challenge_name = 'Coesão e Coerência'
            elif "compreensao do texto" in incoming_msg or "compreesão do texto" in incoming_msg:
                msg.media(class_challenge["compreensao do texto"])
                current_challenge_name = 'Compreensão do texto'
            elif "probabilidade" in incoming_msg or "combinatoria" in incoming_msg or "estatistica" in incoming_msg:
                msg.media(
                    class_challenge["estatistica, probabilidade e combinatoria"])
                current_challenge_name = 'Estatística, probabilidade e combinatória'
            elif "grandezas e medidas" in incoming_msg:
                msg.media(class_challenge["grandezas e medidas"])
                current_challenge_name = 'Grandezas e Medidas'
            elif "algebra e funções" in incoming_msg or "algebra e funcoes" in incoming_msg:
                msg.media(class_challenge["numeros, algebra e funcoes"])
                current_challenge_name = 'Algebra e Funções'
            elif "relacoes entre textos" in incoming_msg or "relações entre textos" in incoming_msg:
                msg.media(class_challenge["relacoes entre textos"])
                current_challenge_name = 'Relações entre textos'
            elif "variacao linguistica" in incoming_msg or "variação linguística" in incoming_msg:
                msg.media(class_challenge["variacao linguistica"])
                current_challenge_name = 'Variação Linguística'
            else:
                msg.body("algo de errado não está certo!")
            if current_challenge_name:
                msg.body(f'Digite *"Concluído"* após finalizar a atividade!')

    elif "*" in flow[get_count()][0]:
        if get_subject() == 'matematica':
            current_module = math_modules
            for i in current_module:
                module_name = i
                temp_count += 1
                if temp_count > get_item():
                    break
            size_module = length_math_module(module_name)
            text = get_math_module(module_name, get_fase(), get_level())

        elif get_subject() == 'portugues':
            current_module = portuguese_modules
            for i in current_module:
                module_name = i
                temp_count += 1
                if temp_count > get_item():
                    break
            size_module = length_portuguese_module(module_name)
            text = get_portuguese_module(module_name, get_fase(), get_level())

        complete_text = text.split('$')
        print(complete_text)
        class_link = complete_text[1]
        text = complete_text[0]
        text = text.replace('.', '')
        # print(f'class_link: {class_link} | text: {text}')
        text = f'''Módulo {get_item()+1}: {module_name.upper()} - AULA {get_fase()+1}/{size_module} 📐🚀                                                                    
                        \nÓtimo, nessa aula você vai descobrir como _*"{text}"*_, assista sua aula em: {class_link}
                        \nQuando concluir a aula, mande um *OK*                                                               
                        \nNão esqueça de:\n- Fazer exercícios.\n- Estudar os conteúdos.'''

        # put here the files implements when it's done...
        if "|" in text:
            try:
                msg.media(text.replace("|", "").strip())
            except:
                msg.body(text)
        else:
            msg.body(text)

        if get_fase() < size_module - 1:
            plus_fase(1)

        elif get_item() < len(current_module) - 1:
            plus_item(1)
            set_fase(0)

        else:
            set_item(0)
            set_fase(0)
            set_count(0)

    elif get_count() < len(flow[get_count()]):

        for i in range(len(flow[get_count()])):
            text += flow[get_count()][i] + " \n\n"

        if get_count() == 1 and get_level() == None:
            if '1' in incoming_msg or '9' in incoming_msg:
                set_level(0)
            elif '2' in incoming_msg or '3' in incoming_msg:
                set_level(1)
            else:
                text = '\n\nDesculpe, não entendi sua resposta. Por favor, tente novamente\n\n'
        elif get_count() == 1:
            if 'matemática' in incoming_msg or 'matematica' in incoming_msg:
                set_subject('matematica')
                plus_count(1)
                text = 'Dê um *ok*, para confirmar a disciplina de Matemática!'
            elif 'portugues' in incoming_msg or 'português' in incoming_msg:
                set_subject('portugues')
                plus_count(1)
                text = 'Dê um *ok*, para confirmar a disciplina de Português!'
            else:
                text = '\n\nDesculpe, não entendi sua resposta. Por favor, tente novamente\n\n'
        else:
            plus_count(1)

        msg.body(text)
    else:
        set_count(0)

    return str(resp)
