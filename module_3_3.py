def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
#print_params(1, 2, 3, 4)  # ошибка "takes from 0 to 3 positional arguments but 4 were given"
print_params(150)          # то же что и print_params(a = 150)
print_params(6, 7)
print_params(8, 9, 5)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [2, 'stroka', True]
values_dict = {'a': 1, 'b': 'slovo', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)