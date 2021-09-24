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

    if "*" in flow[get_count()][0]:
        for i in math_modules:
            module_name = i
            temp_count += 1
            if temp_count > get_item():
                break

        text = get_math_module(module_name, get_fase(), 0)
        if "|" in text:
            try: 
                msg.media(text.replace("|", "").strip())
            except:
                msg.body(text)
        else:
            msg.body(text)

        if get_fase() < length_math_module(module_name) - 1:
            plus_fase(1)

        elif get_item() < len(math_modules) - 1:
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
        msg.body(text)
        plus_count(1)
    else: 
        set_count(0)

    return str(resp)
