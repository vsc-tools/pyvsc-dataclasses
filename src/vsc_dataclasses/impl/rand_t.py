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
# Created on Apr 15, 2022
#
# @author: mballance
#****************************************************************************

class RandT(object):
    
    T = None

    def __new__(cls, *args, **kwargs):
        """
        There are a couple of constructor forms used by rand_t
        - RandT as a type-specialized wrapper
          - T is set to the field type
          - No additional parameters are passed
        - RandT as a type-specialized wrapper with an initial-value parameter (eg rand[int_t[8]](20))
          - T is set to the field type
          - An additional parameter is passed with the initial value
        - RandT called as a wrapper around a type instance (eg rand(bit_t(w, i)))
          - In this case, the type parameter, T, is None
          - The first parameter is the field instance
          - An optional second parameter may be provided with the initial value
        """
        
        print("RandT: T=%s" % str(cls.T))

        if cls.T is not None:        
            ret = cls.T()
        else:
            ret = args[0]
        
        # Propagate the knowledge that this is a rand field
        ret._modelinfo.set_rand()
       
        return ret