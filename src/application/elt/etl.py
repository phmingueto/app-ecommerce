from collections import OrderedDict
import pandas as pd
from pandas import DataFrame
import os


class Engine(object):

    @staticmethod
    def extract(pasta: str) -> DataFrame:
        return pd.read_excel(pasta)

    @staticmethod
    def group_by(column: str, dataframe: DataFrame) -> dict:
        table = dataframe.groupby([column])
        groups = table.groups.keys()
        groups_dict = dict()
        for group in groups:
            group_table = table.get_group(group)
            current_dict = {group: group_table}
            groups_dict = {**groups_dict, **current_dict}
        return groups_dict

    @staticmethod
    def write(pasta: str, dataframe: DataFrame, file: str) -> None:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        fullname = os.path.join(pasta, file)
        dataframe.to_excel(excel_writer=fullname, index=False)

    @staticmethod
    def concat_table(table_one: DataFrame, table_two: DataFrame, colun: str) -> DataFrame:
        concat_table = pd.concat([table_one, table_two], ignore_index=True)
        drop_table = concat_table.drop_duplicates(colun)
        return drop_table

    @staticmethod
    def modify_column(dataframe: DataFrame, dict_column: dict, column_key: str, column_value: str) -> DataFrame:
        for k, v in dict_column.items():
            dataframe.loc[getattr(dataframe, column_key) == k, column_value] = v
        return dataframe

    @staticmethod
    def column_dict_drop(dataframe: DataFrame, column_one: str, column_two: str) -> dict:
        key_list = dataframe[column_one].tolist()
        key_list_drop = list(OrderedDict.fromkeys(key_list))
        value_list = dataframe[column_two].tolist()
        value_list_drop = list(OrderedDict.fromkeys(value_list))
        return dict(zip(key_list_drop, value_list_drop))
