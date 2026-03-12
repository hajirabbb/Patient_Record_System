def get_menu_choice():
    "This menu allows us to display menu options that user can choose from."
    menu_options = ["Register Patient", "Update Patient", "View All Patient", "Search Patient",
                    "Filter by Blood Type", "Delete Patient", "Exit"]

    """This function displays the menu and collects user request"""
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
