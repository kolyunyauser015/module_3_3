def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['номер', 23, False]
values_dict = {'a': 1975, 'b': 'номер', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 'пример']
print_params(*values_list_2, 42)
