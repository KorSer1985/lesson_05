# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json


list_dicts = []
profit = {}
aver_prof = {"average_profit": 0}

with open("data/hw_07.txt", encoding="utf-8") as temp_file:
    temp_average = 0
    num_prof_firm = 0
    for string in temp_file:
        firm_name, form_ownership, gain, costs = string.split()
        print(f"The company's profit was: {firm_name} - {int(gain) - int(costs)}")
        profit[firm_name] = int(gain) - int(costs)
        if int(gain) - int(costs) > 0:
            temp_average = temp_average + profit[firm_name]
            num_prof_firm += 1
    aver_prof["average_profit"] += round(temp_average / num_prof_firm, 2)
    print(f'Average profit of profitable firms: {aver_prof["average_profit"]}')

list_dicts.append(profit)
list_dicts.append(aver_prof)

with open("data/hw_06.json", "w", encoding="utf-8") as write_json:
    json.dump(list_dicts, write_json)
