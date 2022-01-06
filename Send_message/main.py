from twilio.rest import Client
import pandas as pd

# Your Account SID from twilio.com/console
account_sid = "ACfa8fac753dd24daef7a5675e6aa2ad20"
# Your Auth Token from twilio.com/console
auth_token = "6bd629a66d2b1b6273d4b26b2e6b0cbe"

client = Client(account_sid, auth_token)
# iremos instalar as biblicotecas Pandas, openpyxl e twilio

# Passo a passo para a solução do problema

lista_vendas = ['Vendas']

tabela_vendas = pd.read_excel('Vendas.xlsx')
print(tabela_vendas)
for tabela in lista_vendas:
    if (tabela_vendas['Valor Final'] > 4000).any():
        estabelecimento = tabela_vendas.loc[tabela_vendas['Valor Final'] > 4000, 'ID Loja'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Valor Final'] > 4000, 'Valor Final'].values[0]
        mensagem = f'Foi encontrado em {tabela} alguém que bateu a meta. Estabelecimento: {estabelecimento}, Vendas: {vendas}'
        message = client.messages.create(
            to="+5571999554284",
            from_="+14156494428",
            body=mensagem)

        print(message.sid)
    else:
        message = client.messages.create(
            to="+5571999554284",
            from_="+14156494428",
            body="Ninguém bateu a meta de 3000 mil reais.")

        print(message.sid)

# DevExtreme primeiro abrir os arquivos que mosques ler

# Verificar dentro desses arquivos an coluna de vendas se há valores maiores que 55 mil reais

# Se for maior que 55 mil reais deverá ser enviado um SMS informado quem e o quanto.

# Caso não for maior que 55 mil reais, então nada será feito.
