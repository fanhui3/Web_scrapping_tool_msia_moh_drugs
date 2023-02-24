import os


def get_ingredient_list():
    INGREDIENTS = []
    lines = open("active_ingredient_list.txt", "r").readlines()
    modified = []
    for line in lines:
        if line[-1] == "\n":
            INGREDIENTS.append(line[:-1])
        else:
            INGREDIENTS.append(line)

    return INGREDIENTS
