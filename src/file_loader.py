import csv
import json
import yaml
import xml.etree.ElementTree as ET
from itertools import zip_longest

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

def load_json(path):
    with open(path, 'r') as file_json:
        data = json.load(file_json)
        
    return data

def load_yaml(path):
    with open(path, 'r') as file_yaml:
        data = yaml.safe_load(file_yaml)

    return data

def create_datadict_from_xml(unstructured_data, tag_list):
    data = []
    save = []
    for elem in zip_longest(*unstructured_data):
        save.append(elem)

    for elem in save:
        new_dict = {}
        index = 0
        for key in tag_list:
            new_dict[key] = elem[index]
            index += 1
        data.append(new_dict)

    return data

def parse_xml_data(root, tag_list):
    unstructured_data = []
    for tag in tag_list:
        container = []
        for elem in root.iter(tag):
            container.append(elem.text)
        unstructured_data.append(container)
    
    data = create_datadict_from_xml(unstructured_data, tag_list)

    return data

def get_all_xml_tags(root):
    root_tag = root.tag
    get_all_tags = set([elem.tag for elem in root.iter()])
    tag_list = list(get_all_tags)
    tag_list.remove(root_tag)

    return tag_list

def load_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    tag_list = get_all_xml_tags(root)

    data = parse_xml_data(root, tag_list)

    return data
