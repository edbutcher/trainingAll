def rec_av(recipe, available):
    ava_list = []
    for i in recipe:
        if type(available.get(i)) == int:
            ava_list.append(int((available.get(i)/recipe.get(i))))
        else:
            return '0'
    return (min(ava_list))

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print( rec_av(recipe, available))
