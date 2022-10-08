
from .test_base import TestBase
import vsc_dataclasses as vdc

class TestRandClassSmoke(TestBase):

    def test_smoke(self):

        @vdc.randclass
        class MyC(object):
            pass

        ctor = vdc.impl.Ctor.inst()

        # Check that we can find the registered type
        self.assertIsNotNone(ctor.ctxt().findDataTypeStruct(MyC.__qualname__))

        c = MyC()
