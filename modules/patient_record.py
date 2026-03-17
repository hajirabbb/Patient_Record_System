from patient_functions import (
    register_patient,
    get_menu_choice,
    view_all_patients,
    search_patient,
    update_patient,
    filter_by_blood_type,
    delete_patient,
    load_patients
)


def main():
    patients = load_patients()

    while True:
        choice = get_menu_choice()

        if choice == 1:
            register_patient(patients)
        elif choice == 2:
            update_patient(patients)
        elif choice == 3:
            view_all_patients(patients)
        elif choice == 4:
            search_patient(patients)
        elif choice == 5:
            filter_by_blood_type(patients)
        elif choice == 6:
            delete_patient(patients)
        elif choice == 7:
            print("Program ended successfully.")
            break


if __name__ == "__main__":
    main()
