__version__ = '1.0.0'

import logging

from .parsing import parse
from .serializing import serialize

logger = logging.getLogger(__name__)