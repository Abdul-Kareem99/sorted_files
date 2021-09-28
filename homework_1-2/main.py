from pprint import pprint


cook_book = {}
with open("recipes.txt", encoding="utf-8") as file:
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())

        temp_list = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split("|")
            temp_list.append({"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()})
        cook_book[dish_name] = temp_list
        file.readline()

# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                temp_ingredients_dict = {}
                temp_ingredients_dict['measure'] = ingredient['measure']
                if ingredient['ingredient_name'] in ingredients_dict:
                    ingredients_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                    temp_ingredients_dict['quantity'] = ingredients_dict[ingredient['ingredient_name']]['quantity']
                else:
                    temp_ingredients_dict['quantity'] = ingredient['quantity'] * person_count
                ingredients_dict[ingredient['ingredient_name']] = temp_ingredients_dict
    pprint(ingredients_dict)
    return


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5)










