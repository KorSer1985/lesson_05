"""
4 урок. Работа с файлами
Дополнительные задания:
1. Мы потеряли все точки в предложении, но можем разрезать по заглавным буквам.
Сделать split() по заглавным бувам.
2. У нас в папке лежат файлы и скрипты вместе. Нужно сделать папку
data и в нее сложить все, кроме .py скриптов

"""

"""
Работа с файлами: открытие, закрытие, чтение, запись
r Открыть файл на чтение (режим по умолчанию)
w Открыть на запись. При этом удалить содержимое файла. Если файла нет, создать новый.
x Открыть файл на запись, если его нет. Если файл есть, он не будет создан.
a Открыть файл на дозапись. Добавить информацию в конец файла.
b Открыть файл в двоичном формате.
t Открыть файл в текстовом формате (режим по умолчанию)
+ Открыть файл на чтение и запись
"""
"""
f = open("for_lesson_5.txt", "a")
data_for_file = ['Milk\n', 'Bread\n', 'Sugar\n', 'Salad']
f.writelines(data_for_file)
f.close()

f = open("for_lesson_5.txt", 'rb')
data = f.read()
print(type(data))
print(data)
f.close()
"""
"""
Менеджеры контекста
"""
"""
try:
    print("Try to open")
    f = open("for_lesson_5.txt")
except:
    print("Fail")
    print("No!")
finally:
    f.close()
    print("Closed!")


with open('for_lesson_5.txt', "a") as f:
    f.writelines(['potato\n', 'egg'])

with open('train.csv', "r") as f:
    data = f.readlines()
print(data[0])
"""
"""
Определение позиции указателя в файле
"""

with open("data/for_lesson_5.txt", "a+") as f:
    print("Init position:", f.tell())
    data = f.read()
    print("Mid position:", f.tell())
    print(data)

    f.write('\File was visited time!')
    data_new = f.read()
    print("I am new!", data_new)
    print("Last position:", f.tell())

"""
json, shutill, os, sys 
"""
"""
import json

worker = {"age": 27, "name": "Basil", "vaccine": 1}
with open("notebook_2.json") as f:
    data = json.load(f)
print(type(data["age"]))
"""
"""
params = {'n_itters': 5, 'path_file': 'home/work', 'k': 4}
--params path_to_file_json
"""
"""
pandas

import pandas as pd

data = pd.read_csv("train.csv")
print(type(data["Survived"][0]))
"""
"""
import os
import shutil

# os.makedirs("Test_1", exist_ok = True)
# os.makedirs("Test_1/Test_2", exist_ok = True)
os.makedirs("data", exist_ok=True)
files = os.listdir()
for file in files:
    print(file)
# shutil.move("for_lesson_5.txt", 'data')

import sys 
sys.argv
"""