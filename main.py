cook_book = {}
with open('Новый текстовый документ.txt', encoding="utf-8") as f:
    for line in f:
        dish_name = line.strip()
        number_of_ing = int(f.readline())
        list_of_ing = []
        for ingrid in range(number_of_ing):
            ing = f.readline().strip().split('|')
            pairs = {'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]}
            list_of_ing.append(pairs)
            cook_book[dish_name] = list_of_ing
        f.readline()

    print(f'{cook_book}\n')

print()
print()
print()


def get_shop_list_by_dishes(dishes, person_count):
    dict_of_ingr_names = {}
    for dish in dishes:
        if dish in cook_book:
            for element in cook_book[dish]:
                names_of_ingr = {}
                if element['ingredient_name'] in dict_of_ingr_names:
                    dict_of_ingr_names[element['quantity']] = int(element['quantity']) * person_count
                    dict_of_ingr_names[element['quantity']].update(dict_of_ingr_names[element['quantity']])
                else:
                    names_of_ingr['quantity'] = int(element['quantity']) * person_count
                    names_of_ingr['measure'] = element['measure']
                    dict_of_ingr_names[element['ingredient_name']] = names_of_ingr

    return dict_of_ingr_names


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))















