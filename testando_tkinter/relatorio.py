import pandas as pd
#from pandas_profiling import ProfileReport

data_frame = pd.read_csv('casas_para_alugar.csv')

#verificar o carregamento
print(data_frame)

profile = ProfileReport(Dados, title='Dados Alugueis Capitais', html={'style':{'full_width':True}})
profile.to_notebook_iframe()