from patient_functions import register_patient,generate_patient_id,get_menu_choice, view_all_patients, search_patient,update_patient
patients = []

while True:
    choice = get_menu_choice()
    if choice == 1:
        register_patient()
    elif choice == 2:
        update_patient(patients)
    elif choice == 3:
        view_all_patients(patients)
    elif choice == 4:
        search_patient(patients)