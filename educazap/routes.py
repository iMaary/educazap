from bot import app
from flask import request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from msgs_treatment import separate_messages
from global_variables import *

@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    flow = separate_messages('C:/Users/Aluno/cordel-bot/whatsapp-bot/educazap/messages.csv')
    incoming_msg = request.values.get('Body', '').lower()
    module_name = ''
    text = ''
    temp_count = 0
    current_module = None
    size_module = None
  
    if "*" in flow[get_count()][0]:
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
            # set_item(0)
            # plus_count(1)

    elif get_count() < len(flow[get_count()]):
    
        for i in range(len(flow[get_count()])):
            text += flow[get_count()][i] + " \n\n"

        if get_count() == 1 and get_level() == None:
            if '1' in incoming_msg or '9 ano' in incoming_msg:
                set_level(0)
            elif '2' in incoming_msg or '3 ano' in incoming_msg:
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
