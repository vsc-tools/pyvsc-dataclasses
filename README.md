# pyvsc-dataclasses
Dataclasses-centric front-end for capturing verification stimulus and coverage

The pyvsc-dataclasses project provides a front-end for capturing variables,
constraints, and coverage constructs. The project defines a back-end interface
to be provided by implementations, but does not provide a full implementation.

pyvsc-dataclasses allows you to capture constraint constructs such as:

```
import vsc_dataclasses as vdc

@vdc.randclass
class MyRandClass(object):
    a : vdc.rand_uint32_t
    b : vdc.rand_uint32_t

    @vdc.constraint
    def ab_c(self):
        self.a < self.b

c = MyRandClass()

c.randomize()

with c.randomize_with():
  c.a != 0

```

The code above declares a random class type MyRandClass, creates an instance, and
invokes the built-in methods 'randomize' and 'randomize_with'. 
