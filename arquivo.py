import pandas as pd

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