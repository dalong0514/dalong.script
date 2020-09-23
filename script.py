import glob, os
import math

import modify as md

import pandas as pd

xlsx = pd.ExcelFile('readsplit.xlsx')
ls = pd.read_excel(xlsx, 'Sheet1')
spdots = ls['dot'].values

print(spdots[1])