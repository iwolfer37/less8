#Створюємо наш словник та сам файл:
def mane_function(data_dict, file_name):
#відкриваємо файл в режимі запису:
    with open(file_name, 'w') as f:
        for key, value in data_dict.items():
#записуємо словник й все в новому рядку:
            f.write(f"{key}: {value}\n")
        shoping_list = {'Помідорів': 4, 'Огірків': 3, 'Листя салату': 1}
create_file(shoping_list, 'shoping_list.txt')


#Наша нова функція тест
def test_function(file_name)
    data_dict = {}
        with open(file_name, 'r') as f:
            for line in f:
