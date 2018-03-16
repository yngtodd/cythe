from libc.stdlib cimport atoi


cpdef parse_charptr_to_py_int(char* s):
    assert s is not NULL, "Byte string value is NULL."
    return atoi(s)
