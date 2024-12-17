def print_params(a=1, b='строка', c=True):
    print(f'a={a}, b={b}, c={c}')
# Вызов без аргументов
print_params()

# Передача одного аргумента
print_params(b=25)

# Передача нескольких аргументов
print_params(c=[1,2,3], a=10)

values_list = [100, 'другая строка', False]
values_dict = {'a': 200, 'b': 'третья строка', 'c': None}

# Распаковываем значения из списка и словаря
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

# Распакуем список и добавим еще одно значение
print_params(*values_list_2, 42)