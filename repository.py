import json


class JsonRepository:
    """
    Provides CRUD operations on json storage file.

    Attributes:
        filepath (str): path to json file

    Methods:
        save(service, username, password) -> None
        find(service) -> tuple
        update(service, username, password) -> None
        delete(service) -> boolean
    """

    def __init__(self, filepath="data/passwds.json"):
        """
        Constructs attributes for JsonRepository object.

        Parameters:
            filepath (str): path to json file
        """

        self.filepath = filepath

    def _write_json(self, data):
        with open(self.filepath, "w") as data_file:
            json.dump(data, data_file, indent=4)

    def _read_json(self):
        try:
            with open(self.filepath, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            return None
        else:
            return data

    def save(self, service, username, password):
        """
        Saves data into json file or update if service already exists.

        Parameters:
            service (str): service/website name
            username (str): username/login
            password (str): password
        
        Returns:
            None
        """

        service = service.lower()
        entry = {service: 
            {"username":username, "password":password}
        }

        data = self._read_json()
        if data is None:
            self._write_json(entry)
        else:
            data.update(entry)
            self._write_json(data)

    def find(self, service):
        """
        Get data from json file for given service name if exists.
        Return tuple with data or None if nothing found.

        Parameters:
            service (str): service/website name to seach
        
        Returns:
            tuple
        """

        service = service.lower()
        data = self._read_json()
        if (data is None) or (service not in data):
            return None

        entry = data[service]
        return (service, entry["username"], entry["password"])
    
    def update(self, service, username, password):
        """
        Updates username and password for given service name if exists.

        Parameters:
            service (str): service/website name
            username (str): username/login
            password (str): password

        Returns:
            None
        """

        self.save(service, username, password)

    def delete(self, service):
        """
        Deletes data for given service name if exists.
        Returns True if operation succeded or False otherwise.

        Parameters:
            service (str): service/website name

        Returns:
            None
        """

        service = service.lower()
        data = self._read_json()
        if (data is None) or (service not in data):
            return False

        del data[service]
        self._write_json(data)
        return True     
