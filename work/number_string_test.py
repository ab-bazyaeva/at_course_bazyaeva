a = int(1.2)
b = int(1.5)
c = int(1.7)
print(a, b, c)

a = round(1.2)
b = round(2.5)
c = round(1.7)
print(a, b, c)

string1 = 'Нельзя так просто взять и начать писать автотесты'
string2 = "Нельзя так просто взять и начать писать автотесты"
print(string1, string2)

# многосрочный текст
string3 = """
Нельзя так просто взять и начать писать автотесты
Как тебе сначало могло показаться
Для этого нужно будет снова многое изучить 
"""
print(string3)

# длинная строка
string4 = ('Нельзя так просто взять и начать писать автотесты'
'Нельзя так просто взять и начать писать автотесты'
'Нельзя так просто взять и начать писать автотесты')
print(string4)

# ковычки для названий
string5 = 'Нельзя так просто взять и начать писать "автотесты"\n'
print(string5)

# экранирование
string6 = 'Казнить нельзя \nпомиловать'
print(string6)

# сырая строка
string7 = r'C:\python\name.txt'
print(string7)

# КОНКАТЕНАЦИЯ
print(string7 + string5)

# умножение строки
print(string5 * 3)

# индексация
print(string7[0], string7[-1])

# срез
print(string6[:7])

# Пример из АТ
our_org = '123456789'
print(our_org[-5:])

# пример с конкатенацией
print('Можно' + string5[6:])

# длина строки
print(len(string1))

# преобразование в строку
c = str(4)
print(c, type(c))

# преобразование в целое число
d = int('4')
print(d, type(d))

# replace
print(string5.replace('Нельзя', 'Можно'))

# форматирование строк
our_org2 = 'АГРОВОД'
addressee = 'НПО "Физика", ОАО'
nom_name = 'Товар_автотест_реализация'

result = f"""
Создать документ Реализация. Выбрать организацию %s, покупателя %s.
Добавить номенклартуру %s
""" % (our_org2, addressee, nom_name)

print(result)

# форматирование строк 2
our_org2 = 'АГРОВОД'
addressee = 'НПО "Физика", ОАО'
nom_name = 'Товар_автотест_реализация'

result = """
Создать документ Реализация. Выбрать организацию {}, покупателя {}.
Добавить номенклартуру {}
""".format(our_org2, addressee, nom_name)

print(result)