import re
import logging

from ..utils import Parser

parser = Parser()

logger = logging.getLogger(__name__)

def parse(text):
    structs = parser.parse(text)[0]

    logger.debug("Got struct {}".format(str(structs)))
    
    return structs
