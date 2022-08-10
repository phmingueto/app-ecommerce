from src.application.elt.etl import Engine
from src.application.helper.get_path import Helper
import datetime

today = datetime.date.today()

engine = Engine()

init = engine.extract(pasta=rf"\Users\\PEDRO\Downloads\ResumoFinanceiro (13).xlsx")

engine.write(dataframe= init,
             pasta= rf"{Helper.get_key('RAWZONE')}\relatorio_vendar_2\{today.year}\{today.month}\{today.day}",
             file=f'resumo_financeiro.xlsx')

raw_table = engine.extract(pasta=rf"{Helper.get_key('RAWZONE')}\relatorio_vendar_2\{today.year}\{today.month}\{today.day}\resumo_financeiro.xlsx")

try:
    history_table = engine.extract(pasta=rf"{Helper.get_key('HISTORYZONE')}\\resumo_financeiro\\resumo_financeiro.xlsx")
    final_history_table = engine.concat_table(table_one=history_table, table_two=raw_table, colun='codigoPedido')

except FileNotFoundError:
    final_history_table = raw_table

engine.write(dataframe=final_history_table,
             pasta=rf"{Helper.get_key('HISTORYZONE')}\\resumo_financeiro",
             file="resumo_financeiro.xlsx")

print('ok')
