import logging

import Kyandle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s.%(funcName)s: %(message)s'
    )

x = {"3": [2, (5, {3: "8"})]}
with open('tests/kyandle_file.kya', 'w') as f:
    f.write(Kyandle.serialize(x))

with open('tests/kyandle_file.kya', 'r') as f:
    x = Kyandle.parse(f.read())

print(x)