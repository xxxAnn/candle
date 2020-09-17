import re
import logging

from ..utils import Parser

parser = Parser()

logger = logging.getLogger(__name__)

def parse(text):
    structs = parser.parse(text)

    logger.info("Got structs {}".format(str(structs)))
