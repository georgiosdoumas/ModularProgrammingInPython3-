import importlib

module_name = input("Load module: ")
if module_name != "":
    try:
        module = importlib.import_module(module_name)
        module.say_hello()
    except ModuleNotFoundError:
        print("The module you requested cannot be found.Maybe you did a typo?")

