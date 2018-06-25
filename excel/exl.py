import pandas as pd

def set_data_type(mydataframe):
	mydataframe['quantity']=mydataframe.quantity.astype(float)
	mydataframe['rate']=mydataframe.rate.astype(float)

#getting excel data into dataframe
myexcel=pd.read_excel('./trades.xlsx')
mydataframe=pd.DataFrame(myexcel)
set_data_type(mydataframe)

#add a new column valus using existing column data 
mydataframe['total']=mydataframe['quantity']*mydataframe['rate']
mydataframe['margin']=mydataframe['total']*1/100

#finding total of margin so as to calculate profit
mydataframe.at['Total','margin']=mydataframe['margin'].sum()

#writting back to excel file
writer=pd.ExcelWriter('./trades.xlsx',engine='xlsxwriter')
mydataframe.to_excel(writer,sheet_name="Sheet1")
writer.save()


