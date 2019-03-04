from sys import argv

try:
    urls = argv[1]
except IndexError:
    urls = ['https://news.mail.ru/incident/36501659/',
       'https://humanparts.medium.com/an-account-of-a-descent-into-youtube-addiction-3b0a2e345a8b',
       'https://lenta.ru/news/2019/02/28/russia_medal/',
       'https://lenta.ru/news/2019/03/01/chrome/',
       'https://www.gazeta.ru/business/2019/02/26/12209467.shtml',
       'https://pythonworld.ru/osnovy/inkapsulyaciya-nasledovanie-polimorfizm.html',
       'https://www.gazeta.ru/social/2019/03/03/12221329.shtml']


''' переменная для выбора как будет формироваться имя файла. 
    если file_name_setting = 1, то файл упадет в дерикторию с названием сайта
    если = 0, то в корневую дерикторию, но с именем как ссылка на данный сайт 
'''

file_name_setting = 1

''' переменная для выделения нужных тэгов для вытаскивания из сайта, так как 
    сайты построены по разному, то и теги информативные, иногда, разные, поэтому 
    этот варинат можно настраивать'''
tags = ['h1', 'h2', 'p', 'code']

