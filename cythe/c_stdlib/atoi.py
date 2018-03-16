from cythe.c_stdlib import _atoi


def parse_charptr_to_py_int(s):
    """
    Convert string to int.
    
    Parameters:
    ----------
    * `s`: [str]
        String to be converted to int.
    """
    return _atoi.parse_charptr_to_py_int(s)
