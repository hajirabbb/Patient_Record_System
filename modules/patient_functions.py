patients = []
blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
FILE_NAME = "patients.txt"


def get_non_empty_input(prompt):
    """Ensure user does not enter empty input."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please try again.")
        else:
            return value


def generate_patient_id(patients):
    """Generate a unique patient ID."""
    if not patients:
        return "P001"

    max_id = 0
    for patient in patients:
        numeric_part = int(patient["id"][1:])
        if numeric_part > max_id:
            max_id = numeric_part

    return "P" + str(max_id + 1).zfill(3)


def load_patients():
    """Load patient records from file."""
    loaded_patients = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 7:
                    continue

                patient_id, name, age, gender, blood_type, phone_number, ailment = parts

                loaded_patients.append({
                    "id": patient_id,
                    "name": name,
                    "age": int(age),
                    "gender": gender,
                    "blood_type": blood_type,
                    "phone_number": phone_number,
                    "ailment": ailment
                })

    except FileNotFoundError:
        pass

    return loaded_patients


def save_patients(patients):
    """Save all patient records to file."""
    with open(FILE_NAME, "w") as file:
        for patient in patients:
            file.write(
                f"{patient['id']},{patient['name']},{patient['age']},"
                f"{patient['gender']},{patient['blood_type']},"
                f"{patient['phone_number']},{patient['ailment']}\n"
            )


def register_patient(patients):
    """Register patient details."""
    while True:
        print("=" * 32)
        print("Register Patient Menu")
        print("=" * 32)

        name = get_non_empty_input("Enter Name: ").title()

        while True:
            age_input = get_non_empty_input("Enter age: ")
            try:
                age = int(age_input)
                if age > 0:
                    break
                else:
                    print("Age must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            gender = get_non_empty_input("Gender (Male/Female): ").title()
            if gender in ["Male", "Female"]:
                break
            else:
                print("Please enter Male or Female.")

        while True:
            user_blood_type = get_non_empty_input(
                "Enter blood type (A+, A-, B+, B-, AB+, AB-, O+, O-): "
            ).upper()
            if user_blood_type in blood_types:
                break
            else:
                print("Invalid blood type.")

        phone_number = get_non_empty_input("Enter phone number: ")
        ailment = get_non_empty_input("Enter ailment: ").title()

        patient_id = generate_patient_id(patients)

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "blood_type": user_blood_type,
            "phone_number": phone_number,
            "ailment": ailment
        }

        patients.append(patient)
        save_patients(patients)

        print(
            f"\nPatient {name} registered successfully with ID {patient_id}.")

        while True:
            next_patient = get_non_empty_input("Next Patient? (Y/N): ").upper()
            if next_patient in ["Y", "N"]:
                break
            print("Please enter Y or N only.")

        if next_patient == "N":
            break
        else:
            print("\nInput details for next patient.\n")


def update_patient(patients):
    """Update patient details."""
    print("=" * 32)
    print("Update Patient Menu")
    print("=" * 32)

    while True:
        patient_id = get_non_empty_input(
            "Enter patient ID (or type 'exit' to cancel): "
        ).strip().upper()

        if patient_id == "EXIT":
            print("Update cancelled.")
            return

        for patient in patients:
            if patient_id == patient["id"]:
                print(f"\nID found. You are updating {patient['name']}.")
                print("You can only update phone number, ailment, and age.")

                patient["phone_number"] = get_non_empty_input(
                    "New phone number: ")
                patient["ailment"] = get_non_empty_input(
                    "New ailment: ").title()

                while True:
                    age_input = get_non_empty_input("New age: ")
                    try:
                        new_age = int(age_input)
                        if new_age > 0:
                            patient["age"] = new_age
                            break
                        else:
                            print("Age must be greater than 0.")
                    except ValueError:
                        print("Age must be a valid number.")

                save_patients(patients)
                print(f"Patient {patient['name']} updated successfully.")
                return

        print("Patient ID does not exist.")


def view_all_patients(patients):
    """View all registered patients."""
    print("=" * 32)
    print("View Patients Menu")
    print("=" * 32)

    if not patients:
        print("\nNo patients recorded yet.\n")
        return

    for number, patient in enumerate(patients, start=1):
        print(f"\nPatient {number}")
        print("-" * 40)

        for key, value in patient.items():
            print(f"{key.replace('_', ' ').title():15} : {value}")

        print("=" * 40)


def search_patient(patients):
    """Search patient by ID."""
    print("=" * 32)
    print("Search Menu")
    print("=" * 32)

    search_request = get_non_empty_input("Enter the ID of Patient: ").upper()
    print("=" * 32)

    found = False

    for patient in patients:
        if search_request == patient["id"]:
            found = True
            for key, value in patient.items():
                print(f"{key.replace('_', ' ').title():15} : {value}")
            break

    if not found:
        print("ID not found.")


def filter_by_blood_type(patients):
    """Filter patients by blood type."""
    print("=" * 32)
    print("Filter Patient by Blood Type")
    print("=" * 32)

    blood_type_request = get_non_empty_input(
        "What blood type are you searching for? "
    ).upper()

    if blood_type_request not in blood_types:
        print("This is not a valid blood type.")
        return

    found = False
    print(f"\nPatients with blood type {blood_type_request}")
    print("-" * 32)

    for patient in patients:
        if patient["blood_type"] == blood_type_request:
            print(f"{patient['id']} - {patient['name']}")
            found = True

    if not found:
        print("Blood type not found.")


def delete_patient(patients):
    """Delete patient by ID."""
    print("=" * 32)
    print("Delete Patient Menu")
    print("=" * 32)

    delete_patient_request = get_non_empty_input(
        "Enter the ID of patient you want to delete: "
    ).upper()

    found = False

    for patient in patients:
        if patient["id"] == delete_patient_request:
            patients.remove(patient)
            save_patients(patients)
            print(f"{patient['name']} has been deleted successfully.")
            found = True
            break

    if not found:
        print(f"Patient with ID {delete_patient_request} not found.")


def get_menu_choice():
    """Display menu options and return user's choice."""
    menu_options = [
        "Register Patient",
        "Update Patient",
        "View All Patients",
        "Search Patient",
        "Filter by Blood Type",
        "Delete Patient",
        "Exit"
    ]

    print("=" * 32)
    print("Patient Record System")
    print("=" * 32)

    for number, option in enumerate(menu_options, start=1):
        print(f"{number}. {option}")

    while True:
        choice_input = get_non_empty_input("Enter request (1-7): ")

        try:
            request = int(choice_input)
            if 1 <= request <= len(menu_options):
                return request
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid number.")
