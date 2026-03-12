def generate_patient_id(patients):
    """A function that generates patient_id"""
    return "P" + str(len(patients) + 1).zfill(3)
