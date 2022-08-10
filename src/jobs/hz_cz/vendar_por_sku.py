from src.application.elt.etl import Engine
from src.application.helper.get_path import Helper


engine = Engine()
history_table = engine.extract(pasta=rf"{Helper.get_key('HISTORYZONE')}\resumo_financeiro\resumo_financeiro.xlsx")

grouped_history_by_sku = engine.group_by(column="SkuProduto", dataframe=history_table)

for key in grouped_history_by_sku:
    engine.write(pasta=rf"{Helper.get_key('CONZUMEZONE')}\vendas_por_sku\{key}",
                 file=f"{key}.xlsx",
                 dataframe=grouped_history_by_sku[key])
