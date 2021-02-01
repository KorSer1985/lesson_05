# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

hw_list = ["У папа была собака\n", "Он её любил\n", "Она съела кусок мяса\n"]
with open("data/hw_02.txt", "a") as temp_file:
    temp_file.writelines(hw_list)

with open("data/hw_02.txt") as temp_file:
    strings = 0
    words = 0
    for string in temp_file:
        strings += string.count("\n")
        words = len(string.split())
        print(f"Words per line: {words}")
    print(f"Number of rows: {strings}")

