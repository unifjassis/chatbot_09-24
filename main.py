#encoding: utf-8

from chatbot import ChatBot

myChatBot = ChatBot()

# apenas carregar um modelo pronto
# myChatBot.loadModel()

# criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot para tirar duvidas relacionadas ao PIPE")

pergunta = input("O que deseja saber?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta)

while intencao[0]['intent'] != "despedida":
    pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    # print(resposta + "   [" + intencao[0]['intent'] + "]")
    print(resposta)

print("Chatbot finalizado!")
