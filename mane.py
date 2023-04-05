def mane_function(data_dict, file_name):
    with open(file_name, 'w') as f:
        for key, value in data_dict.items():
            f.write(f"{key}: {value}\n")
        shoping_list = {'Помідорів': 4, 'Огірків': 3, 'Листя салату': 1}