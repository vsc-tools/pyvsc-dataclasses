#****************************************************************************
#* data_type_list_fixed_size.py
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
import vsc_dataclasses.impl.context as ctxt_api
from .data_type_list import DataTypeList

class DataTypeListFixedSize(DataTypeList, ctxt_api.DataTypeListFixedSize):

    def __init__(self, elem_t, sz):
        super().__init__(elem_t)
        self._sz = sz

    def getSize(self):
        return self._sz

    def accept(self, v):
        v.visitDataTypeListFixedSize(self)
