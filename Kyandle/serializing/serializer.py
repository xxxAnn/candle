from ..utils.errors import InvalidKyandle

def serialize(struct):
    if isinstance(struct, list):
        serialized = str("^")

        for instance in struct:
            if isinstance(instance, dict) or isinstance(instance, list):
                instance = serialize(instance)
            else:
                instance = __indicate_type(instance)
            serialized += "'" + instance + "' AND "
        
        if serialized.endswith(" AND "):
            serialized = serialized[:-5]

        serialized += str("$")
        return serialized

    elif isinstance(struct, dict):

        serialized = "<"

        for k, v in struct.items():
            if isinstance(k, dict) or isinstance(k, list):
                k = serialize(k)
            else:
                k = __indicate_type(k)
            if isinstance(v, dict) or isinstance(v, list):
                v = serialize(v)
            else:
                v = __indicate_type(v)
            serialized += "'{0}' IS '{1}' AND ".format(k, v)
        
        if serialized.endswith(" AND "):
            serialized = serialized[:-5]

        serialized += ">"
        return serialized

def __indicate_type(instance):
    if isinstance(instance, str):
        instance = "s" + str(instance)
    elif isinstance(instance, int):
        instance = "i" + str(instance)
    elif isinstance(instance, float):
        instance = "f" + str(instance)
    elif isinstance(instance, bool):
        instance = "b" + str(instance)
    instance = str(instance)
    return instance