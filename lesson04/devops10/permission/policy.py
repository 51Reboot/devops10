def key_match_method(key1, key2):
    """determines whether key1 matches the pattern of key2 (similar to RESTful path), key2 can contain a *.
    For example, "/foo/bar" matches "/foo/*"
    """
    print("key1: {}".format(key1))
    print("key2: {}".format(key2))
    if '|' not in key2:
        print(2)
        i = key2.find("*")
        if i == -1:
            return key1 == key2

        if len(key1) > i:
            return key1[:i] == key2[:i]
        return key1 == key2[:i]
    else:
        key2 = [x.strip() for x in key2.split('|') if x]
        return key1 in key2


def key_match_method_func(*args):
    """The wrapper for key_match.
    """
    name1 = args[0]
    name2 = args[1]

    return key_match_method(name1, name2)