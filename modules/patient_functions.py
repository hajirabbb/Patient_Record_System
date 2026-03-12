patients = []

def get_menu_choice():
    """This function displays the menu and collects user request"""
    
    
    #This menu allows us to display menu options that user can choose from.
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


def generate_patient_id(patients):
    """A function that generates patient_id"""
    return "P" + str(len(patients) + 1).zfill(3)


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
        gender = input("\nGender(Male/ Female): ")
        blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        while True:
            user_blood_type = input(
                "\nEnter blood type (A+, A-, B+, B-, AB+, AB-, O+, O-): ").upper()
            if user_blood_type in blood_types:
                break
            else:
                print("Please input an appropriate blood type")

        phone_number = int(input("\nEnter phone number: "))
        ailment = input("\nAliment: ")
        id = generate_patient_id(patients)

        # storing to list
        patient = {
            "id": id,
            "name": name,
            "age": age,
            "gender": gender,
            "blood type": user_blood_type,
            "phone number": phone_number,
            "ailment": ailment


        }
        patients.append(patient)
        print(f"\nPatient: {name} registered successfully")

        next_patient = input("\nNext Patient?(Y/N) ").upper()
        if next_patient == "N":
            break

        else:
            print(f"Input details for next patient\n")
