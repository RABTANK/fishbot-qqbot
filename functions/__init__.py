import importlib
import os
def load_functions():
    functions={}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for folder in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, folder)) and folder != '__pycache__':
            module = importlib.import_module(f".{folder}", package=__name__)
            functions.update(module.functions)
    return functions

functions = load_functions()