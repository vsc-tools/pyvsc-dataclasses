'''
Created on Jul 4, 2022

@author: mballance
'''
from .field_base_impl import FieldBaseImpl
from .ctor import Ctor
from .expr import Expr


class FieldListScalarImpl(FieldBaseImpl):
    
    def __init__(self, name, typeinfo, lib_field):
        super().__init__(name, typeinfo, lib_field)
        
    @property
    def size(self):
        ctor = Ctor.inst()
        
        if ctor.expr_mode():
            if ctor.is_type_mode():
                raise Exception("size")
            else:
                ref = ctor.ctxt().mkModelExprFieldRef(self._modelinfo._lib_obj.getSizeRef())
            return Expr(ref)
        else:
            return self._modelinfo._lib_obj.getSize()
    
    def append(self, v):
        pass
    
    def __getitem__(self, it):
        pass
        