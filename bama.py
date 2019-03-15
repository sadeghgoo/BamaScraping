from bs4 import BeautifulSoup
import requests
import math
import time

class BamaCar:
    
    def __init__(self,car_model,car_brand,province,isAutomatic = False,year = '1397-1397',body_condition = 1):
        self.car_isAuto     = isAutomatic
        self.car_brand      = car_brand
        self.car_province   = province
        self.body_condition = body_condition
        self.car_model      = car_model
        self.car_year       = year
        self.car_page_count = [1]
        self.list_price_car = list()
        self.url_list_car   = list()
        
    def seperator(self,inside_number):
        spliter = inside_number.strip().split(' ')
        if len(spliter)>=2:
            replaced = spliter[0].replace(',','')
            if replaced.isdigit():
                self.list_price_car.append(replaced)
                return True
        else:
            return False 

    def sort_array(self):
        mini = self.list_price_car.index(min(self.list_price_car))
        maxi = self.list_price_car.index(max(self.list_price_car))
        print(f'minimum number is :{min(self.list_price_car)} and index is {mini}  ')
        print(f'maximum number is :{max(self.list_price_car)} and index is {maxi}  ')
        print(f'smal url is {self.url_list_car[mini]}')
        print(f'max url is {self.url_list_car[maxi]}')
        #print(self.list_price_car)

    def fetch_number_rigistered_cars(self,url_query_rigestered): # return number of rigistered cars 
        base_url_rigistered = 'https://bama.ir/car/'
        url_rigistered = f'{base_url_rigistered}{url_query_rigestered}'
        url_link_get_rigistered = requests.get(url_rigistered)
        print(url_rigistered)
        soup_1 = BeautifulSoup(url_link_get_rigistered.text,'html.parser')
        inside_rigistered_0 = soup_1.find('div',class_='paging-bottom-div hidden-xs')

        if inside_rigistered_0 != None:
            maximum_rigistered = inside_rigistered_0.text
            spliter_rigistered = maximum_rigistered.strip().split(' ')
            divided = int(spliter_rigistered[-2])/12
            ceiled = math.ceil(divided)
            for number_rig in range(1,ceiled):
                self.car_page_count.append(number_rig+1)
            print(self.car_page_count)
        
    def fetch_data(self,url_query):

        self.fetch_number_rigistered_cars(url_query)

        for count in self.car_page_count:
            base_url = 'https://bama.ir/car/'           
            complete_url = f'{base_url}{url_query}&page={count}'
            url_link_get = requests.get(complete_url)

            soup = BeautifulSoup(url_link_get.text,'html.parser')
            main_banner_2 = soup.find('div',class_='eventlist clearfix')
            inside_0 = main_banner_2.find('ul')
            inside_1 = inside_0.find_all('li',itemtype = 'http://schema.org/Car')

            for fetch_price in inside_1:
                inside_2   = fetch_price.find('div',class_= 'listdata')
                inside_3   = inside_2.find('div',class_='overview')
                inside_4   = inside_3.find('p',class_='cost')
                inside_2_1 = inside_2.find('div',class_='detail')
                inside_2_2 = inside_2_1.find('div',class_='addetailpage-div cartitlediv')
                inside_2_3 = inside_2_2.find('a')
             
                bool_check_url = self.seperator(inside_4.text)
                if bool_check_url == True:
                    self.url_list_car.append('https://www.bama.ir' + inside_2_3.get('href'))
               
        self.sort_array()     
               
    def choose_your_url(self):
        
        if self.car_isAuto == True:   

            self.fetch_data(f'{self.car_brand}/{self.car_model}/all-trims?province={self.car_province}&trans=2&status={self.body_condition}&instalment=0&year={self.car_year}')
        else:

            self.fetch_data(f'{self.car_brand}/{self.car_model}/all-trims?province={self.car_province}&trans=1&status={self.body_condition}&instalment=0&year={self.car_year}')
 


obj = BamaCar('optima','kia','tehran',True,'2016-2016','1')
obj.choose_your_url()
