from datetime import datetime
import ui

def log_to_file(entry):  # Запись в файл
    
    with open('phonebook_hor.csv', 'a') as file:
        file.write(
            f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]};\n')

    with open('phonebook_ver.csv', 'a') as file:
        file.write(
            f'{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n{entry[4]}\n\n')    

def reading_file(param): # Чтение из файла
    b = ui.style()
    if b == 1:
        with open('phonebook_hor.csv', 'r') as file:
            for line in file:
                if param in line:
                    print(line)
    if b == 2:
        list = []
        with open('phonebook_hor.csv', 'r') as file:
            for line in file:
                if param in line:
                    list = line.split(";")
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}\n\n')                       

def read_all_file(): # Чтение всего справочника
    b = ui.style()
    if b == 1:
        with open('phonebook_hor.csv', 'r') as file:
            for line in file:
                print(line)    
    if b == 2:
        with open('phonebook_ver.csv', 'r') as file:
            for line in file:
                print(line)       