import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacao["text"] = texto
    #print(texto)

#pegar_cotacoes()


#1- janela principal
janela = Tk()

#alterar o titulo
janela.title("cotação atual das moedas")

#tamanho da janela 
janela.geometry("400x400")

#incrementar o texto -. texto dentro da janela é label
texto_orientacao = Label(janela, text= 'Clique no botão para ver a cotação das moedas')
texto_orientacao.grid(column=0, row=0, padx= 10, pady=10)

botao = Button(janela, text='Buscar cotação', command=pegar_cotacoes)
botao.grid(column=0,row=1, padx= 10, pady=10)
#texto que sera exibido dentro da janela
texto_cotacao = Label(janela, text="")
#espaço padx e pady
texto_cotacao.grid(column=0, row=2, padx= 10, pady=10)

#exibe a janela -> ultima linha de codigo
janela.mainloop()

#pra pessoa nao ter que rodar o codigo, tem que colocar em arquivo executavel