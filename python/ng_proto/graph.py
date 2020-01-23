import logging

log = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

from ng_proto import Connection


class NodeFactoryError(ValueError):
    pass


class Graph(object):
    node_factory = {}

    @classmethod
    def register_node(cls, name, node_cls):
        cls.node_factory[name] = node_cls

    def __init__(self):
        self.activeNode = None
        self.nodes = {}
        self.plugs = {}
        self.connections = []

    def add_node(self, node_type, values):
        node_cls = self.node_factory.get(node_type)

        if node_cls is None:
            msg = "Invalid node type: {0}".format(node_type)
            log.debug(msg)
            raise NodeFactoryError(msg)

        node = node_cls(*values)
        self.nodes.setdefault(node, [])
        return node

    def add_connection(self, unode, dnode, param):
        connection = Connection()
        oplug, iplug = connection.create_from_nodes(unode, dnode, param)

        inputs = self.plugs.setdefault(oplug, [])
        inputs.append(iplug)

        to_nodes = self.nodes[oplug.node]
        if not iplug.node in to_nodes:
            to_nodes.append(iplug.node)

        self.connections.append(connection)

        return connection

    def execute_connection(self, connection):
        """

        :param connection: Connection
        :return:
        """
        log.debug("Executing {0}".format(connection))

        connection.execute()

        if self.activeNode == connection.iplug.node:
            self.activeNode.execute()
            log.info(self.activeNode.output.getValue())

        log.debug("Executed {0}\n".format(connection))
