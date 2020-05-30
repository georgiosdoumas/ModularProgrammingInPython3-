# The recipe.py file must exist in the same folder
import recipes
pizza_dough = recipes.new("Pizza Dough", num_servings=1)
recipes.add_ingredient(pizza_dough, "Greek Yogurt", 1, "cup")
recipes.add_ingredient(pizza_dough, "Self-Raising Flour", 1.5, "cups")
recipes.add_instruction(pizza_dough, "Combine yogurt and 2/3 of the flour in a bowl and mix with a beater until combined")
recipes.add_instruction(pizza_dough, "Slowly add additional flour until it forms a stiff dough")
recipes.add_instruction(pizza_dough, "Turn out onto a floured surface and knead until dough is tacky")
recipes.add_instruction(pizza_dough, "Roll out into a circle of the desired thickness and place on a greased and lined baking tray")
print(pizza_dough)

for s in recipes.to_string(pizza_dough, num_servings=2):
    print(s)
