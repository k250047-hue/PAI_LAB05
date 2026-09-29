import requests
import json
import csv

url = "https://jsonplaceholder.typicode.com/posts"

try:
    user_id = input("Enter user ID (1-10): ")

    params = {
        "userId": user_id
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        raise requests.exceptions.HTTPError("HTTP Error")

    data = response.json()

    if len(data) == 0:
        print("No data found.")
    else:
        results = []

        for post in data:
            result = {
                "id": post["id"],
                "user_id": post["userId"],
                "text": post["title"],
                "score": len(post["body"])
            }

            results.append(result)

        total_score = 0

        for item in results:
            total_score += item["score"]

        average = total_score / len(results)

        highest = results[0]

        for item in results:
            if item["score"] > highest["score"]:
                highest = item

        print("\nProcessed Data")

        for item in results:
            print(item)

        print("\nAverage Score:", average)
        print("Highest Score:", highest["score"])
        print("Highest Scoring Text:", highest["text"])

        try:
            with open("processed_data.json", "w") as file:
                json.dump(results, file, indent=4)

            with open("processed_data.csv", "w", newline="") as file:
                fields = ["id", "user_id", "text", "score"]
                writer = csv.DictWriter(file, fieldnames=fields)

                writer.writeheader()
                writer.writerows(results)

            print("\nData saved successfully.")

        except OSError:
            print("File could not be created or saved.")

        try:
            with open("processed_data.json", "r") as file:
                saved_json = json.load(file)

            print("\nJSON File Verified")
            print("Records:", len(saved_json))

        except FileNotFoundError:
            print("JSON file does not exist.")

        except json.JSONDecodeError:
            print("JSON file contains invalid data.")

        try:
            with open("processed_data.csv", "r", newline="") as file:
                reader = csv.DictReader(file)
                saved_csv = list(reader)

            print("CSV File Verified")
            print("Records:", len(saved_csv))

        except FileNotFoundError:
            print("CSV file does not exist.")

except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet connection.")

except requests.exceptions.Timeout:
    print("The API request timed out.")

except requests.exceptions.HTTPError:
    print("HTTP error. The API could not provide the data.")

except json.JSONDecodeError:
    print("Invalid JSON data received from the API.")

except requests.exceptions.RequestException:
    print("An error occurred while connecting to the API.")

else:
    print("\nAPI processing completed successfully.")

finally:
    print("Program execution finished.")

