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
# Created on Jul 4, 2022
#
# @author: mballance
#****************************************************************************

from .typeinfo_vsc import TypeInfoVsc

class TypeInfoEnum(TypeInfoVsc):
    
    def __init__(self, info, kind, e_info):
        super().__init__(kind, lib_typeobj)
        self._e_info = e_info
        
    @property
    def e_info(self):
        return self._e_info

    @e_info.setter
    def e_info(self, val):
        self._e_info = val
    
    @staticmethod
    def get(info):
        if not hasattr(info, TypeInfoVsc.ATTR_NAME):
            setattr(info, TypeInfoVsc.ATTR_NAME, TypeInfoEnum(info))
        return getattr(info, TypeInfoVsc.ATTR_NAME)