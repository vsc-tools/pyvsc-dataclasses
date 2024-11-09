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
# Created on Mar 18, 2022
#
# @author: mballance
#****************************************************************************

class ConstraintDecl(object):
    """Holds information about a specific constraint declaration"""
    
    def __init__(self, name, method_t):
        self._name = name
        self._method_t = method_t
        
    @property
    def name(self):
        return self._name
    
    def __call__(self, obj):
        self._method_t(obj)
        
    pass