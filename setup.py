
import os
from setuptools import setup, find_namespace_packages

version="0.0.1"

if "BUILD_NUM" in os.environ.keys():
    version += "." + os.environ["BUILD_NUM"]

setup(
  name = "pyvsc-dataclasses",
  version=version,
  packages=find_namespace_packages(where='src'),
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = "Front-end for capturing Verification Stimulus and Coverage constructs using dataclasses",
  long_description="""
  PyVSC-Dataclasses provides a front-end for capturing random variables, constraints, and covergroups 
  in a dataclass-centric manner
  """,
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL"],
  url = "https://github.com/vsc-tools/pyvsc-dataclasses",
  setup_requires=[
    'setuptools_scm',
  ],
  install_requires=[
    'typeworks',
  ],
)

