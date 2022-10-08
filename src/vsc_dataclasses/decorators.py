'''
Created on Feb 26, 2022

@author: mballance
'''

from .impl.constraint_decorator_impl import ConstraintDecoratorImpl
from .impl.randobj_decorator_impl import RandObjDecoratorImpl
from .impl.randclass_decorator_impl import RandClassDecoratorImpl
from .impl.covergroup_decorator_impl import CovergroupDecoratorImpl


def constraint(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return ConstraintDecoratorImpl({})(args[0])
    else:
        return ConstraintDecoratorImpl(kwargs)
    
def covergroup(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return CovergroupDecoratorImpl({})(args[0])
    else:
        return CovergroupDecoratorImpl(kwargs)

def randclass(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return RandClassDecoratorImpl([], {})(args[0])
    else:
        return RandClassDecoratorImpl(args, kwargs)
    
def randobj(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # No-argument form
        return RandObjDecoratorImpl({})(args[0])
    else:
        return RandObjDecoratorImpl(kwargs)
    
    