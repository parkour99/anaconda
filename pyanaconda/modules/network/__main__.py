import logging
logging.basicConfig(level=logging.DEBUG)

from pyanaconda.modules.network.network import NetworkModule

network_module = NetworkModule()
network_module.run()
