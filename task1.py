filename = "experiments.txt"

def create_file():
    file = open(filename, "w")
    file.close()

def add_experiment():
    exp_id = input("Enter experiment ID: ")
    model = input("Enter model name: ")
    dataset = input("Enter dataset name: ")
    rate = input("Enter learning rate: ")
    epochs = input("Enter number of epochs: ")

    file = open(filename, "a")
    file.write(exp_id + "," + model + "," + dataset + "," + rate + "," + epochs + "\n")
    file.close()

    print("Experiment added successfully.")

def display_experiments():
    file = open(filename, "r")
    data = file.readlines()
    file.close()

    if len(data) == 0:
        print("No experiments found.")
        return

    print("\nExperiment Configurations:")
    for line in data:
        parts = line.strip().split(",")
        print("ID:", parts[0])
        print("Model:", parts[1])
        print("Dataset:", parts[2])
        print("Learning Rate:", parts[3])
        print("Epochs:", parts[4])
        print()

def search_experiment():
    search_id = input("Enter experiment ID to search: ")

    file = open(filename, "r")
    found = False

    for line in file:
        parts = line.strip().split(",")

        if parts[0] == search_id:
            print("\nExperiment Found")
            print("ID:", parts[0])
            print("Model:", parts[1])
            print("Dataset:", parts[2])
            print("Learning Rate:", parts[3])
            print("Epochs:", parts[4])
            found = True
            break

    file.close()

    if not found:
        print("Experiment does not exist.")

def update_experiment():
    update_id = input("Enter experiment ID to update: ")

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    found = False

    for i in range(len(lines)):
        parts = lines[i].strip().split(",")

        if parts[0] == update_id:
            model = input("Enter new model name: ")
            dataset = input("Enter new dataset name: ")
            rate = input("Enter new learning rate: ")
            epochs = input("Enter new number of epochs: ")

            lines[i] = update_id + "," + model + "," + dataset + "," + rate + "," + epochs + "\n"
            found = True
            break

    if found:
        file = open(filename, "w")
        file.writelines(lines)
        file.close()
        print("Experiment updated successfully.")
    else:
        print("Experiment does not exist.")

def delete_experiment():
    delete_id = input("Enter experiment ID to remove: ")

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    new_lines = []
    found = False

    for line in lines:
        parts = line.strip().split(",")

        if parts[0] == delete_id:
            found = True
        else:
            new_lines.append(line)

    if found:
        file = open(filename, "w")
        file.writelines(new_lines)
        file.close()
        print("Experiment removed successfully.")
    else:
        print("Experiment does not exist.")

create_file()

while True:
    print("\n===== AI Experiment Manager =====")
    print("1. Add Experiment")
    print("2. Display Experiments")
    print("3. Search Experiment")
    print("4. Update Experiment")
    print("5. Remove Experiment")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_experiment()

    elif choice == "2":
        display_experiments()

    elif choice == "3":
        search_experiment()

    elif choice == "4":
        update_experiment()

    elif choice == "5":
        delete_experiment()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")