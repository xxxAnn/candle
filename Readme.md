# Parser
## License
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Kyando2/candle/blob/master/LICENSE)
<br>
## Version
[![Version](https://img.shields.io/pypi/v/Kyandle.svg)](https://github.com/Kyando2/candle/)<br>
# Syntax
## Types
There are three types: <br>```dict (key = value, key = value ...), ```<br>```list (value, value, value ...) and ```<br>```native (native classes or objects to the language of the interpreter)```
### Dict
Dicts are written as `<'key' IS 'value' AND 'key' IS 'value' ...>` any key and value must be surrounded by `''`<br>It is to be noted that `IS` and `AND` can be omitted
### List
List are written as `^'value' AND 'value' AND 'value' ...$` any value must be surrounded by `''`<br>It is to be noted that `AND` can be omitted
### Native
Natives are object that are native to the language, they have a type identifier at the beginning<br>An python `int` object for the value 3 would be written as `<'i3'>` in a list. The interpreter may then reconvert it to the type.