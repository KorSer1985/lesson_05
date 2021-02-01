# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

hw_list = []
flag = True
while flag:
    string = input("Enter the text: ")
    if string == '':
        print(hw_list)
        flag = False
    else:
        new_line = string + '\n'
        hw_list.append(new_line)

    with open("data/hm_01.txt", "w") as file_temp:
        file_temp.writelines(hw_list)
