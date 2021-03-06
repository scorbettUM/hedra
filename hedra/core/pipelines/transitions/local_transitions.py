from hedra.core.pipelines.stages.types.stage_types import StageTypes
from .common import (
    idle_transition,
    invalid_transition,
    exit_transition
)

from .validate import (
    validate_to_optimize_transition,
    validate_to_execute_transition
)

from .idle import (
    invalid_idle_transition,
    idle_to_setup_transition,
)

from .setup import (
    setup_to_validate_transition,
    setup_to_optimize_transition,
    setup_to_execute_transition,
    setup_to_checkpoint_transition,
)

from .optimize import (
    optimize_to_execute_transition,
    optimize_to_checkpoint_transition,
)

from .execute import (
    execute_to_setup_transition,
    execute_to_execute_transition,
    execute_to_optimize_transition,
    execute_to_teardown_transition,
    execute_to_analyze_transition,
    execute_to_checkpoint_transition,
)

from .teardown import (
    teardown_to_analyze_transition,
    teardown_to_checkpoint_transition
)

from .analyze import (
    analyze_to_checkpoint_transition,
    analyze_to_submit_transition
)

from .checkpoint import (
    checkpoint_to_setup_transition,
    checkpoint_to_optimize_transition,
    checkpoint_to_execute_transition,
    checkpoint_to_teardown_transition,
    checkpoint_to_analyze_transition,
    checkpoint_to_complete_transition,
    checkpoint_to_submit_transition
)

from .submit import (
    submit_to_setup_transition,
    submit_to_optimize_transition,
    submit_to_execute_transition,
    submit_to_checkpoint_transition,
    submit_to_complete_transition
)


local_transitions = {

        # State: Idle
        (StageTypes.IDLE, StageTypes.IDLE): idle_transition,
        (StageTypes.IDLE, StageTypes.SETUP): idle_to_setup_transition,
        (StageTypes.IDLE, StageTypes.VALIDATE): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.OPTIMIZE): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.EXECUTE):  invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.TEARDOWN): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.ANALYZE): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.CHECKPOINT): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.SUBMIT): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.COMPLETE): invalid_idle_transition,
        (StageTypes.IDLE, StageTypes.ERROR): invalid_idle_transition,

        # State: Setup
        (StageTypes.SETUP, StageTypes.SETUP): invalid_transition,
        (StageTypes.SETUP, StageTypes.IDLE): invalid_transition,
        (StageTypes.SETUP, StageTypes.VALIDATE): setup_to_validate_transition,
        (StageTypes.SETUP, StageTypes.OPTIMIZE): setup_to_optimize_transition,
        (StageTypes.SETUP, StageTypes.EXECUTE): setup_to_execute_transition,
        (StageTypes.SETUP, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.SETUP, StageTypes.ANALYZE): invalid_transition,
        (StageTypes.SETUP, StageTypes.CHECKPOINT): setup_to_checkpoint_transition,
        (StageTypes.SETUP, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.SETUP, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.SETUP, StageTypes.ERROR): invalid_transition,

        # State: Validate
        (StageTypes.VALIDATE, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.IDLE): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.SETUP): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.OPTIMIZE): validate_to_optimize_transition,
        (StageTypes.VALIDATE, StageTypes.EXECUTE): validate_to_execute_transition,
        (StageTypes.VALIDATE, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.ANALYZE): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.CHECKPOINT): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.VALIDATE, StageTypes.ERROR): invalid_transition,

        # State: Optimize
        (StageTypes.OPTIMIZE, StageTypes.OPTIMIZE): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.IDLE): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.SETUP): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.EXECUTE): optimize_to_execute_transition,
        (StageTypes.OPTIMIZE, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.ANALYZE): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.CHECKPOINT): optimize_to_checkpoint_transition,
        (StageTypes.OPTIMIZE, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.OPTIMIZE, StageTypes.ERROR): invalid_transition,

        # State: Execute
        (StageTypes.EXECUTE, StageTypes.EXECUTE): execute_to_execute_transition,
        (StageTypes.EXECUTE, StageTypes.IDLE): invalid_transition,
        (StageTypes.EXECUTE, StageTypes.SETUP): execute_to_setup_transition,
        (StageTypes.EXECUTE, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.EXECUTE, StageTypes.OPTIMIZE): execute_to_optimize_transition,
        (StageTypes.EXECUTE, StageTypes.TEARDOWN): execute_to_teardown_transition,
        (StageTypes.EXECUTE, StageTypes.ANALYZE): execute_to_analyze_transition,
        (StageTypes.EXECUTE, StageTypes.CHECKPOINT): execute_to_checkpoint_transition,
        (StageTypes.EXECUTE, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.EXECUTE, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.EXECUTE, StageTypes.ERROR): invalid_transition,

        # State: Teardown
        (StageTypes.TEARDOWN, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.IDLE): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.SETUP): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.OPTIMIZE): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.EXECUTE): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.ANALYZE): teardown_to_analyze_transition,
        (StageTypes.TEARDOWN, StageTypes.CHECKPOINT): teardown_to_checkpoint_transition,
        (StageTypes.TEARDOWN, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.TEARDOWN, StageTypes.ERROR): invalid_transition,

        # State: Analyze
        (StageTypes.ANALYZE, StageTypes.ANALYZE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.IDLE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.SETUP): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.OPTIMIZE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.EXECUTE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.CHECKPOINT): analyze_to_checkpoint_transition,
        (StageTypes.ANALYZE, StageTypes.SUBMIT): analyze_to_submit_transition,
        (StageTypes.ANALYZE, StageTypes.COMPLETE): invalid_transition,
        (StageTypes.ANALYZE, StageTypes.ERROR): invalid_transition,

        # State: Checkpoint
        (StageTypes.CHECKPOINT, StageTypes.CHECKPOINT): invalid_transition,
        (StageTypes.CHECKPOINT, StageTypes.IDLE): invalid_transition,
        (StageTypes.CHECKPOINT, StageTypes.SETUP): checkpoint_to_setup_transition,
        (StageTypes.CHECKPOINT, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.CHECKPOINT, StageTypes.OPTIMIZE): checkpoint_to_optimize_transition,
        (StageTypes.CHECKPOINT, StageTypes.EXECUTE): checkpoint_to_execute_transition,
        (StageTypes.CHECKPOINT, StageTypes.TEARDOWN): checkpoint_to_teardown_transition,
        (StageTypes.CHECKPOINT, StageTypes.ANALYZE): checkpoint_to_analyze_transition,
        (StageTypes.CHECKPOINT, StageTypes.SUBMIT): checkpoint_to_submit_transition,
        (StageTypes.CHECKPOINT, StageTypes.COMPLETE): checkpoint_to_complete_transition,
        (StageTypes.CHECKPOINT, StageTypes.ERROR): invalid_transition,


        # State: Submit
        (StageTypes.SUBMIT, StageTypes.SUBMIT): invalid_transition,
        (StageTypes.SUBMIT, StageTypes.IDLE): invalid_transition,
        (StageTypes.SUBMIT, StageTypes.SETUP): submit_to_setup_transition,
        (StageTypes.SUBMIT, StageTypes.VALIDATE): invalid_transition,
        (StageTypes.SUBMIT, StageTypes.OPTIMIZE): submit_to_optimize_transition,
        (StageTypes.SUBMIT, StageTypes.EXECUTE): submit_to_execute_transition,
        (StageTypes.SUBMIT, StageTypes.TEARDOWN): invalid_transition,
        (StageTypes.SUBMIT, StageTypes.ANALYZE): invalid_transition,
        (StageTypes.SUBMIT, StageTypes.CHECKPOINT): submit_to_checkpoint_transition,
        (StageTypes.SUBMIT, StageTypes.COMPLETE): submit_to_complete_transition,
        (StageTypes.SUBMIT, StageTypes.ERROR): invalid_transition,

        # State: Complete
        (StageTypes.COMPLETE, StageTypes.COMPLETE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.IDLE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.SETUP): exit_transition,
        (StageTypes.COMPLETE, StageTypes.VALIDATE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.OPTIMIZE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.EXECUTE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.TEARDOWN): exit_transition,
        (StageTypes.COMPLETE, StageTypes.ANALYZE): exit_transition,
        (StageTypes.COMPLETE, StageTypes.CHECKPOINT): exit_transition,
        (StageTypes.COMPLETE, StageTypes.SUBMIT): exit_transition,
        (StageTypes.COMPLETE, StageTypes.ERROR): exit_transition,

        # State: Error
        (StageTypes.ERROR, StageTypes.ERROR): exit_transition,
        (StageTypes.ERROR, StageTypes.IDLE): exit_transition,
        (StageTypes.ERROR, StageTypes.SETUP): exit_transition,
        (StageTypes.ERROR, StageTypes.VALIDATE): exit_transition,
        (StageTypes.ERROR, StageTypes.OPTIMIZE): exit_transition,
        (StageTypes.ERROR, StageTypes.EXECUTE): exit_transition,
        (StageTypes.ERROR, StageTypes.TEARDOWN): exit_transition,
        (StageTypes.ERROR, StageTypes.ANALYZE): exit_transition,
        (StageTypes.ERROR, StageTypes.CHECKPOINT): exit_transition,
        (StageTypes.ERROR, StageTypes.SUBMIT): exit_transition,
        (StageTypes.ERROR, StageTypes.COMPLETE): exit_transition
    }