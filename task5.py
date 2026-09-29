import requests
import json
import csv

url = "https://jsonplaceholder.typicode.com/posts"

try:
    user_id = input("Enter user ID to retrieve posts (1-10): ")

    params = {
        "userId": user_id
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        if len(data) == 0:
            print("No text data found.")
        else:
            results = []

            for post in data:
                record = {
                    "id": post["id"],
                    "text": post["title"] + " " + post["body"],
                    "source": "User " + str(post["userId"]),
                    "user_id": post["userId"]
                }

                results.append(record)

            print("\nRetrieved Text Data")

            for item in results:
                print("ID:", item["id"])
                print("Text:", item["text"])
                print("Source:", item["source"])
                print()

            try:
                with open("text_data.json", "w") as file:
                    json.dump(results, file, indent=4)

                with open("text_data.csv", "w", newline="") as file:
                    fields = ["id", "text", "source", "user_id"]
                    writer = csv.DictWriter(file, fieldnames=fields)

                    writer.writeheader()
                    writer.writerows(results)

                print("Data saved successfully to text_data.json")
                print("Data saved successfully to text_data.csv")

            except OSError:
                print("File error. Data could not be saved.")

    else:
        print("Request failed. HTTP status:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet connection.")

except requests.exceptions.RequestException:
    print("An error occurred while requesting data.")

except ValueError:
    print("Invalid JSON response received from the API.")

