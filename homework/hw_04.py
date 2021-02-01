# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ru = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("data/hw_04.txt", "r", encoding="utf=8") as temp_file:
    for el in temp_file:
        el = el.split(" ", 1)
        new_file.append(ru[el[0]] + ' ' + el[1])
    # print(new_file)

with open("data/new_hw_04.txt", "w", encoding="utf8") as temp_file:
    temp_file.writelines(new_file)
