import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    print("GET Request")
    response = requests.get(url + "/1", timeout=10)

    print("Status Code:", response.status_code)
    print("JSON Response:")
    print(response.json())


    print("\nPOST Request")

    data = {
        "title": "Image Prediction",
        "body": "Cat detected in image",
        "userId": 1
    }

    response = requests.post(url, json=data, timeout=10)

    print("Status Code:", response.status_code)
    print("JSON Response:")
    print(response.json())


    print("\nPUT Request")

    data = {
        "id": 1,
        "title": "Updated Prediction",
        "body": "Dog detected in image",
        "userId": 1
    }

    response = requests.put(url + "/1", json=data, timeout=10)

    print("Status Code:", response.status_code)
    print("JSON Response:")
    print(response.json())


    print("\nPATCH Request")

    data = {
        "body": "Updated image prediction"
    }

    response = requests.patch(url + "/1", json=data, timeout=10)

    print("Status Code:", response.status_code)
    print("JSON Response:")
    print(response.json())


    print("\nDELETE Request")

    response = requests.delete(url + "/1", timeout=10)

    print("Status Code:", response.status_code)
    print("JSON Response:")
    
    if response.text:
        print(response.json())
    else:
        print("Record deleted successfully.")


except requests.exceptions.Timeout:
    print("Request timed out.")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet connection.")

except requests.exceptions.HTTPError:
    print("HTTP error occurred.")

except ValueError:
    print("Invalid JSON response received.")

except requests.exceptions.RequestException:
    print("An API request error occurred.")

