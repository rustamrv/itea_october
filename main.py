from lib.parsers import Parser


if __name__ == '__main__':
    address = 'https://meteo.ua/sputnik'
    parser = Parser(address)
    if not parser.check_valid():
        print('Указанный ресурс не найден!')
    else:
        print(f'Ресурс {address} - найден!')

        # Получение HTML-кода целевой страницы
        # ------------------------------------
        # html = parser.get_html()
        # with open('content.html', 'w') as file:
        #    file.write(html)
        # print('Контент страницы успешно сохранен')

        # Получение строки погоды:
        # ------------------------
        parser.get_weather()

        currency_course = parser.get_currency_course("https://korrespondent.net/business/indexes/course_valjut/")
        print(currency_course)
