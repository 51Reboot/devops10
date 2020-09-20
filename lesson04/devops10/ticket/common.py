

def write_file(filename, data):
    try:
        with open(filename, 'w') as fd:
            fd.write(data)
    except Exception as e:
        return e.args, False
    return "", True