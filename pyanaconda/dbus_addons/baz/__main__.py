import logging
logging.basicConfig(level=logging.DEBUG)

from pyanaconda.dbus_addons.baz.baz import Baz

baz = Baz()
baz.run()
