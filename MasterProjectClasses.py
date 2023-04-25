"""
Sean's Project Classes Branch

Testing Below
Doctor:
1 -
2 -
3 -
4 -
5 -
6 -

Patient:
1 - Works, but should be formatted to a table // first entry displayed should be hidden
2 - Works, but should be formatted to a table
3 - Works, but needs to display {pid} instead of BLANK
4 - Works
5 - Works

Management:
1 -
2 - Works, just needs some formatting
3 - Works, but if you open Doctor/Patient, go to Main Menu, then try to exit, it will not exit
"""


class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None,
                 qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def get_working_time(self):
        return self.working_time

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"


class DoctorManager:

    def __init__(self):
        pass

    def format_dr_info(self, doctor):
        pass

    def enter_dr_info(self):
        pass

    def read_doctors_file(self):
        pass

    def search_doctor_by_id(self):
        pass

    def search_doctor_by_name(self):
        pass

    def display_doctor_info(self, Doctor):
        pass

    def edit_doctor_info(self):
        pass

    def display_doctors_list(self):
        pass

    def write_list_of_doctors_to_file(self):
        pass

    def add_dr_to_file(self):
        pass


class Patient:
    def __init__(self, pid="", name="", disease="", gender="", age=""):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid

    def set_pid(self, new_pid):
        self.pid = new_pid

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_disease(self):
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}\n"

    def enter_patient_info(self):
        print(" ")
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        print(" ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        with open("patients.txt", "r") as f:
            for line in f:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    def search_patient_by_id(self):
        print(" ")
        pid = input("Enter patient ID: ")
        for patient in self.patients:
            if patient.pid == pid:
                self.display_patient_info(patient)
                print(" ")
                return
        print("Can't find the patient...")

    def display_patient_info(self, patient):
        print(" ")
        print(f"Patient ID: {patient.pid}")
        print(f"Name: {patient.name}")
        print(f"Disease: {patient.disease}")
        print(f"Gender: {patient.gender}")
        print(f"Age: {patient.age}")

    def edit_patient_info_by_id(self):
        print(" ")
        pid = input("Enter patient ID to edit: ")
        for patient in self.patients:
            if patient.pid == pid:
                patient.name = input("Enter new name: ")
                patient.disease = input("Enter new disease: ")
                patient.gender = input("Enter new gender: ")
                patient.age = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                print(" ")
                print(f"Patient whose ID is {pid} has been added.\n")
                return
        print("Cannot find the patient...")

    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)
            print()

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as f:
            for patient in self.patients:
                f.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patients.append(patient)
        with open("patients.txt", "a") as f:
            f.write(self.format_patient_info_for_file(patient))
        print(f"Patient whose ID is BLANK has been added.\n")


class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            choice = input(
                "Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, or "
                "select 3 to stop:\n1 -  Doctors\n2 -  Patients\n3 -  Exit Program\n")
            if choice == "1":
                self.display_doctor_menu()
            elif choice == "2":
                self.display_patient_menu()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_doctor_menu(self):
        while True:
            choice = input("Doctor Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - "
                           "Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to Main Menu\n")
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                new_doctor = self.doctor_manager.add_dr_to_file()
                self.doctor_manager.write_list_of_doctors_to_file()
                print("New doctor added successfully.")
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
                self.doctor_manager.write_list_of_doctors_to_file()
                print("Doctor information updated successfully.")
            elif choice == "6":
                print(" ")
                self.display_menu()
            else:
                print("Invalid choice. Please try again.")

    def display_patient_menu(self):
        while True:
            choice = input("Patient Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n"
                           "4 - Edit patient info\n5 - Back to the Main Menu\n")
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_id()
            elif choice == "3":
                new_patient = self.patient_manager.add_patient_to_file()
                self.patient_manager.write_list_of_patients_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()
                self.patient_manager.write_list_of_patients_to_file()
            elif choice == "5":
                print(" ")
                self.display_menu()
            else:
                print("Invalid choice. Please try again.")


run = Management()
run.display_menu()
