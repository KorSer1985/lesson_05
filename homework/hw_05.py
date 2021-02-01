# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import numpy
import re

with open("data/hw_05.txt", "w", encoding="utf-8") as temp_file:
    temp_file.writelines(str(numpy.random.randint(-99, 99, 999)))


temp = open('data/hw_05.txt').read()
total = sum(map(int, re.findall(r'\d+', temp)))
print(f"The sum of the numbers in the file = {total}")