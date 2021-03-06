from typing import Any
from hedra.core.hooks.types.types import HookType
from hedra.core.pipelines.stages.stage import Stage
from hedra.core.pipelines.stages.types.stage_states import StageStates
from hedra.core.pipelines.stages.types.stage_types import StageTypes


async def teardown_to_analyze_transition(current_stage: Stage, next_stage: Stage):

    teardown_hooks = []
    execute_stages = current_stage.context.stages.get(StageTypes.EXECUTE).values()
    paths = current_stage.context.paths

    valid_states = [
        StageStates.EXECUTED
    ]
    
    if current_stage.state == StageStates.INITIALIZED:

        current_stage.state = StageStates.TEARDOWN_INITIALIZED

        for stage in execute_stages:
            in_path = current_stage.name in paths.get(stage.name)

            if stage.state in valid_states and in_path:
                stage.state = StageStates.TEARDOWN_INITIALIZED

                stage_teardown_hooks = stage.hooks.get(HookType.TEARDOWN)
                if stage_teardown_hooks:
                    teardown_hooks.extend(stage_teardown_hooks)

        current_stage.hooks[HookType.ACTION] = teardown_hooks
        await current_stage.run()

        for stage in execute_stages:
            in_path = current_stage.name in paths.get(stage.name)

            if stage.state == StageStates.TEARDOWN_INITIALIZED and in_path:
                stage.state = StageStates.TEARDOWN_COMPLETE

        current_stage.state = StageStates.TEARDOWN_COMPLETE

    next_stage.context = current_stage.context
    return None, StageTypes.ANALYZE


async def teardown_to_checkpoint_transition(current_stage: Stage, next_stage: Stage):
    next_stage.previous_stage = current_stage.name
    next_stage.context = current_stage.context
    
    return None, StageTypes.CHECKPOINT
