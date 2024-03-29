#****************************************************************************
#* __main__.py
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
import argparse
import os
import vsc_dataclasses as vdc
from vsc_dataclasses.impl.ctor import Ctor
from vsc_dataclasses.impl.pyctxt.context import Context
from vsc_dataclasses.impl.generators.vsc_data_model_cpp_gen import VscDataModelCppGen
from ..extract_cpp_embedded_dsl import ExtractCppEmbeddedDSL

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--outdir", default="vscdefs",
        help="Specifies the output directory")
    parser.add_argument("-d", "--depfile",
        help="Specifies a dependency file")
    parser.add_argument("files", nargs='+')

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    deps_ts = None
    if args.depfile is not None and os.path.isfile(args.depfile):
        deps_ts = os.path.getmtime(args.depfile)

    fragment_m = {}
    for file in args.files:
        print("Process %s" % file)
        if deps_ts is not None:
            file_ts = os.path.getmtime(file)
            if file_ts <= deps_ts:
                print("Skip due to deps")
                continue

        fragments = ExtractCppEmbeddedDSL(file).extract()
        print("fragments: %s" % str(fragments))

        for f in fragments:
            if f.name in fragment_m.keys():
                raise Exception("Duplicate fragment-name %s" % f.name)
            fragment_m[f.name] = f

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir, exist_ok=True)

    for fn in fragment_m.keys():
        Ctor.init(Context())

        try:
            exec_globals = globals().copy()
            exec(
                fragment_m[fn].content,
                exec_globals)
        except Exception as e:
            print("Error while processing %s" % fn)
            raise e

        header_path = os.path.join(args.outdir, "%s.h" % fn)
        root_t = Ctor.inst().ctxt().findDataTypeStruct(fragment_m[fn].root_types[0])
        gen = VscDataModelCppGen()
        gen._ctxt = "m_ctxt"
        with open(header_path, "w") as fp:
            fp.write(gen.generate(root_t))

        pass

    if args.depfile is not None:
        with open(args.depfile, "w") as fp:
            fp.write("\n")

if __name__ == "__main__":
    main()
