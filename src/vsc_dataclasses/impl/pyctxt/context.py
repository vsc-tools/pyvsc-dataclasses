
import vsc_dataclasses.impl as impl
from .rand_state import RandState

class Context(impl.Context):
    """Pure-python stub implementation of context"""

    def mkRandState(self, seed : str) -> RandState:
        return RandState(seed)