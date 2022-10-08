

from .field_scalar_impl import FieldScalarImpl
from .modelinfo import ModelInfo
from .typeinfo_vsc import TypeInfoVsc


class TypeInfoScalar(TypeInfoVsc):

    def __init__(self, is_signed):
        super().__init__(None, None)
        self.is_signed = is_signed

    def createInst(
            self,
            modelinfo_p : ModelInfo,
           name, 
           idx):
        field = FieldScalarImpl(name, self, idx)

        # Get the appropriate type/inst object
        field._modelinfo.libobj = modelinfo_p.libobj.getField(idx)

        modelinfo_p.addSubfield(field._modelinfo)
        return field
