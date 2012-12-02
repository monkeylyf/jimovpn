import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from jimovpn import settings
from django.core.management  import setup_environ
setup_environ(settings)
