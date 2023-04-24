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

    def format_dr_info(self, Doctor):
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
    def __init__(self, pid="", name="", disease="", gender="", age=0):
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
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        with open("patients.txt", "r") as f:
            for line in f:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    def search_patient_by_id(self):
        pid = input("Enter patient ID: ")
        for patient in self.patients:
            if patient.pid == pid:
                self.display_patient_info(patient)
                return
        print("Can't find the patient...")

    def display_patient_info(self, patient):
        print(f"Patient ID: {patient.pid}")
        print(f"Name: {patient.name}")
        print(f"Disease: {patient.disease}")
        print(f"Gender: {patient.gender}")
        print(f"Age: {patient.age}")

    def edit_patient_info_by_id(self):
        pid = input("Enter patient ID to edit: ")
        for patient in self.patients:
            if patient.pid == pid:
                patient.name = input("Enter new name: ")
                patient.disease = input("Enter new disease: ")
                patient.gender = input("Enter new gender: ")
                patient.age = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                print("Patient information updated.")
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
        print("New patient added.")


class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("MAIN MENU")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit")
            choice = input("Enter your choice: ")

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
            print("DOCTOR MENU")
            print("1. Display list of doctors")
            print("2. Search for a doctor by ID")
            print("3. Search for a doctor by name")
            print("4. Add a new doctor")
            print("5. Edit a doctor's information")
            print("6. Back to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                doctor_id = input("Enter the doctor ID: ")
                self.doctor_manager.search_doctor_by_id(get_doctor_id)
            elif choice == "3":
                doctor_name = input("Enter the doctor name: ")
                self.doctor_manager.search_doctor_by_name(get_doctor_name)
            elif choice == "4":
                new_doctor = self.doctor_manager.add_doctor_to_file()
                self.doctor_manager.write_list_of_doctors_to_file()
                print("New doctor added successfully.")
            elif choice == "5":
                doctor_id = input("Enter the doctor ID: ")
                self.doctor_manager.edit_doctor_info(doctor_id)
                self.doctor_manager.write_list_of_doctors_to_file()
                print("Doctor information updated successfully.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_patient_menu(self):
        while True:
            print("PATIENT MENU")
            print("1. Display list of patients")
            print("2. Search for a patient by ID")
            print("3. Add a new patient")
            print("4. Edit a patient's information")
            print("5. Back to main menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                patient_id = input("Enter the patient ID: ")
                self.patient_manager.search_patient_by_id(patient_id)
            elif choice == "3":
                new_patient = self.patient_manager.add_patient_to_file()
                self.patient_manager.write_list_of_patients_to_file()
                print("New patient added successfully.")
            elif choice == "4":
                patient_id = input("Enter the patient ID: ")
                self.patient_manager.edit_patient_info_by_id(patient_id)
                self.patient_manager.write_list_of_patients_to_file()
                print("Patient information updated successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
