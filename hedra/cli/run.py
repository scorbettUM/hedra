import asyncio
import click
import inspect
import sys
import importlib
import ntpath
from pathlib import Path
from hedra.core.pipelines.stages.stage import Stage

from hedra.core.pipelines import Pipeline


@click.command("Run a specified test file.")
@click.argument('path')
def run(path: str):
    package_dir = Path(path).resolve().parent
    package_dir_path = str(package_dir)
    package_dir_module = package_dir_path.split('/')[-1]
    
    package = ntpath.basename(path)
    package_slug = package.split('.')[0]
    spec = importlib.util.spec_from_file_location(f'{package_dir_module}.{package_slug}', path)

    if path not in sys.path:
        sys.path.append(str(package_dir.parent))

    module = importlib.util.module_from_spec(spec)
    sys.modules[module.__name__] = module

    spec.loader.exec_module(module)
    
    direct_decendants = list({cls.__name__: cls for cls in Stage.__subclasses__()}.values())

    discovered = {}
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, Stage) and obj not in direct_decendants:
            discovered[name] = obj

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    pipeline = Pipeline(
        list(discovered.values())
    )

    pipeline.validate()
    
    loop.run_until_complete(pipeline.run())

    