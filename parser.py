from requests import get, exceptions
from bs4 import BeautifulSoup
import re


class Parser:

    def __init__(self, url: str):
        self.__url = url
        self.__http = None
        self.__cont = None
        self.__soap = None
        self.__html = None

    def check_valid(self) -> bool:
        try:
            self.__http = get(self.__url)
            self.__cont = self.__http.content
            self.__soap = BeautifulSoup(self.__cont, 'html.parser')
            self.__html = self.__soap.prettify()
        except exceptions.BaseHTTPError as err1:
            print(err1)
        except exceptions.MissingSchema as err2:
            print(err2)
        else:
            return True
        return False

    def get_html(self) -> str:
        return self.__html

    def get_weather(self):
        target_div = self.__soap.select('.region_weather')[0]
        result = target_div.select('.table')[0]
        target_name = result.find_all('a')
        name = [re.sub(r'\s+', ' ', cell.text) for cell in target_name]

        target_cells = result.find_all('span', attrs={'class': 'rw_tmp'})
        temperature = [re.sub(r'\s+', ' ', cell.text) for cell in target_cells]
        for i in range(len(name)):
            print(name[i], temperature[i])

    def get_currency_course(self, url) -> str:
        self.__init__(url)
        if not self.check_valid():
            result = 'Указанный ресурс не найден!'
        else:
            print(f'Ресурс {url} - найден!')
            target_name = self.__soap.find_all('span', attrs={'class': 'biz_name'})
            name = [cell.text for cell in target_name]
            target_cells = self.__soap.find_all('span', attrs={'class': 'biz_bold'})

            courses = [float(cell.text) for cell in target_cells]

            result = 'Курсы валют:\n'
            result += '----------------\n'
            result += f'Валюта: {name[0]}\n'

            result += f'Покупка: {courses[0]:.4f}\n'
            result += f'Продажа: {courses[1]:.4f}\n'
            result += f'НБУ: {courses[3]:.4f}\n'

            result += '----------------\n'
            result += f'Валюта: {name[1]}\n'

            result += f'Покупка: {courses[4]:.4f}\n'
            result += f'Продажа: {courses[5]:.4f}\n'
            result += f'НБУ: {courses[7]:.4f}\n'

            result += '----------------\n'
            result += f'Валюта: {name[2]}\n'

            result += f'Покупка: {courses[8]:.4f}\n'
            result += f'Продажа: {courses[9]:.4f}\n'
            result += f'НБУ: {courses[11]:.4f}\n'

        return result
