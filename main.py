import os

BASE_DIR = os.getcwd()
FOLDER_NAME = 'files'
FILE_NAME = 'recipes.txt'
full_path = os.path.join(BASE_DIR, FOLDER_NAME, FILE_NAME)


from pprint import pprint




# Task 1

# Открытие и преобразование данных файла в список, состоящий из списка блюд
def open_and_conversion_file(path=full_path):
    with open(path, encoding="utf-8") as file:
        content = file.read().split("\n\n")
        list = []
        for dish in content:
            list.append(dish.split("\n"))
        return list

# Преобразование списка блюд в словарь
def composition_dish(structure_dish):
    res = {}
    list = []
    flag = 0
    count = 0
    for dish in structure_dish:
        if flag == 0:
            res[dish]= list
            flag += 1
        elif flag == 1:
            count = int(dish) + 2
            flag += 1
        elif flag < count:
            dish = dish.split(' | ')
            flag += 1
            list.append({'ingredient_name' : dish[0], 'quantity' : dish[1], 'measure' : dish[2]})
            if flag == count:
                return res

# Слияние словарей блюд в один словарь
def merge_dict_dish(converted_file):
    cook_book = {}
    for dish in converted_file:
        cook_book |= composition_dish(dish)
    return cook_book

# cook_book = merge_dict_dish(open_and_conversion_file())
# pprint(cook_book)



# Task 2

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for food in dishes:
        for dish, compound in cook_book.items():
            if dish == food:
                    for ingredients in compound:
                        if ingredients['ingredient_name'] not in shopping_list:
                            portion = int(ingredients['quantity']) * person_count
                            shopping_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'],
                                                                             'quantity': portion
                                                                             }
                        else:
                            portion = (int(ingredients['quantity']) * person_count)
                            # ВОПРОС 1 - Корректный ли здесь перенос строки?
                            ((shopping_list[ingredients['ingredient_name']])['quantity']) = ((shopping_list
                            [ingredients['ingredient_name']])['quantity']) + portion
    return shopping_list

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))





# Task 3

BASE_DIR = os.getcwd()
FOLDER_NAME = 'sorted_files'
full_path = os.path.join(BASE_DIR, FOLDER_NAME)
name_resul_file = 'result_sorted_file.txt'

# Получение списка файлов с кол-вом строк (без сортировки)
def get_files_and_lines(path):
    list_dir = os.listdir(full_path)
    list_files = []
    for number_lines, name_file in enumerate(list_dir):
        path_file = os.path.join(full_path, name_file)
        with open(path_file, encoding='utf-8') as file:
            content = file.readlines()
            list_files.append((name_file, len(content)))
    return list_files
# print(get_files_and_lines())

# Получение сортированного списка файлов по кол-ву строк
def get_sorted_list_files(path=full_path):
    list_files = get_files_and_lines(path)
    sorted_list_files = sorted(list_files, key=lambda x: x[1])
    return sorted_list_files
# print(get_sorted_list_files())

# Запись в файл по возрастанию кол-ва строк
def record_in_new_file(name_file=name_resul_file, path=full_path):
    for name_file, number_lines in get_sorted_list_files(path):
        path_file = os.path.join(path, name_file)
        with open(path_file, encoding='utf-8') as file:
            content = file.read()
        with open(name_resul_file, 'a', encoding='utf-8') as sort_file:
            sort_file.write(f'{name_file}\n{number_lines}\n{content}\n')

# record_in_new_file(name_resul_file, full_path)