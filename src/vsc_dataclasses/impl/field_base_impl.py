'''
Created on May 25, 2022

@author: mballance
'''

from .context import Context

from .ctor import Ctor
from .expr import Expr
from .modelinfo import ModelInfo


class FieldBaseImpl(object):
    
    def __init__(self, name, typeinfo, idx):
        self._modelinfo = ModelInfo(self, name, typeinfo, idx)
        
    def _to_expr(self):
        ctor = Ctor.inst()

        if ctor.is_type_mode():
            print("FieldScalarImpl._to_expr (%s)" % self._modelinfo.name, flush=True)
            ref = ctor.ctxt().mkTypeExprFieldRef()
            mi = self._modelinfo
            while mi._parent is not None:
                print("  IDX: %d" % mi._idx)
                ref.addIdxRef(mi._idx)
                print("MI: %s" % str(mi))
                mi = mi._parent

            print("is_topdown_scope: %d" % mi._is_topdown_scope)
            if mi._is_topdown_scope:            
                ref.addRootRef()
            else:
                ref.addActiveScopeRef(-1)
        else:        
            print("FieldScalarImpl._to_expr (%s)" % self.model().name(), flush=True)
            ref = ctor.ctxt().mkModelExprFieldRef(self.model())
        
        return Expr(ref)
    
