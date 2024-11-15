#****************************************************************************
# Copyright 2019-2024 Matthew Ballance and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# 
# 
# @author: mballance
#****************************************************************************
from .field_base_impl import FieldBaseImpl
from .ctor import Ctor

class FieldListObjectImpl(FieldBaseImpl):

    def __init__(self, name, typeinfo, lib_field):
        super().__init__(name, typeinfo, lib_field)
        self._elems = []
        
    @property
    def size(self):
        ctor = Ctor.inst()
        
        if ctor.expr_mode():
            return 
            if ctor.is_type_mode():
                raise Exception("TODO")
            else:
                pass
            
    def __len__(self):
        ctor = Ctor.inst()
        if ctor.expr_mode():
            raise Exception('len cannot be used in constraints')
        else:
            return self._modelinfo._lib_obj.getSize()
        
    def append(self, v):
        self._elems.append(v)
#        self._modelinfo._lib_obj.push_back()
        print("TODO: append")
    