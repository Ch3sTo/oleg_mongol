# Короче, код почему то не работает
# у меня вылезает ошибка TypeError: '>' not supported between instances of 'str' and 'int'
# и всегда ошибка возникает на девятой строчке if number > 0:
# разберись в чем проблема и загрузи исправленный файл в репозиторий, а я пошел спать :), удачи

number = str(input("Укажите число: "))


if number > 0:
    print("Число больше нуля")

elif number < 0:
    print("Число меньше нуля")

elif number == 0:
    print("Число равно нулю")

else:
    print("Ошибка!")