# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 21:38:08 2018




This is a temporary script file.
"""
#print(a)
#import beautifulsoup4 as bsp
from bs4 import BeautifulSoup
import requests
#source = requests.get('https://www.cardekho.com/filter/new-cars').text

#source = requests.get('https://www.cardekho.com/new-volvo+cars').text
source = requests.get('https://www.cardekho.com/new-datsun+cars').text
soup=BeautifulSoup(source,'lxml')
main1 = soup.find('div',{'class':'listitems gsc_row'})
for cars in main1.find_all('div',class_='card card_new '):
    carsname = cars.find('div',class_='gsc_col-sm-7 gsc_col-xs-8 gsc_col-md-8 listView holder')
    carsname1 = carsname.h3.a.text
    #print(carsname1)
    carsprice = carsname.find('div','price')
    carsprice1=carsprice.span.text
    #print(carsprice1)
    carsspecs = carsname.find('div','dotlist')
    carsmileage=carsspecs.find('span',title='Mileage')
    #print(carsmileage.text)
    #print(carsprice1)
    #carsspecs = carsname.find('div','dotlist')
    carsdisp=carsspecs.find('span',title='Engine Displacement')
    #print(carsdisp.text)
    
    #carsspecs = carsname.find('div','dotlist')
    carsseat=carsspecs.find('span',title='Seating Capacity')
    #print(carsseat.text)
    with open("..//Desktop//gaurav//test1.csv","a") as myfile:
        print('carname is {} and its price is {} and mileage is {} and with displacement is {} and seating capacity is {}'.format(carsname1,carsprice1,carsmileage.text,carsdisp.text,carsseat.text),file=myfile)
    

with open("..//Desktop//gaurav//test1.csv","a") as myfile:
        #print('carname is {} and its price is {} and mileage is {} and with displacement is {} and seating capacity is {}'.format(carsname1,carsprice1,carsmileage.text,carsdisp.text,carsseat.text),file=myfile)
    print("variants are below",file=myfile)
count = 0 
for vcars in main1.find_all('ul',class_='gsc_thin_scroll'):
    for vcarsname in vcars.find_all('div',class_='gsc_col-md-11 gsc_col-sm-10 gsc_col-xs-10 brandvariantcar'):
        vcarsname1 = vcarsname.a.text
        
        #print(vcarsname1)
        vcarsspecs1 = vcarsname.span.text
        #print(vcarsspecs1)
        with open("..//Desktop//gaurav//test1.csv","a") as myfile:
        #print('carname is {} and its price is {} and mileage is {} and with displacement is {} and seating capacity is {}'.format(carsname1,carsprice1,carsmileage.text,carsdisp.text,carsseat.text),file=myfile)
            print("carname is {} and its specs are {}".format(vcarsname1,vcarsspecs1),file=myfile)
        count +=1

with open("..//Desktop//gaurav//test1.csv","a") as myfile:
    #print('carname is {} and its price is {} and mileage is {} and with displacement is {} and seating capacity is {}'.format(carsname1,carsprice1,carsmileage.text,carsdisp.text,carsseat.text),file=myfile)        
    print("total cars count is {}".format(count),file=myfile)
    print("\n",file=myfile)
        #carsprice = vcarsname.find('div','price')
    #    vcarsspecs=vcarsname1.span.text
        #print(vcarsspecs)
#    carsspecs = carsname.find('div','dotlist')
#    carsmileage=carsspecs.find('span',title='Mileage')
#    print(carsmileage.text)
#    #print(carsprice1)
#    #carsspecs = carsname.find('div','dotlist')
#    carsdisp=carsspecs.find('span',title='Engine Displacement')
#    print(carsdisp.text)
#    
#    #carsspecs = carsname.find('div','dotlist')
#    carsseat=carsspecs.find('span',title='Seating Capacity')
#    print(carsseat.text)
#    
    
    #print(main.prettify())
#print(main1.prettify())
# ==================================================================n===========
#     for carnew1 in main1.find_all('div',{'class':'gsc_col-sm-7 gsc_col-xs-8 gsc_col-md-8 listView holder'}):
#         #print(carnew1.prettify())
#         carname = carnew1.find('div',class_='gsc_col-sm-7 gsc_col-xs-8 gsc_col-md-8 listView holder')
#     #print(carname.prettify())   
#         carname1 = carname.h3.a.text
#         print(carname1)
#         a+=1
#         carprice = carname.div.span.text
#         print(carprice)
#         cardetails = carname.find('div',class_='dotlist')
#         carmileage =cardetails.span.text
#     
#         print(carmileage)
#     
# =============================================================================
    #    main_car_name = carnew1.find('div',class_='gsc_col-sm-7 gsc_col-xs-8 gsc_col-md-8 listView holder')
        #print(main_car_name.prettify())
     #   print(main_car_name.h3.a.text)
# =============================================================================
#     
#     #main_car_variants = main.find('div',class_='expandcollapse matching clear')
#     #print(main_car.prettify())
#     for carnametype in main.find('div',class_='expandcollapse matching clear'):
#         main_car_variants_name = carnametype.find('div',class_='test')
#         #print(main_car_variants_name.prettify())
#        # #--print(main_car_variants_name.h3.a.text)
#         main_car_variants_name_li = main_car_variants_name.find('ul',class_='gsc_thin_scroll')
#         #main_car_variants_name_li = main_car_variants_name.find('div',class_='variantlist   clearfix')
#         #main_car_variants_name_li = main_car_variants_name.find('div',class_='variantlist   clearfix')
#         #print(main_car_variants_name_li.prettify())
#         count = 0
#         
#         for card in main_car_variants_name_li.find_all('div',class_='gsc_col-md-11 gsc_col-sm-10 gsc_col-xs-10 brandvariantcar'):
#         #print(main_car_variants_name_li.prettify())
#             count +=1
#             carname1 = card.a.text
#             carlabelling = card.span.text
#             print('carname is {0} and features are {1}'.format(carname1,carlabelling))
#             
#     print(count) 
#     
#    
#         
# =============================================================================
#count2 = count + count1
#print(count2)