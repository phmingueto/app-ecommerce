# import pytest
# from pandas import DataFrame
#
# from src.application.elt.etl import Engine
# from src.application.helper.get_path import Helper
#
#
# class TestEngine(object):
#     @pytest.fixture
#     def engine(self) -> Engine:
#         return Engine()
#
#     @pytest.fixture
#     def pasta(self) -> str:
#         historyzone = Helper.get_key('HISTORYZONE')
#         return rf'{historyzone}\relatorio_vendas\(13, 7, 2022, datetime.time(18, 5, 16)).xlsx'
#
#     def test_extract_method_should_return_a_dataframe(self, engine, pasta):
#         tabela = engine.extract(pasta=pasta)
#         assert type(tabela) == DataFrame
#
#     def test_group_by_method_should_return_dataframe_with_one_column(self, engine, pasta):
#         table = engine.extract(pasta=pasta)
#         grouped_table = engine.group_by(dataframe=table, column="SkuProduto")
#         assert type(grouped_table) == dict
