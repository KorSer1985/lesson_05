# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

list_of_employees = {"White": 9999999, "Yermakov": 25000, "Sheremetiev": 27000, "Ali Baba": 5000,
                     "Troshkin": 4000, "Maltsev": 8000}
with open("data/hw_03.txt", "a") as temp_list:
    for surname, wages in list_of_employees.items():
        temp_list.write(surname + ":" + str(wages) + "\n")

total_salary = 0
num_of_employees = 0
starving_people = []
with open("data/hw_03.txt", "r") as temp_list:
    for string in temp_list:
        salary = string.split(":")
        if int(salary[1]) <= 20000:
            starving_people.append(salary[0])
        total_salary += int(salary[1])
        num_of_employees += 1
average_salary = total_salary / num_of_employees

print(f"Last names of beggars: {starving_people}")
print(f'Average income of the "Gentlemen of fortune": {average_salary}')



