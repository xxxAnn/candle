import logging

import Kyandle

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s.%(funcName)s: %(message)s'
    )

with open('tests/test.kya', 'r') as f:
    Kyandle.parse(f.read())