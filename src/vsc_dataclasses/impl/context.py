#****************************************************************************
#* context.py
#*
#* Declares back-end interface API and associated data types
#****************************************************************************
from enum import IntEnum


class BinOp(IntEnum):
    pass

class UnaryOp(IntEnum):
    pass

class DataTypeStruct(object):
    pass

class ModelFieldFlag(IntEnum):
    pass

class ModelVal(object):
    pass

class TypeFieldAttr(IntEnum):
    pass

class ModelBuildContext(object):
    pass

class RandState(object):

    def seed(self) -> str:
        raise NotImplementedError("seed")

    def randint32(self, low, high):
        raise NotImplementedError("randint32")

    def randbits(self, v : ModelVal):
        raise NotImplementedError("randbits")

    def setState(self, other : 'RandState'):
        raise NotImplementedError("setState")

    def clone(self) -> 'RandState':
        raise NotImplementedError("clone")

    def next(self) -> 'RandState':
        raise NotImplementedError("next")

class SolveFlags(IntEnum):
    pass

class Context(object):

    def findDataTypeStruct(self, name) -> DataTypeStruct:
        raise NotImplementedError("findDataTypeStruct")

    def mkDataTypeStruct(self, name) -> DataTypeStruct:
        raise NotImplementedError("mkDataTypeStruct")

    def addDataTypeStruct(self, t : DataTypeStruct) -> bool:
        raise NotImplementedError("addDataTypeStruct")

    def mkRandState(self, seed : str) -> RandState:
        raise NotImplementedError("mkRandState")

    pass
