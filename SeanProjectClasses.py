"""
Sean's Project Classes Branch

Testing Below
Doctor:
1 - Error, should be formatted to a table
2 - Error
3 - Error
4 - Error
5 - Error
6 - Error

Patient:
1 - Works, but should be formatted to a table // first entry displayed should be hidden
2 - Works, but should be formatted to a table
3 - Works
4 - Works
5 - Works
"""


class Doctor:
    def __init__(self, doc_id=None, doc_name=None, doc_spec=None, doc_timing=None,
                 doc_qual=None, doc_rm_num=None):
        self.__doc_id = doc_id
        self.__doc_name = doc_name
        self.__doc_spec = doc_spec
        self.__doc_timing = doc_timing
        self.__doc_qual = doc_qual
        self.__doc_rm_num = doc_rm_num

    def get_doctor_id(self):
        return self.__doc_id

    def set_doctor_id(self, new_id):
        self.__doc_id = new_id

    def get_name(self):
        return self.__doc_name

    def set_name(self, new_name):
        self.__doc_name = new_name

    def get_specialization(self):
        return self.__doc_spec

    def set_specialization(self, new_specialization):
        self.__doc_spec = new_specialization

    def get_working_time(self):
        return self.__doc_timing

    def set_working_time(self, new_working_time):
        self.__doc_timing = new_working_time

    def get_qualification(self):
        return self.__doc_qual

    def set_qualification(self, new_qualification):
        self.__doc_qual = new_qualification

    def get_room_number(self):
        return self.__doc_rm_num

    def set_room_number(self, new_room_number):
        self.__doc_rm_num = new_room_number

    def __str__(self):
        return f"{self.__doc_id}_{self.__doc_name}_{self.__doc_spec}_{self.__doc_timing}_{self.__doc_qual}_{self.__doc_rm_num}"


class DoctorManager:
    def __init__(self):
        pass

    def format_dr_info(self, doctor):
        return f"{doctor.__doc_id}_{doctor.__doc_name}_{doctor.__doc_spec}_{doctor.__doc_timing}_{doctor.__doc_qual}_{doctor.__doc_rm_num}"

    def enter_dr_info(self):
        doc_id = input("Enter the doctor\'s ID:\t")
        doc_name = input("Enter the doctor\'s name:\t")
        doc_spec = input("Enter the doctor\'s speciality:\t")
        doc_timing = input("Enter the doctor\'s timing (e.g., 7am-10pm):\t")
        doc_qual = input("Enter the doctor\'s qualification:\t")
        doc_rm_num = input("Enter the doctor\'s room number:\t")
        doctor = doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num
        return doctor

    def read_doctors_file(self):
        with open("doctors.txt", "r") as f:
            for line in f:
                doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num = line.strip().split("_")
                doctor = Doctor(doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num)
                self.doctors.append(doctor)
        pass

    def search_doctor_by_id(self):
        pass

    def search_doctor_by_name(self):
        pass

    def display_doctor_info(self, doctor):
        pass

    def edit_doctor_info(self):
        choice = input("Please enter the id of the doctor that you want to edit their information:\t")
        # call search doctor by ID
        doc_new_name = input("Enter new name:\t")
        doc_new_specialist = input("Enter new Specialist:\t")
        doc_new_timing = input("Enter new Timing:\t")
        doc_new_qualification = input("Enter new Qualification:\t")
        doc_new_room = input("Enter new Room number:\t")
        # compile new info together for formatting
        # call function here
        # print(f"Doctor whose ID is {} has been edited\n")
        pass

    def display_doctors_list(self):  # needs to be represented as a table
        for doctor in self.doctors:
            self.display_doctor_info(doctor)
            print()

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as f:
            for doctor in self.doctors:
                f.write(self.format_dr_info(doctor))

    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        self.doctor.append(doctor)
        with open("doctors.txt", "a") as f:
            f.write(self.format_dr_info(doctor))
        return print("New doctor added.")


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

    def display_patient_info(self, patient):  # needs to be represented as a table
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
        return print("New patient added.")


class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            choice = input("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, or "
                           "select 3 to stop:\n1 -  Doctors\n2 -  Patients\n3 -  Exit Program\n")
            if choice == "1":
                print(" ")
                self.display_doctor_menu()
            elif choice == "2":
                print(" ")
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
                doc_new_name = self.doctor_manager.add_dr_to_file()
                self.doctor_manager.write_list_of_doctors_to_file()
                print("New doctor added successfully.")
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()  # doctor_id was here but removed because it was an unexpected argument
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
                self.patient_manager.search_patient_by_id()  # patient_id was here but removed because it was an unexpected argument
            elif choice == "3":
                new_patient = self.patient_manager.add_patient_to_file()
                self.patient_manager.write_list_of_patients_to_file()
                print("New patient added successfully.")
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()  # patient_id was here but removed because it was an unexpected argument
                self.patient_manager.write_list_of_patients_to_file()
                print("Patient information updated successfully.")
            elif choice == "5":
                print(" ")
                self.display_menu()
            else:
                print("Invalid choice. Please try again.")


run = Management()
run.display_menu()
