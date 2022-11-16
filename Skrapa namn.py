#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup
import lxml

people_urls = [
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=1&postid=Folk_121409018&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=2&postid=Folk_121409022&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=3&postid=Folk_121409024&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=4&postid=Folk_121409026&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=5&postid=Folk_121409023&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=6&postid=Folk_121409009&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=7&postid=Folk_121409007&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=8&postid=Folk_121409012&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=9&postid=Folk_121409017&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=10&postid=Folk_121409011&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=11&postid=Folk_121409025&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=12&postid=Folk_121409013&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=13&postid=Folk_121409015&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=14&postid=Folk_121409016&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=15&postid=Folk_121409019&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=16&postid=Folk_121409008&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=17&postid=Folk_121409014&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=18&postid=Folk_121409027&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=19&postid=Folk_121409010&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=20&postid=Folk_121409020&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=21&postid=Folk_121409021&tab=post#tab",
"https://sok.riksarkivet.se/fritext?ValdSortering=A_O&PageSize=100&Sokord=Egendom+N%3ao+59+Bergsgatan&EndastDigitaliserat=false&typAvLista=Standard&AvanceradSok=True&FacettFilter=register_facet%24Folkr%c3%a4kningar%3a%7cregister_facet%24Folkr%c3%a4kningar%2fFolkr%c3%a4kning+1880%3a&FacettState=%2fNjGwA%3ao%7caXCRbw%3ac%7c&page=21&postid=Folk_121409021&tab=post#tab"]

for url in people_urls:
    
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id="content")

    name_elements = results.find_all("div", class_="post_header")

    for name_element in name_elements:
        the_name = name_element.find("h1", class_="post_title")
        print(the_name.text)


# In[ ]:




