import logging

import きゃんどる

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s.%(funcName)s: %(message)s'
    )

これ = {"3": [2, (5, {3: "8"})]}
with open('tests/kyandle_file.kya', 'w') as f:
    f.write(きゃんどる.serialize(これ))

with open('tests/kyandle_file.kya', 'r') as f:
    これ = きゃんどる.parse(f.read())

print(これ)