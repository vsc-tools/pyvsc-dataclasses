'''
Created on Jun 23, 2022

@author: mballance
'''
from .impl.sample_meta_t import SampleMetaT

class sample(metaclass=SampleMetaT):
    pass

def coverpoint(expr):
    pass