
# my_dict = {'name': '15', '1233': '1'}
my_dict = ['145', '654987', '14']

for key in range(0, len(my_dict)):
    my_dict[key] = '*' * len(my_dict[key])

print(my_dict)