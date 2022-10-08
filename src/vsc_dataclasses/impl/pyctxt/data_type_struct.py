
from typing import Callable, List
import vsc_dataclasses.impl.context as ctxt_api

class DataTypeStruct(ctxt_api.DataTypeStruct):

    def __init__(self, name):
        self._name = name
        self._fields = []
        self._constraints = []
        self._create_h = None

    def name(self) -> str:
        return self._name

    def addField(self, f : 'TypeField'):
        self._fields.append(f)

    def getFields(self) -> List['TypeField']:
        return self._fields

    def addConstraint(self, c : 'TypeConstraint'):
        self._constraints.append(c)

    def getConstraints(self) -> List['TypeConstraint']:
        return self._constraints

    def setCreateHook(self, hook : Callable):
        self._create_h = hook

    def mkRootField(self,
        ctxt : 'ModelBuildContext',
        name : str,
        is_ref : bool) -> 'ModelField':
        raise NotImplementedError("mkRootField")

    def mkTypeField(self,
        ctxt : 'ModelBuildContext',
        type : 'TypeField') -> 'ModelField':
        raise NotImplementedError("mkTypeField")