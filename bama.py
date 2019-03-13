from bs4 import BeautifulSoup
import requests

class BamaCar:
    
    def __init__(self,car_model,car_brand,province,isAutomatic = False,year = 1397-1397,page_count = [1,2,3,4,5,6,7,8,9,10,11,12]):

        self.car_isAuto = isAutomatic
        self.car_brand = car_brand
        self.car_province = province
        self.car_page_count = page_count
        self.car_model = car_model
        self.car_year = year
        self.list_price_car = list()

    def seperator(self,inside_number):
        spliter = inside_number.strip().split(' ')
        if len(spliter)>=2:
            replaced = spliter[0].replace(',','')
            if replaced.isdigit():
                self.list_price_car.append(replaced)
               

    def sort_array(self):
        print(f'minimum number is :{min(self.list_price_car)}')
        print(f'maximum number is :{max(self.list_price_car)}')
        
    def fetch_data(self):

        for count in self.car_page_count:
            print(f'I am on Page :{count}')
            base_url = 'https://bama.ir/car/'
            complete_url = base_url + f'{self.car_brand}/{self.car_model}/all-trims?province={self.car_province}&trans=2&year={self.car_year}&page={count}'
            url_link_get = requests.get(complete_url)
            print(f'url is {complete_url}')

            soup = BeautifulSoup(url_link_get.text,'html.parser')
            main_banner_2 = soup.find('div',class_='eventlist clearfix')
            inside_0 = main_banner_2.find('ul')
            inside_1 = inside_0.find_all('li',itemtype = 'http://schema.org/Car')

            for fetch_price in inside_1:
                inside_2 = fetch_price.find('div',class_= 'listdata')
                inside_3 = inside_2.find('div',class_='overview')
                inside_4 = inside_3.find('p',class_='cost')

                self.seperator(inside_4.text)
            
        self.sort_array()     
               
    def choose_your_url(self):
        
        if self.car_isAuto == True:
            
            # url_link_get = requests.get(base_url + self.car_brand +'/all-models/all-trims?trans=2')
            self.fetch_data()

        else:
            pass

obj = BamaCar('207','peugeot','isfahan',True,1396-1396,[1])
obj.choose_your_url()
