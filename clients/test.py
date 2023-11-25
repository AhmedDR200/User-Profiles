import requests


def client():

    """
    This is a simple client that sends a request to the server and prints the response.
    It uses the `requests` library, which must be installed in order for this script to run correctly.
    """

    credentials = {
        'username': 'admin',
        'password': 'password',
    }
    response = requests.post("http://localhost:8000/rest-auth/login", data=credentials)

    print("Status Code: ", response.status_code)
    
    response_data = response.json()
    print("Response Data: ", response_data)


if __name__ == "__main__":
    client()
