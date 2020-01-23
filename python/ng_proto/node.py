import logging

log = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s {0}: %(message)s'.format(__name__))
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


class Number(object):
    def __init__(self, default=0):
        self._value = default

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def __repr__(self):
        return "<{0}({1})>".format(self.__class__.__name__, self._value)


class Node(object):
    """
    A node in the NodeGraph
    """
    def __init__(self):
        self._name = "{0}{1}".format(self.__class__.__name__, self.__class__.instance)
        self.__class__.instance += 1

    @property
    def name(self):
        return self._name


class Add(Node):
    """
    This node adds two numbers
    """
    instance = 0

    _cache = {
    }

    def __init__(self, number1=0, number2=0):
        super(Add, self).__init__()
        self.number1 = Number()
        self.number2 = Number()
        self.output = Number()

        self.number1.setValue(number1)
        self.number2.setValue(number2)

    @classmethod
    def cache(cls, inputs):
        if inputs in cls._cache:
            return cls._cache[inputs]

        log.debug("Cache miss: input {0}".format(inputs))

        return None

    @classmethod
    def function(cls, number1, number2):
        return number1 + number2

    def execute(self):
        number1 = self.number1.getValue()
        number2 = self.number2.getValue()

        result = self.cache((number1, number2))

        if result is None:
            result = self.function(number1, number2)
            self._cache[(number1, number2)] = result

        self.output.setValue(result)

    def __repr__(self):
        return "<{0}({1}, {2}) -> {3}>".format(self.__class__.__name__,
                                    self.number1.getValue(),
                                    self.number2.getValue(),
                                    self.output.getValue())

