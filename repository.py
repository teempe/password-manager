import json


DATA_FILE_PATH = "data/passwds.json"


def read_json(filepath=DATA_FILE_PATH):
    with open(filepath, "r") as data_file:
        data = json.load(data_file)
    return data    


def write_json(data, filepath=DATA_FILE_PATH):
    with open(filepath, "w") as data_file:
        json.dump(data, data_file, indent=4) 


def find_service(service_name):
    """
    Finds username and password for given service. If not found file or data returns None.

    Paramaters:
        service_name (str): Service name to look for

    Returns:
        tuple: (service, username, password) or None when nothing found
    """
    
    try:
        data = read_json()
    except FileNotFoundError:
        return None

    data_found = data.get(service_name, None)
    if data_found is not None:
        return (service_name, data_found["username"], data_found["password"])
    else:
        return None


def save(service, username, password):
    """Save data to json file."""

    entry = {service : {
        "username": username,
        "password": password
    }}

    try:
        data = read_json()
    except FileNotFoundError:
        write_json(entry)
    else:
        data.update(entry)
        write_json(data)


if __name__ == "__main__":
    print(find_service("Facebook"))
    print(find_service("StackOverflow"))