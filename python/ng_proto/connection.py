from ng_proto import getLogger
log = getLogger(__name__)

from ng_proto import InputPlug, OutputPlug


class Connection(object):
    """
    A connection between the Output Plug of a node and the
    Input Plug of another node.
    """

    # Cache for plugs that are participating in the connections
    _cache = {
        'output': {

        },
        'input': {

        }
    }

    __slots__ = ('_oplug', '_iplug')

    def __init__(self):
        self._oplug = None
        self._iplug = None

    @property
    def oplug(self):
        return self._oplug

    @property
    def iplug(self):
        return self._iplug

    def create_from_plugs(self, oplug, iplug):
        """

        :param oplug: OutputPlug instance
        :param iplug: InputPlug instance
        :return: None
        """
        self._oplug = oplug
        self._iplug = iplug

    def create_from_nodes(self, upstream_node, downstream_node, downstream_node_param):
        """
        :param upstream_node: Node
        :param downstream_node: Node
        :param downstream_node_param: str
        :return:
        """
        self.setOutputPlug(upstream_node)
        self.setInputPlug(downstream_node, downstream_node_param)
        return self._oplug, self._iplug

    def setOutputPlug(self, node):
        cache_plugs = self._cache['output']
        args = (node, 'output')
        plug = cache_plugs.get(args)

        if not plug:
            log.debug("Connection cache miss {0}".format(args))

            plug = OutputPlug()
            plug.setNodeParam(*args)

            cache_plugs[args] = plug
            log.debug("Added {0} to connection cache".format(plug))

        self._oplug = plug

    def setInputPlug(self, node, param):
        args = (node, param)

        cache_plugs = self._cache['input']
        plug = cache_plugs.get(args)

        if not plug:
            log.debug("Connection cache miss {0}".format(args))

            plug = InputPlug()
            plug.setNodeParam(*args)

            cache_plugs[args] = plug
            log.debug("Added {0} to connection cache".format(plug))

        self._iplug = plug

    def execute(self):
        """
        Evaluates the upstream plug and then set the value of
        the downstream plug.
        """
        value = self._oplug.getValue()
        self._iplug.setValue(value)

    def __repr__(self):
        return "<{0}({1} -> {2})>".format(self.__class__.__name__,
                                         self._oplug,
                                         self._iplug)
