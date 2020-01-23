import logging

log = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


class Plug(object):
    """
    A Plug is something that can be connected to/from

    A Plug is a container for a node and one of its parameter
    """
    __slots__ = ('_node', '_param')

    def __init__(self):
        self._node = None
        self._param = None

    @property
    def node(self):
        return self._node

    def setNodeParam(self, node, param):
        """
        A Connection object will be calling this method
        """
        self._node = node
        self._param = param

    def __repr__(self):
        return "<{0}({1}, {2}>".format(self.__class__.__name__,
                                    self._node,
                                    self._param)


class InputPlug(Plug):
    """
    A Plug that is connected from an OutputPlug
    """
    def setValue(self, value):
        """
        When the connection that this plug belongs to get's executed
        the value of the node's parameter that this plug contains is updated
        """
        attr = getattr(self._node, self._param)
        attr.setValue(value)


class OutputPlug(Plug):
    """
    A Plug that connects to another node's Input Plug
    """
    def getValue(self):
        """
        This method is called by the connection that this plug belongs to
        get's executed
        """
        self._node.execute()
        return self._node.output.getValue()

