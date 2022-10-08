
from .test_base import TestBase
import vsc_dataclasses as vdc

class TestRandClassSmoke(TestBase):

    def test_smoke(self):

        @vdc.randclass
        class MyC(object):
            pass


        pass