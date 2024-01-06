import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Response Body:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
