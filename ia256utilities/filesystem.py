import json
import os


def load_json(path, default_dict=True):
    """
    Loads a json file and returns it as a dictionary or list
    """
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, encoding="utf8") as file:
            data = json.load(file)
        file.close()
        return data
    else:
        if default_dict:
            return {}
        else:
            return []


def save_json(data, path, indent=None):
    """
    Saves dictionary or list as json file
    """
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w', encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False, indent=indent))
    file.close()

def save(data, path):
    """
    Saves text to a file
    """
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w', encoding="utf-8") as file:
        file.write(data)
    file.close()


def save_binary(data, path):
    """
    Saves data as a binary file
    """
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'wb') as file:
        file.write(data)
    file.close()


def load_binary(path):
    """
    Loads data as a binary file
    """
    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'rb') as file:
            data = file.read()
        file.close()
        return data
    else:
        return None
