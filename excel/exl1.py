import pandas as pd

mydataframe=pd.excel_reader('./trades.xlsx',sheet_name='Sheet1')
for i in mydataframe:
	print(i)
