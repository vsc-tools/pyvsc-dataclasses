
# Facade, Type, and Model Objects
Several classes of objects (all represented by Python classes) exist
across the lifecycle of a VSC-DM description.

Facade objects are the user-defined classes that declare fields,
constraints, and hook methods. Instances of these objects 
exist at runtime to allow user-facing code to interact with the
data model.

Type objects

# Registration, Type Definition, and Elaboration

# TypeInfo Objects
Each type-like object that can be constructed has an associated
`TypeInfo` object. For example, a TypeInfoRandClass object is
the result of decorating a Python class with `@randclass`.

Objects that are not constructed, such as constraints, do not
have a corresponding TypeInfo object.

The TypeInfo object serves several purposes:
- Manages the process of elaborating key type information about a class
- Implements the constructor functionality for creating the 
