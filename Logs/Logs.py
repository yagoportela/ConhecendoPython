import pandas as pd
import logging
import logging.config
import json

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')

print('Inicio')
print('_' * 100)

tabela_vendas = pd.read_excel('../Arquivos/Vendas.xlsx')
pd.set_option('display.max_columns', None)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
ticket_medio = (faturamento['Valor Final'] /quantidade['Quantidade']).to_frame()

faturamento_json = faturamento.to_json()
quantidade_json = quantidade.to_json()
ticket_medio_json = ticket_medio.to_json()

print('\n')
print('Faturamento')
print('_' * 100)
print(faturamento)
print('\n')
print('Quantidade')
print('_' * 100)
print(quantidade)
print('\n')
print('Ticket Medio')
print('_' * 100)
print(ticket_medio)
print('\n')
print('\n')

print('Faturamento')
print('_' * 100)
logger.info('Faturamento', extra=json.loads(faturamento_json))
print('\n')
print('Quantidade')
print('_' * 100)
logger.info('Quantidade', extra=json.loads(quantidade_json))
print('\n')
print('Ticket Medio')
print('_' * 100)
logger.info('Ticket Medio', extra=json.loads(ticket_medio_json))
print('\n')
print('\n')
