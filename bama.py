from bs4 import BeautifulSoup
import requests

class BamaCar:
    
    def __init__(self,province,isAutomatic = False,car_brand = 'unknown'):

        self.isAuto = isAutomatic
        self.car_brand = car_brand
        self.province = province
        # self.car_model = car_model


    def fetch_data(self):

        base_url = 'https://bama.ir/car/'

        url_link_get = requests.get(base_url + self.car_brand +'/all-models/all-trims?trans=2')

        #print(url_link_get.text)

        soup = BeautifulSoup(url_link_get.text,'html.parser')

        main_banner_2 = soup.find('div',class_= 'eventlist clearfix')

        inside_0 = main_banner_2.find('ul')
        
        inside_1 = inside_0.find_all('li',itemtype = 'http://schema.org/Car')

        for fetch_price in inside_1:
            
            inside_2 = fetch_price.find('div',class_= 'listdata')

            if not(inside_2 is None):

                inside_3 = inside_2.find('div',class_='overview')
        
                inside_4 = inside_3.find('p',class_='cost')
                inside_5 = inside_4.find('span',itemgroup= 'price')
                print(inside_5)

                

               

 

    def choose_your_url(self):
        
        # base_url = 'https://bama.ir/car/'

        if self.isAuto == True:
            
            # url_link_get = requests.get(base_url + self.car_brand +'/all-models/all-trims?trans=2')
            self.fetch_data()

        else:
            pass

        #     url_link_get = requests.get(base_url + self.car_brand + '/all-models/all-trims?trans=1')
            
        
        # print(f'your url is {url_link_get.url}')
        # print(f'your car model is {self.car_brand}')


obj = BamaCar('tabriz',True,'toyota')
obj.choose_your_url()
 