def choice ():
    print('\n Вас приветствует телефонный справочник.\n')
    result = int(input('Выберете операцию, которую необходимо выполнить:\n\
        1 - Внести новый телефон контакта\n\
        2 - Поиск\n\
        3 - Вывести весь список\n\
        4 - Закончить работу\n\
        Ваш выбор: '))
    return result

def style():
    a = int(input('В каком формате предоставить данные: \n\
        1 - Строка;\n\
        2 - Столбец.\n\
        Ваш выбор: '))
    return a