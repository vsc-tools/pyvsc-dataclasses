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

import typeworks
from .ctor import Ctor
from .constraint_decl import ConstraintDecl

class ConstraintDecoratorImpl(typeworks.RegistrationDecoratorBase):
    """Constraint decorator implementation"""
    
    def __init__(self, kwargs):
        pass
    
    def __call__(self, T):
        decl = ConstraintDecl(T.__name__, T)
        typeworks.DeclRgy.push_decl(ConstraintDecoratorImpl, decl)

        return T
        