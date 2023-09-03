#****************************************************************************
#* test_dsl_extractor.py
#*
#* Copyright 2022 Matthew Ballance and Contributors
#*
#* Licensed under the Apache License, Version 2.0 (the "License"); you may 
#* not use this file except in compliance with the License.  
#* You may obtain a copy of the License at:
#*
#*   http://www.apache.org/licenses/LICENSE-2.0
#*
#* Unless required by applicable law or agreed to in writing, software 
#* distributed under the License is distributed on an "AS IS" BASIS, 
#* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
#* See the License for the specific language governing permissions and 
#* limitations under the License.
#*
#* Created on:
#*     Author: 
#*
#****************************************************************************
import io
from .test_base import TestBase
from vsc_dataclasses.util.extract_cpp_embedded_dsl import ExtractCppEmbeddedDSL

class TestDslExtractor(TestBase):

    def test_smoke(self):
        content="""
        TEST_F(TestSuite, test_name) {
            VSC_DATACLASSES(TestSuite_test_name, (MyC), R"(
            @vdc.randclass
            class MyC(object):
                a : vdc.rand_uint32_t
                b : vdc.rand_uint32_t
            )")
        }
        """
        snippets = ExtractCppEmbeddedDSL(
            io.StringIO(content),
            "my_file").extract()
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].name, "TestSuite_test_name")
        self.assertEqual(len(snippets[0].root_types), 1)

    def test_multi_root(self):
        content="""
        TEST_F(TestSuite, test_name) {
            VSC_DATACLASSES(TestSuite_test_name, (MyC, MyC2), R"(
            @vdc.randclass
            class MyC(object):
                a : vdc.rand_uint32_t
                b : vdc.rand_uint32_t
            )")
        }
        """
        snippets = ExtractCppEmbeddedDSL(
            io.StringIO(content),
            "my_file").extract()
        self.assertEqual(len(snippets), 1)
        self.assertEqual(snippets[0].name, "TestSuite_test_name")
        self.assertEqual(len(snippets[0].root_types), 2)

