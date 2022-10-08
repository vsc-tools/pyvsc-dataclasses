
import vsc_dataclasses.impl.context as ctxt_api

class DataTypeInt(ctxt_api.DataType):

    def __init__(self, is_signed : bool, width : int):
        self._is_signed = is_signed
        self._width = width

    def mkRootField(self,
        ctxt : 'ModelBuildContext',
        name : str,
        is_ref : bool) -> 'ModelField':
        raise NotImplementedError("mkRootField")

    def mkTypeField(self,
        ctxt : 'ModelBuildContext',
        type : 'TypeField') -> 'ModelField':
        raise NotImplementedError("mkTypeField")

    pass