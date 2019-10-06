#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

#Open page and grab HTML
my_url = ('https://www.eia.gov/dnav/ng/hist/rngwhhdM.htm')
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parser 
page_soup = soup(page_html, 'html.parser')

table = []

#Find table
ele_table = page_soup.find_all("table", width ="675")

#Find table 2
ele_table2 = ele_table[2]

#traverse table
col_tag = 'th'
ele_rows = ele_table2.find_all('tr',recursive=False)
for ele_row in ele_rows:
    row = []
    ele_cols = ele_row.find_all(col_tag, recursive =False)
    for ele_col in ele_cols:
        #use empty string for no data column
        content = ele_col.string.strip() if ele_col.string else ''
        row.append(content)
    col_tag = 'td'
    #just save row with data
    if any(row):
        table.append(row)
        
#open CSV file
file = open('GasPriceMonthly.csv','w')
writer = csv.writer(file)
        
        
        
#print table
for row in table:
    writer.writerow(row)
    print('\t'.join(row))
    
#Close CSV file
file.close()


# In[ ]:





# In[ ]:





# In[ ]:




