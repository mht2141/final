####################
# Name : Min-Hua Tsou
# UNI : mht2141
#
# This modifies a csv file from Japan Tourism Statistics. It reads the table as a 
# pandas DataFrame, processes the table, and pivots the table according to the 
# Country and the Year.
####################

import pandas as pd

def jpstatistics():
    '''This function modifies a csv file from Japan Tourism Statistics. It reads 
    the table as a pandas DataFrame, processes the table, and pivots the table 
    according to the Country and the Year.'''
    
    #reads the csv file
    data = pd.read_csv('japanstat.csv')
    
    #converts the file to a pandas DataFrame
    df = pd.DataFrame(data=data, columns=['Country', 'Month', 'Year', 'Visitors'])
    
    #removes the extra commas in the Visitors data 
    df['Visitors'] = df['Visitors'].replace(',','', regex=True)
    
    #converts the Visitors data to floats
    df['Visitors'] = df['Visitors'].astype(float)
    
    #pivots the table by Country and Year
    df = df.pivot_table(index=["Country", "Year"], values=['Visitors'])
    
    #renders DataFrame as a html table
    df = df.to_html()  
    
    return df 



