import re
import logging

from .errors import InvalidKyandle

line_finder = re.compile(r"(\<|\^)(.*)(\>|\$)")
# nest_finder = re.compile(r"((\<|\|)[^\|]+(\>|\|))")
values_finder = re.compile(r"(\'.*?\')")

logger = logging.getLogger(__name__)

class Parser:

    def parse(self, text):
        structs = line_finder.findall(
            text
            )

        structs = self.__fix(structs)
        natives = []

        if len(structs) > 0:
            if self.__has_extras(text, structs):
                for struct in structs:
                    natives.append(self.__create_natives(struct))
                return natives

        raise InvalidKyandle

    def __has_extras(self, text, structs):

        for struct in structs:
            text = text.replace(struct[1], "")

        text = text.replace("<", "").replace(">", "").replace("$", "").replace("^", "").replace("\n", "").replace("\r", "").replace("\s", "")

        if len(text) > 0:
            return False
        return True

    def __fix(self, structs):
        new_structs = []
        for struct in structs:
            if struct[0] != "<" and struct[2] != ">":
                if struct[0] != "^" and struct[2] != "$":
                    continue

            if struct[0] == "^":
                new_structs.append(("LIST", struct[1]))
            elif struct[0] == "<":
                new_structs.append(("DICT", struct[1]))

        return new_structs

    def __create_natives(self, struct):
        logger.debug("Parsing {}".format(struct[0]))
        if struct[0] == "DICT":
            return self.__parse_dict(struct)
        elif struct[0] == "LIST":
            return self.__parse_list(struct)

    def __parse_list(self, struct):
        values = self.__super_parsing(struct[1])
        return self.__to_list(values)
    
    def __parse_dict(self, struct):
        values = self.__super_parsing(struct[1])
        return self.__to_dict(values)

    def __to_dict(self, super_parsed):
        dic = {}
        
        new_parsed = []
        for pair in super_parsed[3]:
            if pair[1] == 'dict':
                new_parsed.append(self.__to_dict(self.__super_parsing(pair[0])))
            elif pair[1] == 'list':
                new_parsed.append(self.__to_list(self.__super_parsing(pair[0])))
            elif pair[1] == 'native':
                new_parsed.append(pair[0])
        
        i = 1
        while i<len(new_parsed):
            dic[new_parsed[i-1]] = new_parsed[i]

            i += 2

        return dic
    
    def __to_list(self, super_parsed):
        to_list = []
        for native in super_parsed[2]:
            to_list.append(self.__to_list(self.__super_parsing(native)))
        for native in super_parsed[1]:
            to_list.append(self.__to_list(self.__super_parsing(native)))

        for nonnative in super_parsed[0]:
            to_list.append(nonnative)

        return to_list

    def __super_parsing(self, string):
        string = string.replace("'^", "^").replace("$'", "$").replace("'<", "<").replace(">'", ">")
        data = []
        lits = []
        lists = []
        dicts = []
        values = []
        opened_lit = -1
        opened_lists = []
        opened_dicts = []

        for i in range(len(string)):

            if string[i] == "'" and len(opened_lists) == 0 and len(opened_dicts) == 0:
                if opened_lit != -1:
                    type_identifier = string[opened_lit+1]
                    from_index = (opened_lit+2)
                    lits.append((from_index, i, type_identifier))
                    values.append((self.__typer(type_identifier, string[lits[-1][0]:lits[-1][1]]), 'native'))
                    opened_lit = -1
                else:
                    opened_lit = i

            elif string[i] == "^":
                opened_lists.append(i)

            elif string[i] == "<":
                opened_dicts.append(i)

            elif string[i] == "$":
                if len(opened_lists) > 0:
                    from_index = (opened_lists.pop(-1)+1)
                    if len(opened_lists) == 0 and len(opened_dicts) == 0:
                        lists.append((from_index, i))
                        values.append((string[lists[-1][0]:lists[-1][1]], 'list'))
                else:
                    raise InvalidKyandle

            elif string[i] == ">":
                if len(opened_dicts) > 0:
                    from_index = (opened_dicts.pop(-1)+1)
                    if len(opened_dicts) == 0 and len(opened_lists) == 0:
                        dicts.append((from_index, i))
                        values.append((string[dicts[-1][0]:dicts[-1][1]], 'dict'))
                else:
                    raise InvalidKyandle
            
        if len(opened_dicts) > 0 or len(opened_lists) > 0 or opened_lit != -1:
            for rg in lits:
                print(string[rg[0]:rg[1]])
            raise InvalidKyandle
        
        true_dicts = []
        true_lists = []
        true_lits = []

        for rg in lits:
            true_lits.append(self.__typer(rg[2], string[rg[0]:rg[1]]))

        for rg in dicts:
            true_dicts.append(string[rg[0]:rg[1]])

        for rg in lists:
            true_lists.append(string[rg[0]:rg[1]])

        tup = (true_lits, true_dicts, true_lists, values)         

        return tup

    def __typer(self, type_identifier, obj):
        if type_identifier == "s":
            return str(obj)
        elif type_identifier == "f":
            return float(obj)
        elif type_identifier == "i":
            return int(obj)
        elif type_identifier == "b":
            return bool(obj)
        
