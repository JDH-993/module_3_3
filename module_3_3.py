def print_params(a = 1, b = 'строка', c = True):
	print(a, b, c)


values_list = []
values_list.append(int(input("введите число ")))
values_list.append(input("введите строку "))
values_list.append(float(input("введите число ")))

values_dict = {}
key1, key2, key3 = "a", "b", "c"
values_dict[key1], values_dict[key2], values_dict[key3] = (
	input("введите значение 1 "), input("введите значение 2 "), input("введите значение 3 "))

values_list_2 = [float(input("введите число ")), input("введите строку ")]

print_params(*values_list_2, 42)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
