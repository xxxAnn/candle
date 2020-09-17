import re
import logging

from .errors import InvalidKyandle

line_finder = re.compile(r"(\<|\|)(.*)(\>|\|)")
nest_finder = re.compile(r"((\<|\|)[^\|]+(\>|\|))")
values_finder = re.compile(r"(\'.*?\')")

logger = logging.getLogger(__name__)

class Parser:

    def parse(self, text):
        structs = line_finder.findall(
            text
            )

        structs = self.__fix(structs)

        if len(structs) > 0:
            if self.__has_extras(text, structs):
                return self.__create_natives(structs)

        raise InvalidKyandle

    def __has_extras(self, text, structs):

        for struct in structs:
            logger.info(struct[0]+struct[1])
            text = text.replace(struct[1], "")

        text = text.replace("<", "").replace(">", "").replace("|", "").replace("\n", "").replace("\r", "").replace("\s", "")

        if len(text) > 0:
            return False
        return True

    def __fix(self, structs):
        new_structs = []
        for struct in structs:
            if struct[0] != "<" or struct[2] != ">":
                if struct[0] != "|" or struct[2] != "|":
                    continue

            if struct[0] == "|":
                new_structs.append(("LIST", struct[1]))
            elif struct[0] == "<":
                new_structs.append(("DICT", struct[1]))

        return new_structs

    def __create_natives(self, structs):
        new_structs = []
        for struct in structs:
            logger.info("Parsing {}".format(struct[0]))
            if struct[0] == "DICT":
                new_structs.append(self.__parse_dict(struct))
            if struct[0] == "LIST":
                new_structs.append(self.__parse_list(struct))
        return new_structs

    def __parse_dict(self, struct):
        string = self.__and_parsing(struct[1])

        logger.info(string)

    def __parse_list(self, struct):
        string = self.__and_parsing(struct[1])

        logger.info(string)

    def __and_parsing(self, string):
        return splitter.findall(
            string
            )