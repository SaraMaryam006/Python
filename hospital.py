patients = {}

def add_patient(pid, name, age, disease):
    patients[pid] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": "Not Assigned",
        "Days": 0,
        "Bill": 0
    }
    return "Patient Added Successfully"


def assign_doctor(pid, doctor):
    if pid in patients:
        patients[pid]["Doctor"] = doctor
        return "Doctor Assigned"
    else:
        return "Patient ID Not Found"


def generate_bill(pid, days, room_charge, medicine_charge):
    if pid in patients:
        bill = (days * room_charge) + medicine_charge
        patients[pid]["Days"] = days
        patients[pid]["Bill"] = bill
        return bill
    else:
        return "Patient ID Not Found"


def display_patient(pid):
    if pid in patients:
        return patients[pid]
    else:
        return "Patient ID Not Found"


def discharge_patient(pid):
    if pid in patients:
        del patients[pid]
        return "Patient Discharged Successfully"
    else:
        return "Patient ID Not Found"
