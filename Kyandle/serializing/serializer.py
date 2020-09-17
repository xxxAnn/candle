from ..utils.errors import InvalidKyandle

def serialize(struct):
    if isinstance(struct, list):
        serialized = str("^")

        for instance in struct:
            if isinstance(instance, dict) or isinstance(instance, list):
                instance = serialize(instance)
            serialized += "'" + str(instance) + "' AND "
        
        if serialized.endswith(" AND "):
            serialized = serialized[:-5]

        serialized += str("$")
        return serialized

    elif isinstance(struct, dict):

        serialized = "<"

        for k, v in struct.items():
            if isinstance(k, dict) or isinstance(k, list):
                k = serialize(k)
            if isinstance(v, dict) or isinstance(v, list):
                v = serialize(v)
            serialized += "'{0}' IS '{1}' AND ".format(str(k), str(v))
        
        if serialized.endswith(" AND "):
            serialized = serialized[:-5]

        serialized += ">"
        return serialized