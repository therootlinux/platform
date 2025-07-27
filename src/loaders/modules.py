import os
import importlib.util

def load_modules(app, modules_path='./src/modules'):
    for filename in os.listdir(modules_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  
            module_path = os.path.join(modules_path, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'init'):
                module.init(app)
