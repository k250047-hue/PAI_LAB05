import json

filename = "model_results.json"

def create_file():
    try:
        file = open(filename, "x")
        json.dump([], file, indent=4)
        file.close()
    except FileExistsError:
        pass

def read_results():
    file = open(filename, "r")
    data = json.load(file)
    file.close()
    return data

def display_results():
    results = read_results()

    if len(results) == 0:
        print("No model results found.")
        return

    print("\nModel Results")
    for model in results:
        print("Model:", model["model"])
        print("Accuracy:", model["accuracy"])
        print("Precision:", model["precision"])
        print("Recall:", model["recall"])
        print("F1-score:", model["f1_score"])
        print()

def highest_accuracy():
    results = read_results()

    if len(results) == 0:
        print("No model results found.")
        return

    best = results[0]

    for model in results:
        if model["accuracy"] > best["accuracy"]:
            best = model

    print("\nHighest Accuracy")
    print("Model:", best["model"])
    print("Accuracy:", best["accuracy"])

def highest_f1():
    results = read_results()

    if len(results) == 0:
        print("No model results found.")
        return

    best = results[0]

    for model in results:
        if model["f1_score"] > best["f1_score"]:
            best = model

    print("\nHighest F1-score")
    print("Model:", best["model"])
    print("F1-score:", best["f1_score"])

def add_model():
    results = read_results()

    name = input("Enter model name: ")
    accuracy = float(input("Enter accuracy: "))
    precision = float(input("Enter precision: "))
    recall = float(input("Enter recall: "))
    f1 = float(input("Enter F1-score: "))

    new_model = {
        "model": name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }

    results.append(new_model)

    save_results(results)

    print("Model result added successfully.")

def update_model():
    results = read_results()

    name = input("Enter model name to update: ")
    found = False

    for model in results:
        if model["model"] == name:
            model["accuracy"] = float(input("Enter new accuracy: "))
            model["precision"] = float(input("Enter new precision: "))
            model["recall"] = float(input("Enter new recall: "))
            model["f1_score"] = float(input("Enter new F1-score: "))

            found = True
            break

    if found:
        save_results(results)
        print("Model result updated successfully.")
    else:
        print("Model does not exist.")

def remove_model():
    results = read_results()

    name = input("Enter model name to remove: ")
    found = False

    for model in results:
        if model["model"] == name:
            results.remove(model)
            found = True
            break

    if found:
        save_results(results)
        print("Model result removed successfully.")
    else:
        print("Model does not exist.")

def save_results(results):
    file = open(filename, "w")
    json.dump(results, file, indent=4)
    file.close()

create_file()

while True:
    print("\n===== Machine Learning Model Results =====")
    print("1. Display Results")
    print("2. Find Highest Accuracy")
    print("3. Find Highest F1-score")
    print("4. Add New Model")
    print("5. Update Model")
    print("6. Remove Model")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_results()

    elif choice == "2":
        highest_accuracy()

    elif choice == "3":
        highest_f1()

    elif choice == "4":
        add_model()

    elif choice == "5":
        update_model()

    elif choice == "6":
        remove_model()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")