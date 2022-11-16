#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup
import lxml 

# &page=x, där x i det här fallet = sidan med sökträffar
html = requests.get("https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=mellangatan%2C+haga&EndastDigitaliserat=false&FacettFilter=register_facet%24Folkr%C3%A4kningar%3A%7Cregister_facet%24Folkr%C3%A4kningar%2FFolkr%C3%A4kning+1880%3A&FacettState=undefined%3Ac%7C%2FNjGwA%3Ao%7CaXCRbw%3Ac%7C&typAvLista=Standard&AvanceradSok=True&page=8#tab").text

soup = BeautifulSoup(html, 'lxml')

for a_tag in soup.select('a[href*="/fritext"]'):
    
    link = a_tag['href']
    
    link = link[1:]
    
    # För länkar formaterad som element i en Pythonlista
    print(f'"https://sok.riksarkivet.se/{link}",')
    
    # För "rena" länkar
    # print(f'https://sok.riksarkivet.se/{link}')


# In[ ]:




