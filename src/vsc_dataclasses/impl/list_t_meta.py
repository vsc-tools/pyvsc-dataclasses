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
# Created on Jun 28, 2022
#
# @author: mballance
#****************************************************************************


class ListTMeta(type):
    
    def __init__(self, name, bases, dct):
        self.type_m = {}
        
    def __getitem__(self, item):
        from .list_t import ListT
        from .list_tt_meta import ListTTMeta

        if item in self.type_m.keys():
            return self.type_m[item]
        else:
            t = ListTTMeta("list_t[%s]" % str(item), (ListT,), 
                dict(T=item, DIM=[]))
            t.T = item
            self.type_m[item] = t
            return t
        
    