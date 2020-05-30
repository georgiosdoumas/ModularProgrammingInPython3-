def new(name, num_servings):
    return {'name' : name, 'num_servings' : num_servings,
            'instructions' : [], 'ingredients' : [] }

def set_name(recipe, name):
    recipe['name'] = name

def get_name(recipe):
    return recipe['name']

def set_num_servings(recipe, num_servings):
    recipe['num_servings'] = num_servings

def get_num_servings(recipe):
    return recipe['num_servings']

def set_ingredients(recipe, ingredients):
    recipe['ingredients'] = ingredients

def get_ingredients(recipe):
    return recipe['ingredients']

def set_instructions(recipe, instructions):
    recipe['instructions'] = instructions

def get_instructions(recipe):
    return recipe['instructions']

def add_instruction(recipe, instruction):
    recipe['instructions'].append(instruction)

def add_ingredient(recipe, ingredient, amount, units):
    recipe['ingredients'].append({'ingredient': ingredient, 'amount': amount, 'units': units})

def to_string(recipe, num_servings):
    multiplier = num_servings / recipe['num_servings']
    s = []
    s.append("\nRecipe for {}, {} servings:".format(recipe['name'], num_servings))
    s.append("---")
    s.append("Ingredients:")
    s.append("....")
    for ingredient in recipe['ingredients']:
        s.append("    {} - {} {}".format(ingredient['ingredient'], ingredient['amount']*multiplier, ingredient['units']))
    s.append("****")
    s.append("Instructions:")
    s.append("")
    for i,instruction in enumerate(recipe['instructions']):
        s.append("{}. {}".format(i+1, instruction))
    return s
