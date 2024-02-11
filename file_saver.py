import csv
import json

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