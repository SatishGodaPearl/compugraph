import logging

def getLogger(module_name):
    log = logging.getLogger(module_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s {0}: %(message)s'.format(module_name))
    handler.setFormatter(formatter)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    return log

