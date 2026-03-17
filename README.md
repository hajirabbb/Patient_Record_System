# Patient Record Management System

## Overview

This is a simple command-line based Patient Record Management System built with Python. It allows users to register, update, search, view, filter, and delete patient records. The system stores patient data in a text file for persistence.

The project demonstrates fundamental programming concepts such as file handling, input validation, modular programming, and data management using lists and dictionaries.

---

## Features

* Register new patients
* Update existing patient information
* View all registered patients
* Search for a patient by ID
* Filter patients by blood type
* Delete patient records
* Persistent data storage using a text file
* Input validation to prevent empty or invalid entries

---

## Technologies Used

* Python 3
* File handling (read/write operations)
* Command-line interface (CLI)

---

## Project Structure

```
project-folder/
│
├── patient_record.py
├── patient_functions.py
├── patients.txt
└── README.md
```

* `patient_record.py` – Entry point of the program
* `patient_functions.py` – Contains all core logic and functions
* `patients.txt` – Stores patient data

---

## How It Works

The system stores patient data in the following format:

```
ID,Name,Age,Gender,BloodType,PhoneNumber,Ailment
```

Each patient is assigned a unique ID (e.g., P001, P002, etc.). The program reads from and writes to the `patients.txt` file to maintain records across sessions.

---

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/hajirabbb/patient-record-system.git
```

2. Navigate into the project directory:

```
cd patient-record-system
```

3. Run the program:

```
python patient_record.py
```

---

## Usage

After running the program, a menu will be displayed:

```
1. Register Patient
2. Update Patient
3. View All Patients
4. Search Patient
5. Filter by Blood Type
6. Delete Patient
7. Exit
```

Select an option by entering the corresponding number and follow the prompts.

---

## Key Functionalities

### Register Patient

Collects patient details and stores them in the system with a unique ID.

### Update Patient

Allows modification of phone number, age, and ailment using the patient ID.

### Search Patient

Retrieves and displays patient details based on ID.

### Filter by Blood Type

Displays all patients with a specific blood type.

### Delete Patient

Removes a patient record permanently from the system.

---

## Input Validation

The system ensures:

* No empty inputs are accepted
* Age must be a valid number
* Blood type must match predefined values
* Menu selections must be valid numbers

---



---

## Author

Your Name

Hajira Baffoe


