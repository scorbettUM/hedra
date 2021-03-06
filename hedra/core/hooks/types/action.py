import functools
from typing import Coroutine, Dict, List, Union
from .types import HookType
from .hook import Hook
from hedra.core.hooks.registry.registrar import registar


@registar(HookType.ACTION)
def action(weight: int=1, order: int=1, metadata: Dict[str, Union[str, int]]={}, checks: List[Coroutine]=[]):

    def wrapper(func) -> Hook:

        @functools.wraps(func)
        def decorator(*args, **kwargs):

            return func(*args, **kwargs)
                
        return decorator

    return wrapper