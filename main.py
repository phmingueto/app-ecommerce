from src.application.elt.etl import Engine
from src.application.helper.get_path import Helper
import pandas as pd
import datetime


x = Engine()
l = x.extract_all(pasta=f'C:\\Users\\PEDRO\\PycharmProjects\\Downloads\\', typefile='.xls')

print(l)