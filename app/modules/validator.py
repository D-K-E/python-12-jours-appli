"""
Validates given data with respect to the keys specified in given schema
"""
# Author: Kaan Eraslan
# License: see, LICENSE


def compare_keys(dict1: dict, dict2: dict):
    "Compare keys of two dicts"
    for key in dict1.keys():
        if key not in dict2.keys():
            return False
    return True


def check_simple_dict(sdict: dict):
    "check whether sdict is simple key value pairs with values non containers"
    for val in sdict.values():
        if isinstance(val, (list, tuple, dict, set)):
            return False
    return True


def compare_simple_data_to_schema(schema: dict, data: dict):
    "Simple comparison of keys between schema and data"
    assert check_simple_dict(schema)
    assert check_simple_dict(data)
    return compare_keys(schema, data)


def check_simple_list(ls: list) -> bool:
    "Check if list contains a dictionary as an element"
    for l in ls:
        if isinstance(l, dict):
            return False
    return True


def check_simple_list_dict(sdict: dict) -> bool:
    """Check whether sdict consists of values with either non containers or
    simple list"""
    for val in sdict.values():
        if isinstance(val, (dict, set)):
            return False
        if isinstance(val, (list, tuple)):
            if not check_simple_list(val):
                return False
    return True


def compare_simple_list_data_to_schema(schema: dict, data: dict) -> bool:
    "Compare simple list data keys to schema keys"
    assert check_simple_list_dict(schema)
    assert check_simple_list_dict(data)
    return compare_keys(schema, data)

def 


def check_complex_list(ls: list):
    "check whether list contains a dict as element"
    return not check_simple_list(ls)


def check_complex_list_dict(sdict: dict) -> bool:
    "check whether a dict contains a list containing a dict"
    for val in sdict.values():
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, dict):
                    return True
    return False


def compare_complex_list_data_to_schema(schema: dict, data: dict) -> bool:
    "Compare complex list data to schema"
    assert check_complex_list_dict(schema)
    assert check_complex_list_dict(data)
