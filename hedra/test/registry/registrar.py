from types import FunctionType
from typing import Any, Dict, List, Union, Coroutine
from hedra.test.hooks.hook import Hook, Metadata
from hedra.test.hooks.types import HookType


class Registrar:
    all = {}

    def __init__(self, hook_type) -> None:

        self.hook_type = hook_type

    def __call__(self, _: FunctionType) -> Any:
        return self.add_hook(self.hook_type)


    def add_hook(self, hook_type: str):
        if hook_type == HookType.SETUP or hook_type == HookType.TEARDOWN:

            def wrap_hook(metadata: Dict[str, Union[str, int]]={}):
                def wrapped_method(func):

                    hook_name = func.__name__

                    self.all[hook_name] = Hook(
                        hook_name, 
                        func, 
                        hook_type=hook_type,
                        metadata=Metadata(
                            **metadata
                        )
                    )

                    return func
                
                return wrapped_method

        elif hook_type in [HookType.BEFORE, HookType.AFTER, HookType.BEFORE_BATCH, HookType.AFTER_BATCH]:
            
            def wrap_hook(*names):
                def wrapped_method(func):

                    hook_name = func.__name__

                    self.all[hook_name] = Hook(
                        hook_name, 
                        func, 
                        hook_type=hook_type,
                        names=names
                    )

                    return func
                
                return wrapped_method

        else:

            def wrap_hook(weight: int=1, order: int=1, metadata: Dict[str, Union[str, int]]={}, checks: List[Coroutine]=[]):
                def wrapped_method(func):

                    hook_name = func.__name__
                    
                    self.all[hook_name] = Hook(
                        hook_name, 
                        func, 
                        hook_type=hook_type,
                        metadata=Metadata(
                            weight=weight,
                            order=order,
                            **metadata
                        ),
                        checks=checks
                    )

                    return func

                return wrapped_method

        return wrap_hook
        

def makeRegistrar():

    return Registrar


registar = makeRegistrar()