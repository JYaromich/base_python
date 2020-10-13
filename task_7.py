import json

json_out = []
try:
    with open('task_7.txt', 'r') as input_file:
        firm_dict, average_profit = {}, {}
        average_profit['average_profit'] = 0
        count_mean = 0
        for line in input_file:
            line_list = line.split()
            profit = int(line_list[2]) - int(line_list[3])
            firm_dict[line_list[0]] = profit
            if profit > 0:
                count_mean += 1
                average_profit['average_profit'] += profit
        average_profit['average_profit'] = average_profit['average_profit'] / count_mean
        json_out.append(firm_dict)
        json_out.append(average_profit)
    with open('task_7.json', 'w') as output:
        json.dump(json_out, output, sort_keys=True, indent=4, ensure_ascii=False)
except IOError:
    print('Ошибка открытия файла')
except ValueError:
    print('Ошибка при обработки значений прибыли и убытка')
