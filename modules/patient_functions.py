patients = []
blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]


def generate_patient_id(patients):
    """A function that generates patient_id"""
    return "P" + str(len(patients) + 1).zfill(3)


def load_patient():
    try:
        with open("patient.txt", "r") as file:
            for line in file:
                id, name, age, gender, blood_type,  phone_number, ailment = line.strip(). split(",")
                patients.append({
                    "id": id,
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "blood type": blood_type,
                    "phonenumber": phone_number,
                    "ailment": ailment})
    except FileNotFoundError:
        pass

    return patients


def save_patient(patients):
    with open("patient.txt", "w") as file:
        for patient in patients:
            file.write(
                f"{patient['id']},{patient['name']},{patient['age']},{patient['gender']},{patient['blood type']},{patient['phonenumber']},{patient['ailment']} \n")


def register_patient():
    """A function that registers patients details"""
    while True:
        print("="*32)
        print("Register Patient Menu")
        print("="*32)

        name = input("Enter Name: ").title()
        while True:
            try:
                age = int(input("\nEnter age(in numbers): "))
                break
            except ValueError:
                print("Please input a valid number")
        while True:
            gender_types = ["Female", "Male"]
            gender = input("\nGender(Male/ Female): ").title()
            if gender in gender_types:
                break
            else:
                print("\nPlease enter a valid gender type")

        while True:
            user_blood_type = input(
                "\nEnter blood type (A+, A-, B+, B-, AB+, AB-, O+, O-): ").upper()
            if user_blood_type in blood_types:
                break
            else:
                print("\nPlease input an appropriate blood type")

        phone_number = input("\nEnter phone number: ")
        ailment = input("\nAliment: ")
        id = generate_patient_id(patients)

        # storing to list
        patient = {
            "id": id,
            "name": name,
            "age": age,
            "gender": gender,
            "blood type": user_blood_type,
            "phonenumber": phone_number,
            "ailment": ailment


        }
        patients.append(patient)
        print(f"\nPatient: {name} registered successfully")
        save_patient(patients)
        next_patient = input("\nNext Patient?(Y/N) ").upper()
        if next_patient == "N":
            break

        else:
            print(f"Input details for next patient\n")


def update_patient(patients):
    """This functions allows users to update some patient details ie (phone number, ailment and age)"""
    print("="*32)
    print("Update Patient Menu")
    print("="*32)

    while True:
        patient_id = input("Enter patient ID:(or type 'exit' to cancel): ")

        if patient_id.lower() == "exit":
            print("Update cancelled.")
            break

        # Search for the patient
        for patient in patients:
            if patient_id == patient["id"]:
                print(
                    f"Id found. You want to update {patient['name']}. You can only update'phone number', 'age' and 'ailment' ")
                # updating fields

                patient["phonenumber"] = input("New phone number: ")

                patient["ailment"] = input("New Ailment: ")

                while True:
                    try:
                        patient["age"] = int(input("New age: "))
                        break
                    except ValueError:
                        print("Age must be a number")
                save_patient(patients)
                print(f"Patient {patient['name']} updated successfully")
                return

        else:
            print("Patient Id does not exist")


def view_all_patients(patients):
    """This Functions allows users view all registered patients."""
    print("="*32)
    print("View Patients Menu")
    print("="*32)
    if patients == []:
        print("\nNo patients recorded yet\n")
        return
    for number, patient in enumerate(patients, start=1):
        print(f"Patient {number}")
        print("-"*40)

        for key, value in patient.items():

            print(f"{key.title():15} : {value}")

            print("="*32)


def search_patient(patients):
    """This functions allows user search patient details by getting their id."""

    found = False

    print("=" * 32)
    print("Search Menu")
    print("=" * 32)
    search_request = input("Enter the Id of Patient: ")
    print("=" * 32)
    for patient in patients:
        if search_request == patient["id"]:
            found = True
            for key, value in patient.items():
               print(f"{key.title():15} : {value}")
        if not found:
            print("Id not found")




def filter_by_blood_type(patients):
    """This function allows us to filter patients by thier blood types"""
    print("="*32)
    print("Filter Patient by blood type")
    print("="*32)
    blood_type_request = input("what blood are you searching for? ").upper()

    if blood_type_request not in blood_types:
        print("This blood type is not a valid blood type")
        return

    found = False

    for patient in patients:
        if patient["blood type"] == blood_type_request:
            print("-"*32)
            print(f"Patients with blood type{blood_type_request}")
            print("-"*32)
            print(patient["name"])
            found = True

    if not found:
        print("\nBlood type not found")


def delete_patient(patients):
    """This function deletes patient after finding their id numbers."""
    print("=" * 32)
    print("Delete Patient Menu")
    print("=" * 32)
    delete_patient_request = input(
        "Enter the id of patient you want to delete: ")

    found = False

    for patient in patients:
        """the for loop loops through the dictionary and list to patient associated with stated id."""
        if patient["id"] == delete_patient_request:
            patients.remove(patient)
            save_patient(patients)
            print(f"{patient['name']} has been deleted successfully")
            found = True

        if not found:
            print(f"Patient with id {delete_patient_request} not found")
            

def get_menu_choice():
    """This menu allows us to display menu options that user can choose from."""
    menu_options = ["Register Patient", "Update Patient", "View All Patient", "Search Patient",
                    "Filter by Blood Type", "Delete Patient", "Exit"]


    print("=" * 32)
    print("Patient Record System")
    print("=" * 32)
    for number, option in enumerate(menu_options, start=1):
       print(f"{number}.{option}")

    menu_active = True
    while menu_active:
        try:
            request = int(input("Enter request(1-7):"))
            if 1 <= request <= len(menu_options):
                menu_active = False
                return request
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please check your input and make it match the requested input")



