import csv

filename = "patients.csv"

def create_file():
    try:
        file = open(filename, "x", newline="")
        writer = csv.writer(file)
        writer.writerow(["ID", "Age", "BMI", "BloodPressure", "Glucose", "Prediction"])
        file.close()
    except FileExistsError:
        pass

def display_records():
    file = open(filename, "r", newline="")
    reader = csv.DictReader(file)

    print("\nPatient Records")
    for row in reader:
        print(row)

    file.close()

def count_cases():
    file = open(filename, "r", newline="")
    reader = csv.DictReader(file)

    positive = 0
    negative = 0

    for row in reader:
        if row["Prediction"] == "1":
            positive += 1
        else:
            negative += 1

    file.close()

    print("Positive cases:", positive)
    print("Negative cases:", negative)

def glucose_above():
    threshold = float(input("Enter glucose threshold: "))

    file = open(filename, "r", newline="")
    reader = csv.DictReader(file)

    found = False

    print("\nPatients with high glucose:")
    for row in reader:
        if float(row["Glucose"]) > threshold:
            print(row)
            found = True

    file.close()

    if not found:
        print("No patient found.")

def calculate_average():
    file = open(filename, "r", newline="")
    reader = csv.DictReader(file)

    total_bmi = 0
    total_glucose = 0
    count = 0

    for row in reader:
        total_bmi += float(row["BMI"])
        total_glucose += float(row["Glucose"])
        count += 1

    file.close()

    if count > 0:
        print("Average BMI:", total_bmi / count)
        print("Average glucose:", total_glucose / count)
    else:
        print("No records found.")

def add_record():
    patient_id = input("Enter ID: ")
    age = input("Enter age: ")
    bmi = input("Enter BMI: ")
    bp = input("Enter blood pressure: ")
    glucose = input("Enter glucose level: ")
    prediction = input("Enter prediction (1 for positive, 0 for negative): ")

    file = open(filename, "a", newline="")
    writer = csv.writer(file)

    writer.writerow([patient_id, age, bmi, bp, glucose, prediction])

    file.close()

    print("Record added successfully.")

def update_record():
    update_id = input("Enter ID to update: ")

    file = open(filename, "r", newline="")
    reader = csv.DictReader(file)
    records = list(reader)
    file.close()

    found = False

    for row in records:
        if row["ID"] == update_id:
            row["Age"] = input("Enter new age: ")
            row["BMI"] = input("Enter new BMI: ")
            row["BloodPressure"] = input("Enter new blood pressure: ")
            row["Glucose"] = input("Enter new glucose level: ")
            row["Prediction"] = input("Enter new prediction (1/0): ")
            found = True
            break

    if found:
        file = open(filename, "w", newline="")
        fieldnames = ["ID", "Age", "BMI", "BloodPressure", "Glucose", "Prediction"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)

        file.close()

        print("Record updated successfully.")
    else:
        print("Patient ID does not exist.")

create_file()

while True:
    print("\n===== Patient Diabetes Dataset =====")
    print("1. Display Records")
    print("2. Count Positive and Negative Cases")
    print("3. Find Patients Above Glucose Threshold")
    print("4. Calculate Average BMI and Glucose")
    print("5. Add New Record")
    print("6. Update Existing Record")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_records()

    elif choice == "2":
        count_cases()

    elif choice == "3":
        glucose_above()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        add_record()

    elif choice == "6":
        update_record()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")