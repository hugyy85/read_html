import requests, sys, bs4, re, os
from config import tags
import pdb
class Find_text():
    def __init__(self, url, file_name_setting=1):
        self.url = url
        self.file_name_setting = file_name_setting
        self.new_name, self.new_dir = self.rename_url()

    # функция для поиска параграфов и загаловков
    def find_text(self):

        response = requests.get(self.url)
        soup = bs4.BeautifulSoup(response.content, 'lxml')
        text = soup.findAll(tags)
        return text

    # парсинг найденого и запись всего в файл
    def write_text_to_file(self, text):

        with open(self.new_dir + self.new_name, 'w', encoding='utf-8') as f:
            for i in text:
                if i.string != None: # ели в тэге только строка
                    f.write(i.string + '\n' + '\n')

                else: # если есть что то помимо строки

                    for j in i: # разбираем каждый элемент тэга
                        try:
                            if len(i) - 1 == i.index(j):  # если последний элемент параграфа, то добавляем пропуск
                                f.write(j.string + '\n' + '\n')

                            elif i.a.string == j.string:  # если в элементе есть ссылка, то вывод ее в квадратных скобках
                                var = i.a['href']
                                f.write(f'[{var}]')
                                try:
                                    f.write(j.string)
                                except:
                                    f.write('\n')

                            else:  # если ссылок нет, то записываем содержимое параграфа
                                try:
                                    f.write(j.string)
                                except:
                                    f.write('\n')
                        except:
                            pass


        print(f"Данные записаны в файл с именем {self.new_name}")
        return

    def del_html(self, name):
        a = name.partition('.')
        return a[0]


    # переименование имени файла
    def rename_url(self):
        new_name = ''
        new_dir = ''

        if self.file_name_setting == 0:  # имя файла в корневой директории
            new_name = self.url[8:len(self.url)-1].replace('/', '-') + '.txt'

        elif self.file_name_setting == 1: # имя файла в новой директории

            variant = 0 # variant либо 1 либо 2 в зависимости от конца url
            new_name_list = self.url.split('/')
            new_dir = ''
            if new_name_list[-1] == "":
                variant = 2
            elif new_name_list[-1]:
                variant = 1
            for i in range(1, len(new_name_list)-variant):
                new_dir += new_name_list[i] + '\\'

            new_dir = f'{os.getcwd()}' + new_dir
            try:
                os.makedirs(new_dir)
            except FileExistsError:
                pass
            new_name = self.del_html(new_name_list[-variant]) + '.txt'

        return new_name, new_dir

class Formating_file(Find_text):

    def check_width(self, word, count, result):
        if len(word) > 80:
            result += '\n' + word + '\n'
            count = 0
        elif len(word) + count < 80:
            result += word + ' '
        elif len(word) + count >= 80:
            result += '\n' + word + ' '
            count = len(word) + 1

        return result, count

    def width_of_string(self):
        count = 0
        result = ''
        with open(self.new_dir + self.new_name, 'r', encoding='utf-8') as f:
            text = f.read()

        text = text.split(' ')

        for i in text:
            if '\n' in i: # проверка на склейку двух слов символами \n\n
                for j in i.split('\n'):
                    if j == '':
                        result += '\n\n'
                        count = 0
                    elif j:
                        result, count = self.check_width(j, count, result)
                        count += len(j) + 1

                continue

            if len(i) + count < 80:  # если строка + новое слово меньше 80 символов, то запиываем
                result, count = self.check_width(i, count, result)
            elif len(i) + count >= 80:  # если нет, то переносим это слово на следующую строку
                result, count = self.check_width(i, count, result)
                continue

            count += len(i) + 1 # учитываем длины слова и пробел
        with open(self.new_dir + self.new_name, 'w') as f: # перезапись файла в отформатировном фиде
            f.write(result)

        return print(f'Файл {self.new_name} отформатирован в удобный для чтения вид')




