# -*-coding:utf-8-*-
import re
import json
import random

TALE = open("Fairytale.json")
data = json.load(TALE)


# Открываем меню
def menu():
    try:
        welcome = int(input(data["welcome"]["1"]))  # определяемся какую сказку мы хотим: Сразу готовую или по
        # шаблону
        if welcome == 1:
            print(patternselection())
        else:
            print(random.choice(data["tales"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        menu()


# Выбираем шаблон
def patternselection():
    try:
        template = int(input(data["welcome"]["2"]))  # В случае выбора сказки по шаблону, выбираем шаблон
        if template == 1:
            patternRyaba()
        elif template == 2:
            print(patternMedvedi())
        elif template == 3:
            print(patternDonkey())
        elif template == 4:
            print(patternTopor())
        elif template == 5:
            print(patternFoxAndGoat())
    except ValueError:
        print("Ой, что-то пошло не так. Используйте только цифры !")
        patternselection()


def get_ready_tale():
    return random.choice(data["tales"])


# функция предлагает загрузить оригинал
def original(tale):
    try:
        orig = int(input("Хотите увидеть оригинал сказки?\n1.Да, хочу\n2.Нет, не хочу\n"))
        if orig == 1:
            print(tale, menu())
        else:
            menu()
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")

        # ШАБЛОНЫ


# Выбираем способ заполнения шаблона Курочка Ряба
def patternRyaba():
    try:
        vvod = int(input(data["welcome"]["3"]))
        if vvod == 1:
            print(Ryaba(), original(data["ryaba"]["original"]))
        elif vvod == 2:
            print(AvtoRyaba(), original(data["ryaba"]["original"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        patternRyaba()


# Cледующая функция задает вопросы пользователю и вставляет их в шаблон "Курочки Рябы"
def Ryaba():
    text1 = re.sub(u'[Дд]ед', (input(data["ryaba"]["questions"]["1"])).decode('utf-8'),
                   data["ryaba"]["original"])
    text2 = re.sub(u'[Бб]аба', (input(data["ryaba"]["questions"]["2"])).decode('utf-8'), text1)
    text3 = re.sub(u'ряба', (input(data["ryaba"]["questions"]["3"])).decode('utf-8'), text2)
    text4 = re.sub(u'яичко', (input(data["ryaba"]["questions"]["4"])).decode('utf-8'), text3)
    text5 = re.sub(u'простое', (input(data["ryaba"]["questions"]["5"])).decode('utf-8'), text4)
    text6 = re.sub(u'золотое', (input(data["ryaba"]["questions"]["6"])).decode('utf-8'), text5)
    text7 = re.sub(u'Мышка', (input(data["ryaba"]["questions"]["7"])).decode('utf-8'), text6)
    text8 = re.sub(u'хвостиком', (input(data["ryaba"]["questions"]["8"])).decode('utf-8'), text7)
    print("\nВаша сказка готова:")
    return text8


# Cледующая функция случайным образом заполняет шаблон "Курочки Рябы"
def AvtoRyaba():
    text1 = re.sub(u'[Дд]ед', random.choice(data["man"]), data["ryaba"]["original"])
    text2 = re.sub(u'[Бб]аба', random.choice(data["woman"]), text1)
    text3 = re.sub(u'ряба', random.choice(data["namebirds"]), text2)
    text4 = re.sub(u'яичко', random.choice(data["subj"]), text3)
    text5 = re.sub(u'простое', random.choice(data["adj"]), text4)
    text6 = re.sub(u'золотое', random.choice(data["adj"]), text5)
    text7 = re.sub(u'Мышка', random.choice(data["animalswoman"]), text6)
    text8 = re.sub(u'хвостиком', random.choice(data["part"]), text7)
    return text8


# Выбираем способ заполнения шаблона donkey
def patternDonkey() -> object:
    try:
        vvod = int(input(data["welcome"]["3"]))
        if vvod == 1:
            print(donkey(), original(data["donkey"]["original"]))
        elif vvod == 2:
            print(Avtodonkey(), original(data["donkey"]["original"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        patternDonkey()


# Заполняем шаблон Ослик с клавиатуры
def donkey():
    text1 = re.sub(u'ос[ёе]л', (input(data["donkey"]["questions"]["1"])).decode('utf-8'),
                   data["donkey"]["original"])
    text2 = re.sub(u'уши', (input(data["donkey"]["questions"]["2"])).decode('utf-8'), text1)
    text3 = re.sub(u'маленькие', (input(data["donkey"]["questions"]["3"])).decode('utf-8'), text2)
    text4 = re.sub(u'большие', (input(data["donkey"]["questions"]["4"])).decode('utf-8'), text3)
    text5 = re.sub(u'длинные', (input(data["donkey"]["questions"]["5"])).decode('utf-8'), text4)
    text6 = re.sub(u'круглые', (input(data["donkey"]["questions"]["6"])).decode('utf-8'), text5)
    text7 = re.sub(u'Их дают бесплатно', (input(data["donkey"]["questions"]["7"])).decode('utf-8'), text6)
    text8 = re.sub(u'осла', (input(data["donkey"]["questions"]["8"])).decode('utf-8'), text7)
    print("\nВаша сказка готова:")
    return text8


# ЗАполняем Шаблон ослик случайным образом
def Avtodonkey():
    word = random.choice(data["animalm"])
    text1 = re.sub(u'осёл', word, data["donkey"]["original"])
    text2 = re.sub(u'уши', random.choice(data["plural"]), text1)
    text3 = re.sub(u'маленькие', random.choice(data["adjpl"]), text2)
    text4 = re.sub(u'большие', random.choice(data["adjpl"]), text3)
    text5 = re.sub(u'длинные', random.choice(data["adjpl"]), text4)
    text6 = re.sub(u'круглые', random.choice(data["adjpl"]), text5)
    text7 = re.sub(u'бесплатно', random.choice(data["how"]), text6)
    text8 = re.sub(u'осла', word + u'а', text7)
    print("\nВаша сказка готова:")
    return text8


# Выбираем способ заполнения шаблона Три медведя
def patternMedvedi():
    try:
        vvod = int(input(data["welcome"]["3"]))
        if vvod == 1:
            print(Medvedi(), original(data["medvedi"]["original"]))
        elif vvod == 2:
            print(AvtoMedvedi(), original(data["medvedi"]["original"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        patternMedvedi()


# Заполняем шаблон "Три медведя" с клавиатуры
def Medvedi():
    text1 = re.sub(u'в лес', (input(data["medvedi"]["questions"]["1"])).decode('utf-8'),
                   data["medvedi"]["original"])
    text2 = re.sub(u'в лесу', (input(data["medvedi"]["questions"]["2"])).decode('utf-8'), text1)
    text3 = re.sub(u'большой', (input(data["medvedi"]["questions"]["3"])).decode('utf-8'), text2)
    text4 = re.sub(u'лохматый', (input(data["medvedi"]["questions"]["4"])).decode('utf-8'), text3)
    text5 = re.sub(u'гулять по лесу', (input(data["medvedi"]["questions"]["5"])).decode('utf-8'), text4)
    text6 = re.sub(u'голодные', (input(data["medvedi"]["questions"]["6"])).decode('utf-8'), text5)
    text7 = re.sub(u'сдвинул', (input(data["medvedi"]["questions"]["7"])).decode('utf-8'), text6)
    text8 = re.sub(u'сломал', (input(data["medvedi"]["questions"]["8"])).decode('utf-8'), text7)
    print("\nВаша сказка готова:")
    return text8


# Заполняем шаблон "Три Медведя" случайным образом
def AvtoMedvedi():
    text1 = re.sub(u'в лес', random.choice(data["place1"]), data["medvedi"]["original"])
    text2 = re.sub(u'[Вв] лесу', random.choice(data["place2"]), text1)
    text3 = re.sub(u'большой', random.choice(data["adjmsg"]), text2)
    text4 = re.sub(u'лохматый', random.choice(data["adjmsg"]), text3)
    text5 = re.sub(u'гулять по лесу', random.choice(data["action"]), text4)
    text6 = re.sub(u'голодные', random.choice(data["pril"]), text5)
    text7 = re.sub(u'сдвинул', random.choice(data["verb"]), text6)
    text8 = re.sub(u'сломал', random.choice(data["verb"]), text7)
    print("\nВаша сказка готова:")
    return text8


# Проделываем те же операции с шаблоном "Каша из топора", что и спредыдщими
def patternTopor():
    try:
        vvod = int(input(data["welcome"]["3"]))
        if vvod == 1:
            print(Topor(), original(data["topor"]["original"]))
        elif vvod == 2:
            print(AvtoTopor(), original(data["topor"]["original"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        patternTopor()


def Topor():
    word = (input(data["topor"]["questions"]["1"])).decode('utf-8')
    text1 = re.sub(u'[Сс]олдат', word, data["topor"]["original"])
    text11 = re.sub(u'[Сс]луживый', word, text1)
    word2 = (input(data["topor"]["questions"]["2"])).decode('utf-8')
    text2 = re.sub(u'[Сс]таруха', word2, text11)
    text3 = re.sub(u'[хХ]озяйка', word2, text2)
    text4 = re.sub(u'[Хх]озяйкою', (input(data["topor"]["questions"]["2.1"])).decode('utf-8'), text3)
    text5 = re.sub(u'топор', (input(data["topor"]["questions"]["3"])).decode('utf-8'), text4)
    text7 = re.sub(u'кашу', (input(data["topor"]["questions"]["4"])).decode('utf-8'), text5)
    text8 = re.sub(u'каша', (input(data["topor"]["questions"]["4.1"])).decode('utf-8'), text7)
    text9 = re.sub(u'каши', (input(data["topor"]["questions"]["4.2"])).decode('utf-8'), text8)
    print("\nВаша сказка готова:")
    return text9


def AvtoTopor():
    word = random.choice(data["man"])
    text1 = re.sub(u'[Сс]олдат', word, data["topor"]["original"])
    text2 = re.sub(u'[Сс]луживый', word, text1)
    text3 = re.sub(u'[Сс]таруха', random.choice(data["woman"]), text2)
    text4 = re.sub(u'топор', random.choice(data["ingridients"]), text3)
    text5 = re.sub(u'каша', random.choice(data["poridge1"]), text4)
    text6 = re.sub(u'кашу', random.choice(data["poridge2"]), text5)
    text7 = re.sub(u'каши', random.choice(data["poridge3"]), text6)
    print("\nВаша сказка готова:")
    return text7


# Проделываем те же операции с шаблоном "Лиса и козел# ", что и спредыдщими
def patternFoxAndGoat():
    try:
        vvod = int(input(data["welcome"]["3"]))
        if vvod == 1:
            print(FoxandGoat(), original(data["foxandgoat"]["original"]))
        elif vvod == 2:
            print(AvtoFoxandGoat(), original(data["foxandgoat"]["original"]))
    except ValueError:
        print("Ой, что-то пошло не так. Выберите 1 или 2!")
        patternFoxAndGoat()


def FoxandGoat():
    word = (input(data["foxandgoat"]["questions"]["1"])).decode('utf-8')
    text1 = re.sub(u'лиса', word, data["foxandgoat"]["original"])
    text11 = re.sub(u'лисонька', word, text1)
    text2 = re.sub(u'лису', (input(data["foxandgoat"]["questions"]["1.1"])).decode('utf-8'), text11)
    text3 = re.sub(u'лисы', (input(data["foxandgoat"]["questions"]["1.2"])).decode('utf-8'), text2)
    text4 = re.sub(u'коз[ёе]л', (input(data["foxandgoat"]["questions"]["2"])).decode('utf-8'), text3)
    text5 = re.sub(u'козлу', (input(data["foxandgoat"]["questions"]["2.1"])).decode('utf-8'), text4)
    text7 = re.sub(u'[Оо]тличная', (input(data["foxandgoat"]["questions"]["3"])).decode('utf-8'), text5)
    text8 = re.sub(u'[Чч]истая', (input(data["foxandgoat"]["questions"]["4"])).decode('utf-8'), text7)
    text9 = re.sub(u'холодная', (input(data["foxandgoat"]["questions"]["5"])).decode('utf-8'), text8)
    print("\nВаша сказка готова:")
    return text9


def AvtoFoxandGoat():
    word = random.choice(data["woman"])
    word1 = random.choice(data["man"])
    text1 = re.sub(u'лис[ауы]', word, data["foxandgoat"]["original"])
    text2 = re.sub(u'лисонька', word, text1)
    text3 = re.sub(u'коз[ёе]л', word1, text2)
    text4 = re.sub(u'козлу', word1, text3)
    text5 = re.sub(u'[Оо]тличная', random.choice(data["adjwsg"]), text4)
    text6 = re.sub(u'[Чч]истая', random.choice(data["adjwsg"]), text5)
    text7 = re.sub(u'холодная', random.choice(data["adjwsg"]), text6)
    print("\nВаша сказка готова:")
    return text7


# menu()
