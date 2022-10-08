'''
Created on Feb 27, 2022

@author: mballance
'''
from .ctor import Ctor
from .field_enum_impl import FieldEnumImpl
from .enum_info_mgr import EnumInfoMgr
from .typeinfo_enum import TypeInfoEnum
from .type_kind_e import TypeKindE


class EnumT(object):

    # Holds enum info in the case that a type declaration
    # was created
    EnumInfo = None
    
    def __new__(cls, e_t, i=-1):
        ctor = Ctor.inst()

        print("e_t: %s" % str(e_t))        
        # Need to grab the enum type info
        info = EnumInfoMgr.inst().getInfo(e_t)

        raise Exception("Need different approach to enum")        
#        lib_field = libvsc.Task_ModelBuildField(
#            ctor.ctxt(),
#            info.lib_obj,
#            "")
#        print("lib_field: %s" % str(lib_field))
        
        return FieldEnumImpl(
            "", 
            TypeInfoEnum(TypeKindE.Enum, info.lib_obj, info),
            lib_field)
    pass