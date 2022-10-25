def format_ingredients(items):
    n = len(items)
    string = ""

    if n >= 2:
        for item in items[:-2]:
            string = string + item + ", "
        string = string + items[-2] + " and " + items[-1]
    elif n == 1:
        string = items[0]
    return string


items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar", "vanilla sugar"]
format_ingredients(items)
print(format_ingredients(items))

items = ["2 eggs", "1 liter sugar"]
format_ingredients(items)
print(format_ingredients(items))

items = []
format_ingredients(items)
print(format_ingredients(items))
