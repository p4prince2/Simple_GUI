import json


class Database:
    """
    A simple database handler class for storing and verifying user data
    (name, email, password) using a JSON file (`db.json`).
    """

    def add_data(self, name, email, password):
        """
        Adds a new user's data (name, email, password) to the database.

        Parameters:
            name (str): The name of the user.
            email (str): The email of the user, used as a unique identifier.
            password (str): The password for the user account.

        Returns:
            int:
                1 if the user was added successfully.
                0 if the email already exists in the database.
        """
        with open("db.json", 'r') as f:
            database = json.load(f)

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open("db.json", 'w') as f:
                json.dump(database, f)
            return 1

    def check_data(self, email, password):
        """
        Verifies if a given email and password combination exists in the database.

        Parameters:
            email (str): The email to be checked.
            password (str): The password to be validated.

        Returns:
            int:
                1 if the credentials are correct.
                0 if the email is not found or password is incorrect.
        """
        with open("db.json", "r") as f:
            database = json.load(f)

        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0
