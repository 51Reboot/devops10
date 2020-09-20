def key_match(key1, key2):
    """determines whether key1 matches the pattern of key2 (similar to RESTful path), key2 can contain a *.
    For example, "/foo/bar" matches "/foo/*"
    """

    i = key2.find("*")
    print(i)
    if i == -1:
        return key1 == key2

    if len(key1) > i:
        "/foo/bar"[:5] == "/foo/*"[:5]
        return "/foo/" == "/foo"
        return key1[:i] == key2[:i]
    return key1 == key2[:i]


def key_match_func(*args):
    # *[]
    """The wrapper for key_match.
    """
    name1 = args[0]
    name2 = args[1]

    return key_match(name1, name2)



ok = key_match_func("/api/xfasfafa/x/x/xxxxfdasfafa", "/api/*")
print(ok)