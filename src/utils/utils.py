import csv
import json

def load_csv(path):
    with open(path,'r') as csvfile:
    
        dict_data = []
        
        reader = csv.reader(csvfile, delimiter=',')
    
        fields = next(reader)
        
        for row in reader:
            dict_row = {}

            for i,f in enumerate(fields):
                value = row[i]
                try:
                    value = int(row[i])
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                dict_row[f] = value
                
            dict_data.append(dict_row)
            
    return dict_data



def save_csv(dict_data, path, filename):
    
    with open(f"{path}/{filename}", mode='w', newline='') as file_csv:
        
        columns = dict_data[0].keys()
        
        writer = csv.DictWriter(file_csv, fieldnames=columns)
        writer.writeheader()

        writer.writerows(dict_data)

    print(f"Les données ont été enregistrées dans {path}.")



def save_json(dict_data, path, filename):
    
    with open(f"{path}/{filename}", 'w') as file_json:
        json.dump(dict_data, file_json, indent=2)

    print(f"Les données ont été enregistrées dans {path}.")


def load_json(path):
    with open(path, 'r') as file_json:
        data = json.load(file_json)
        
    return data



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