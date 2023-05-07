from pprint import pprint

with open('recipe_list.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        amount_of_ingredients = int(file.readline())
        ingredients = []
        for _ in range(amount_of_ingredients):
            ingredient = file.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            ingredients_dict = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredients_dict)
        file.readline()
        cook_book[dish_name] = ingredients
    pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] not in shop_list_by_dishes:
                    volume = {
                        'measure': ingredients['measure'],
                        'quantity': int(ingredients['quantity']) * person_count
                    }
                    shop_list_by_dishes[ingredients['ingredient_name']] = volume
                else:
                    shop_list_by_dishes[ingredients['ingredient_name']]['quantity'] = \
                    shop_list_by_dishes[ingredients['ingredient_name']]['quantity'] + \
                    (int(ingredients['quantity']) * person_count)
        else:
            return f'Одного или всех блюд из списка нет в кулинарной книге'
    return shop_list_by_dishes


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
