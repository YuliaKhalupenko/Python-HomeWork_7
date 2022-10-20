import record_tel
import search_num
import ui
import logger

def run():
    temp = ui.choice()
    if temp == 1:
        print ('Внесите в справочник новый контакт')
        entry = record_tel.record() # Запись в справочник
        logger.log_to_file(entry)
        run()
    if temp == 2:
        print ('\n Поиск контакта в справочнике\n' )
        entry = search_num.search() # Поиск в справочнике
        logger.reading_file(entry)
        run()
    if temp == 3:
        print ('\n Вывод на печать всех контактов справочника\n\
              \n=== КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n')
        logger.read_all_file()  
        run()
    if temp == 4:
        print('\n Работа c телефонным справочником окончена. Всего доброго.\n')
        exit