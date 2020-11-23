import json


DATA_FILE_PATH = "data/passwds.json"


def save(service, username, password):
    """Save data to json file."""

    entry = {service : {
        "username": username,
        "password": password
    }}

    try:
        with open(DATA_FILE_PATH, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        write_json(entry)
    else:
        data.update(entry)
        write_json(data)


def write_json(data, filepath=DATA_FILE_PATH):
    with open(filepath, "w") as data_file:
        json.dump(data, data_file, indent=4)    