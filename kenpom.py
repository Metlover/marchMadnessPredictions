from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re


base_url = 'https://kenpom.com'
f = requests.get(base_url)
soup = BeautifulSoup(f.text, 'html.parser')
table_html = soup.find_all('table', {'id': 'ratings-table'})

thead = table_html[0].find_all('thead')

table = table_html[0]
for x in thead:
    table = str(table).replace(str(x), '')

df = pd.read_html(table)[0]
df2 = pd.DataFrame([[70.5,'Last In','N/A','16-16', 10.975,111.62,70,100.67,89,67.64,180.1,0.0129,155.1,.846,152.5,106.1,143.8,105.26,161.9,-0.101,170.9]])
df = df.append(df2, ignore_index=True)

df.columns = ["Rank", 'School', 'Conf', 'W-L', 'AdjEM', 'AdjO', 'AdjO Rank', 'AdjD', 'AdjD Rank', 'AdjT', 'AdjT Rank', 'Luck', 'Luck Rank', 'AdjEMOpp', 'AdjEMOpp Rank', 'OppO', 'OppO Rank', 'OppD', 'OppD Rank', 'NCSOS AdjEM', 'NCSOS AdjEM Rank']

df['NewOff'] = (df['AdjO'] - min(df['AdjO']))/(max(df['AdjO']) - min(df['AdjO']))
df['NewDef'] = 1 - (df['AdjD'] - min(df['AdjD']))/(max(df['AdjD']) - min(df['AdjD']))
df['NewEff'] = (df['NewOff'] + df['NewDef'])/2

df.to_csv('kenPomRatings.csv', sep=',', encoding='utf-8')
