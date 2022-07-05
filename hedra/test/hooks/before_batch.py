import functools
from .types import HookType


def before_batch(*names):
    
    def wrapper(func):
        func.names = names
        func.is_action = True
        func.hook_type = HookType.BEFORE_BATCH

        @functools.wraps(func)
        def decorator(*args, **kwargs):
            return func(*args, **kwargs)

        return decorator

    return wrapper