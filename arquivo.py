import pandas as pd
import matplotlib.pyplot as plt

#pandas
df = pd.read_csv('casas_para_alugar.csv')

#exibir a tabela que importamos
print(df)

df = df.rename(columns={'city': 'cidade', 
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
if 'acept' in df['aceita animal?'].values:
    df.loc[df['aceita animal?']=="acept", 'aceita animal?'] = 'aceita'
if 'not acept' in df['aceita animal?'].values:
    df.loc[df['aceita animal?'] == "not acept", 'aceita animal?'] = 'não aceita'

#troca o valor de furnished para mobilhado e not furnished para sem mobilha -> tradução
if 'furnished' in df['mobilhado'].values:
    df.loc[df['mobilhado']=="furnished", 'mobilhado'] = 'mobilhado'
if 'not furnished' in df['mobilhado'].values:
    df.loc[df['mobilhado']=="not furnished", 'mobilhado'] = 'sem mobilha'


#criando uma hipotese que os gastos mensais são apenas o valor do condominio e o valor do lauguel e que os imposto do imovel e seguro fiança é apenas anual. irei calcular os valores mensais, primeiramente

#calcula o valor mensal
df["valores mensais (R$)"] = df["valor condomínio (R$)"] + df["valor do aluguel (R$)"]

#calcula o valor anual de gastos 
df["valores anuais (R$)"] = (df['valores mensais (R$)'] * 12) + df["imposto do imóvel (R$)"] + df["seguro fiança (R$)"]

df.to_csv("Valores analisados - casas para alugar.csv", sep=";")
print(df)

# Agrupar por cidade e calcular a média dos valores mensais
media_valores_mensais = df.groupby('cidade')['valores mensais (R$)'].mean()

# matplotlib
x = media_valores_mensais.index
y = media_valores_mensais.values

plt.bar(x, y)
plt.xlabel("Cidades")
plt.ylabel("Média dos valores mensais (R$)")
plt.title('Valor mensal em média por cidade')

# Adicionar os valores exatos acima das barras
for i, v in enumerate(y):
    plt.text(i, v + 30, f'{v:.2f}', ha='center', va='center', fontsize=8)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("valor mensal em média por cidade.png")
plt.show()

#grafico de pizza
#criando uma figura com 1 linha e 2 colunas, selecionando o segundo subplot para desenhar o grafico
plt.subplot(1, 2, 2)
cidade_counts = df['cidade'].value_counts()
#criando o grafico de pizza -> valores para oo grafico -> define os rotulos das fatias -> formata pra mostrar a porcentagem com uma casa decimal -> define o angulo da primeira fatia da pizza
plt.pie(cidade_counts, labels=cidade_counts.index, autopct='%1.1f%%', startangle=140)
# centralizar o gráfico de pizza 
plt.gca().set_position([0.5, 0.5, 0.5, 0.5])
plt.title('Distribuição das cidades')
plt.tight_layout()
plt.savefig("cidades.png")
plt.show()

#tkinter