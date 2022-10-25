def get_recipe(path, search_id):
    with open(path, "r") as fh:
        recipe = [line.strip().split(",") for line in fh.readlines()]
        for i in recipe:
            dictionary = {"id": i[0], "name": i[1], 'ingredients':i[2:]}
            if i[0] ==search_id:
                return dictionary
            


print(get_recipe("6hw6.txt", "60b90c3b13067a15887e1ae4"))
