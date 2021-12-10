from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe(request, recipe):
    if DATA.get(recipe, None) == None:
        context = {}
    else:
        food = DATA[recipe].copy()
        count = int(request.GET.get('servings', 1))
        for key, value in food.items():
                food[key] = round(value*count, 1)
        context = {'recipe': food}
    return render(request, 'calculator/index.html', context)
