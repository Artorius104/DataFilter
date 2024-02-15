def str_type(chaine):
    if chaine.isdigit():
        return "int"
    try:
        float_value = float(chaine)
        return "float" if '.' in chaine else "int"
    except ValueError:
        return "str"
        


def get_file_type(file_path):
    return file_path.split(".")[-1]


def sum_ord(string):
    return sum(ord(c) for c in string)


def get_column_types(data_list):
    column_types = {}

    for item in data_list:
        for key, value in item.items():
            current_type = type(value)

            if key not in column_types:
                column_types[key] = {current_type}
            else:
                column_types[key].add(current_type)

    return column_types