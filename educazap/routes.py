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
    text = ''
    module_name = ''
    check_math = False
    incoming_msg = request.values.get('Body', '').lower()
    flow = separate_messages('C:/Users/Aluno/cordel-bot/whatsapp-bot/educazap/messages.csv')
    
    if "*" in flow[get_count()][0]:
        module_name = flow[get_count()][0].replace('*', '').lower()
        msg.body(f'{module_name.upper()} {get_fase()+1}/{length_module(module_name)}\n\n' + get_module(module_name, get_fase()))
        if get_fase() < length_module(module_name) - 1:
            plus_fase(1)
        else:
            set_fase(0)
            plus_count(1)
    elif get_count() < len(flow[get_count()]):
        for i in range(len(flow[get_count()])):
            text += flow[get_count()][i] + " \n\n"
        msg.body(text)
        plus_count(1)
    else: 
        set_count(0)

    return str(resp)
