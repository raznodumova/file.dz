cook_book = {}
ingredients = []
ingr_dict = {}


with open ("Cook_book.txt", encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        count = int(f.readline())
        for ingr_line in range(count):
            ingr_name, quan, meas = f.readline().strip().split('|')
            ingredients.append({'product': ingr_name, 'quantity': quan, 'measure': meas})
            recipe = {dish : ingredients}
        blank_line = f.readline()
        cook_book.update(recipe)
    print(f'cook_book = {cook_book}')
