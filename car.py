# -*- coding: utf-8 -*-
"""
Spyder Editor



This is a temporary script file.
"""

import numpy as np
a = np.arange(20)
a = 0
#print(a)
#import beautifulsoup4 as bsp
from bs4 import BeautifulSoup
import requests
source = requests.get('https://www.cardekho.com/filter/new-cars').text
soup=BeautifulSoup(source,'lxml')
#with open('..//Desktop//gaurav//new.html','w') as f:
for card in soup.find_all('div',class_='card card_new '):

    #print(card.prettify()) 
    carname = card.find('div',class_='gsc_col-sm-7 gsc_col-xs-8 gsc_col-md-8 listView holder')
    #print(carname.prettify())   
    carname1 = carname.h3.a.text
    print(carname1)
    a+=1
    carprice = carname.div.span.text
    print(carprice)
    cardetails = carname.find('div',class_='dotlist')
    carmileage =cardetails.span.text
    
    print(carmileage)
        #f.writelines()
        #print(soup.prettify(),file=f)

print(a)