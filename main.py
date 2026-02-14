import hospital

while True:
    print("\n----- HOSPITAL MANAGEMENT SYSTEM -----")
    print("1. Add Patient")
    print("2. Assign Doctor")
    print("3. Generate Bill")
    print("4. Display Patient Details")
    print("5. Discharge Patient")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        print(hospital.add_patient(pid, name, age, disease))

    elif choice == 2:
        pid = input("Enter Patient ID: ")
        doctor = input("Enter Doctor Name: ")
        print(hospital.assign_doctor(pid, doctor))

    elif choice == 3:
        pid = input("Enter Patient ID: ")
        days = int(input("Enter number of days admitted: "))
        room = int(input("Enter room charge per day: "))
        medicine = int(input("Enter medicine charges: "))
        bill = hospital.generate_bill(pid, days, room, medicine)
        print("Total Bill Amount: Rs.", bill)

    elif choice == 4:
        pid = input("Enter Patient ID: ")
        details = hospital.display_patient(pid)
        print(details)

    elif choice == 5:
        pid = input("Enter Patient ID: ")
        print(hospital.discharge_patient(pid))

    elif choice == 6:
        print("Exiting Hospital System")
        break

    else:
        print("Invalid Choice")
