import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import Tk, Label, Button, filedialog, messagebox
from pandasgui import show
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
    def __init__(self, janela):
        self.janela = janela
        janela.title('Análise de casa para alugar')

        self.texto_orientacao = Label(janela, text='Análise de dados de locais para alugar por meio de daos e gráficos')
        self.texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

        #self.carregar_botao = Button(janela, text='Carregar CSV', command=self.carrega_csv)
        #self.carregar_botao.grid(column=0, row=1, padx=10, pady=10)

        self.mostra_botao = Button(janela, text='Mostra tabela', command=self.mostra_tabela)
        self.mostra_botao.grid(column=0, row=2, padx=10, pady=10)

        self.grafico_botao = Button(janela, text='Mostra gráficos', command=self.mostra_grafico)
        self.grafico_botao.grid(column=0, row=3, padx=10, pady=10)

        self.df = None
    
    def carrega_csv(self):
        self.df = pd.read_csv('casas_para_alugar.csv')
        #path_arquivo = filedialog.askopenfilename()

        #if path_arquivo: 
                #deixa o caminho direto ou path_arquivo
            #self.df = pd.read_csv('casas_para_alugar.csv')
            #self.df = pd.read_csv(path_arquivo)
            self.df = self.df.rename(columns={'city': 'cidade', 
                            'rooms': 'quartos', 
                            'bathroom': 'banheiro', 
                            'parking spaces': 'estacionamento', 
                            'floor': 'andar',
                            'animal': 'aceita animal?',
                            'furniture': 'mobilhado', 
                            'hoa (R$)': 'valor condomínio (R$)', 
                            'rent amount (R$)': 'valor do aluguel (R$)', 
                            'property tax (R$)': 'imposto do imóvel (R$)',
                            'fire insurance (R$)': 'seguro fiança (R$)'})
            
            #troca o valor de acept para aceita e nor acept para nao aceita -> tradução
            if 'acept' in self.df['aceita animal?'].values:
                self.df.loc[self.df['aceita animal?']=="acept", 'aceita animal?'] = 'aceita'
            if 'not acept' in self.df['aceita animal?'].values:
                self.df.loc[self.df['aceita animal?'] == "not acept", 'aceita animal?'] = 'não aceita'

            #troca o valor de furnished para mobilhado e not furnished para sem mobilha -> tradução
            if 'furnished' in self.df['mobilhado'].values:
                self.df.loc[self.df['mobilhado']=="furnished", 'mobilhado'] = 'mobilhado'
            if 'not furnished' in self.df['mobilhado'].values:
                self.df.loc[self.df['mobilhado']=="not furnished", 'mobilhado'] = 'sem mobilha'

            #criando uma hipotese que os gastos mensais são apenas o valor do condominio e o valor do lauguel e que os imposto do imovel e seguro fiança é apenas anual. irei calcular os valores mensais, primeiramente
            #calcula o valor mensal
            self.df["valores mensais (R$)"] = self.df["valor condomínio (R$)"] + self.df["valor do aluguel (R$)"]

            #calcula o valor anual de gastos 
            self.df["valores anuais (R$)"] = (self.df['valores mensais (R$)'] * 12) + self.df["imposto do imóvel (R$)"] + self.df["seguro fiança (R$)"]

            self.df.to_csv("Valores analisados - casas para alugar.csv", sep=";")

            messagebox.showinfo("Info", "Arquivo CSV carregado e processado com sucesso!")
            self.mostra_botao.config(state='normal')
            self.grafico_botao.config(state='normal')

    def mostra_tabela(self):
        if self.df is not None:
            show(self.df)

    def mostra_grafico(self):
        if self.df is not None:
            media_valores_mensais = self.df.groupby('cidade')['valores mensais (R$)'].mean()
            x = media_valores_mensais.index
            y = media_valores_mensais.values

            plt.figure(figsize=(12, 6))

            # Gráfico de barras
            plt.subplot(1, 2, 1)
            plt.bar(x, y)
            plt.xlabel("Cidades")
            plt.ylabel("Média dos valores mensais (R$)")
            plt.title('Valor mensal em média por cidade')

            for i, v in enumerate(y):
                plt.text(i, v + 30, f'{v:.2f}', ha='center', va='center', fontsize=8)

            plt.xticks(rotation=45)
            plt.tight_layout()

            # Gráfico de pizza
            plt.subplot(1, 2, 2)
            cidade_counts = self.df['cidade'].value_counts()
            plt.pie(cidade_counts, labels=cidade_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribuição das cidades')

            plt.tight_layout()
            plt.savefig("graficos.png")
            plt.show()
root = Tk()
app = App(root)
root.mainloop()