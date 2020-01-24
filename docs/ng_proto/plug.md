
# Plug

- A Plug belongs to a Node.
- A Plug holds the value of a parameter.
- A Plug is a point of connection.
- There are three types of plugs
    1. Input Plug
    2. Parameter Plug
    3. Output Plug

## Types of Plugs

### Input Plug

- An ``InputPlug`` plug receives a connection from an ``OutputPlug`` of another ``GraphNode``
- If nothing is connected, then the default value or the value entered by the user is used.
- An ``InputPlug`` is implicitly connected to its sibling ``OutputPlug``

### Parameter Plug

- A ``ParameterPlug`` is a place for the user to enter a value for the parameter
- You cannot connect the ``OutputPlug`` of another ``GraphNode`` to a ``ParamterPlug``
- A ``ParameterPlug`` is implicitly connected to its sibling ``OutputPlug``

### Output Plug  

- An ``OutputPlug`` from one ``GraphNode`` is connected to zero or more ``InputPlug``'s of other ``GraphNodes``
