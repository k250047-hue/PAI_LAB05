import requests

url = "https://dummyjson.com/products/search"

try:
    text = input("Enter product to search: ")

    params = {
        "q": text
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if "products" in data and len(data["products"]) > 0:
            product = data["products"][0]

            prediction = product["title"]
            confidence = product["rating"]
            input_data = text

            print("\nAPI Result")
            print("Input:", input_data)
            print("Prediction:", prediction)
            print("Confidence Score:", confidence)
        else:
            print("The API did not provide a requested result.")

    else:
        print("HTTP Error:", response.status_code)
        print("The API could not provide the requested result.")

except requests.exceptions.Timeout:
    print("The request took too long and timed out.")

except requests.exceptions.ConnectionError:
    print("Connection error. Please check your internet connection.")

except requests.exceptions.HTTPError:
    print("An HTTP error occurred.")

except ValueError:
    print("Invalid JSON response received from the API.")

except requests.exceptions.RequestException:
    print("An error occurred while connecting to the API.")

