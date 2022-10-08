#****************************************************************************
#* context.py
#*
#* Declares back-end interface API and associated data types
#****************************************************************************
from enum import IntEnum, IntFlag
from typing import Callable, List


class BinOp(IntEnum):
    pass

class UnaryOp(IntEnum):
    pass

class CompoundSolver(object):

    def solve(self, rs : 'RandState', fields, constraints, flags):
        raise NotImplementedError("solve")

class DataType(object):
    def mkRootField(self,
        ctxt : 'ModelBuildContext',
        name : str,
        is_ref : bool) -> 'ModelField':
        raise NotImplementedError("mkRootField")

    def mkTypeField(self,
        ctxt : 'ModelBuildContext',
        type : 'TypeField') -> 'ModelField':
        raise NotImplementedError("mkTypeField")

class DataTypeEnum(DataType):
    def name(self) -> str:
        raise NotImplementedError("name")

    def isSigned(self) -> bool:
        raise NotImplementedError("isSigned")

    def addEnumerator(self, name, val : 'ModelVal') -> bool:
        raise NotImplementedError("addEnumerator")

    def getDomain(self) -> 'TypeExprRangelist':
        raise NotImplementedError("getDomain")

class DataTypeInt(DataType):
    pass

class DataTypeStruct(DataType):

    def name(self) -> str:
        raise NotImplementedError("name")

    def addField(self, f : 'TypeField'):
        raise NotImplementedError("addField")

    def getFields(self) -> List['TypeField']:
        raise NotImplementedError("getFields")

    def addConstraint(self, c : 'TypeConstraint'):
        raise NotImplementedError("addConstraint")

    def getConstraints(self) -> List['TypeConstraint']:
        raise NotImplementedError("getConstraints")

    def setCreateHook(self, hook : Callable):
        raise NotImplementedError("setCreateHook")

class ModelFieldFlag(IntEnum):
    pass

class ModelVal(object):
    pass

class TypeFieldAttr(IntEnum):
    pass

class ModelBuildContext(object):

    def ctxt(self) -> 'Context':
        raise NotImplementedError("ctxt")

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

class TypeFieldAttr(IntFlag):
    NoAttr = 0
    Rand = (1 << 0)

#********************************************************************
#* TypeExpr
#********************************************************************

class TypeExpr(object):
    pass

class TypeExprRange(TypeExpr):

    def isSingle(self) -> bool:
        raise NotImplementedError("isSingle")

    def lower(self) -> 'TypeExpr':
        raise NotImplementedError("lower")

    def upper(self) -> 'TypeExpr':
        raise NotImplementedError("upper")

#********************************************************************
#* TypeField
#********************************************************************

class TypeField(object):

    def getParent(self) -> 'TypeField':
        raise NotImplementedError("getParent")

    def setParent(self, p : 'TypeField'):
        raise NotImplementedError("setParent")

    def getIndex(self) -> int:
        raise NotImplementedError("getIndex")

    def setIndex(self, idx : int):
        raise NotImplementedError("setIndex")

    def getDataType(self) -> 'DataType':
        raise NotImplementedError("getDataType")

    def name(self) -> str:
        raise NotImplementedError("name")


class Context(object):

    def findDataTypeStruct(self, name) -> DataTypeStruct:
        raise NotImplementedError("findDataTypeStruct")

    def mkDataTypeStruct(self, name) -> DataTypeStruct:
        raise NotImplementedError("mkDataTypeStruct")

    def addDataTypeStruct(self, t : DataTypeStruct) -> bool:
        raise NotImplementedError("addDataTypeStruct")

    def mkRandState(self, seed : str) -> RandState:
        raise NotImplementedError("mkRandState")

    def mkModelBuildContext(self, ctxt : 'Context') -> ModelBuildContext:
        raise NotImplementedError("mkModelBuildContext")


    pass
