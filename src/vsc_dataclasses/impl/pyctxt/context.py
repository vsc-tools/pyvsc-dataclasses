
import vsc_dataclasses.impl as impl
from .data_type_struct import DataTypeStruct
from .model_build_context import ModelBuildContext
from .rand_state import RandState


class Context(impl.Context):
    """Pure-python stub implementation of context"""

    def __init__(self):
        self._dt_struct_m = {}
        self._dt_sint_m = {}
        self._dt_uint_m = {}

    def findDataTypeStruct(self, name) -> DataTypeStruct:
        if name in self._dt_struct_m.keys():
            return self._dt_struct_m[name]
        else:
            return None

    def mkDataTypeStruct(self, name) -> DataTypeStruct:
        return DataTypeStruct(name)

    def addDataTypeStruct(self, t : DataTypeStruct) -> bool:
        if t.name() not in self._dt_struct_m.keys():
            self._dt_struct_m[t.name()] = t
            return True
        else:
            return False

    def mkModelBuildContext(self, ctxt : 'Context') -> ModelBuildContext:
        return ModelBuildContext(ctxt)

    def mkRandState(self, seed : str) -> RandState:
        return RandState(seed)