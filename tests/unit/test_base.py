
from unittest import TestCase
from vsc_dataclasses.impl.pyctxt.context import Context
from vsc_dataclasses.impl.ctor import Ctor

class TestBase(TestCase):

    def setUp(self) -> None:
        print("setUp")
        Ctor.init(Context())
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

