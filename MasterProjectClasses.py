"""
Project Classes
Group Members: Keith Payuran, Ghunder Tayupon, Sean Wagner

Note: On original "doctors.txt" file, we changed spelling of specililty (in file) to speciality (in program) - Attached
"""


class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
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
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}\n"

    def enter_dr_info(self):
        doc_id = input("Enter the doctor\'s ID:\t")
        doc_name = input("Enter the doctor\'s name:\t")
        doc_spec = input("Enter the doctor\'s speciality:\t")
        doc_timing = input("Enter the doctor\'s timing (e.g., 7am-10pm):\t")
        doc_qual = input("Enter the doctor\'s qualification:\t")
        doc_rm_num = input("Enter the doctor\'s room number:\t")
        return Doctor(doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num)

    def read_doctors_file(self):
        with open("doctors.txt", "r") as f:
            next(f)
            for line in f:
                doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num = line.strip().split("_")
                doctor = Doctor(doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num)
                self.doctors.append(doctor)

    def search_doctor_by_id(self):
        doc_id = input("\nEnter the doctor's ID:\t")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doc_id:
                self.display_doctor_info(doctor)
                return
        else:
            return print("Can't find the doctor with the same ID on the system.")

    def search_doctor_by_name(self):
        doc_name = input("\nEnter the doctor's name:\t")
        for doctor in self.doctors:
            if doctor.get_name() == doc_name:
                self.display_doctor_info(doctor)
                return
        else:
            print("Can't find the doctor with the same name on the system.")

    def display_doctor_info(self, doctor):
        print(f"\n{doctor.doctor_id}\t", end="")
        print(f"{doctor.name}\t", end="")
        print(f"{doctor.specialization}\t", end="")
        print(f"{doctor.working_time}\t", end="")
        print(f"{doctor.qualification}\t", end="")
        print(f"{doctor.room_number}\t", end="")

    def edit_doctor_info(self):
        doc_id = input("Please enter the id of the doctor that you want to edit their information:\t")
        for doctor in self.doctors:
            if doctor.doctor_id == doc_id:
                doctor.name = input("Enter new Name: ")
                doctor.specialization = input("Enter new Specialist in: ")
                doctor.working_time = input("Enter new Timing: ")
                doctor.qualification = input("Enter new Qualification: ")
                doctor.room_number = input("Enter new Room number: ")
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {doc_id} has been edited\n")
                return
        print("Cannot find the Doctor with the same id on the system")

    def display_doctors_list(self):
        print("Doctor ID\tName\tSpecialization\tWorking Time\tQualification\tRoom Number")
        for doctor in self.doctors:
            self.display_doctor_info(doctor)
            print(" ")

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as f:
            for doctor in self.doctors:
                f.write(self.format_dr_info(doctor))

    def add_dr_to_file(self):
        doctor = self.enter_dr_info()
        self.doctors.append(doctor)
        with open("doctors.txt", "a") as f:
            f.write(self.format_dr_info(doctor))
        return print(f"Doctor whose ID is {doctor.doctor_id} has been added.")


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
        pid = input("\nEnter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        print(" ")
        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        with open("patients.txt", "r") as f:
            next(f)
            for line in f:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    def search_patient_by_id(self):
        pid = input("\nEnter patient ID: ")
        for patient in self.patients:
            if patient.pid == pid:
                self.display_patient_info(patient)
                print(" ")
                return
        print(f"Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):  # error here
        print(f"\n{patient.pid}\t", end="")
        print(f"{patient.name}\t", end="")
        print(f"{patient.disease}\t", end="")
        print(f"{patient.gender}\t", end="")
        print(f"{patient.age}\t", end="")

    def edit_patient_info_by_id(self):
        pid = input("\nPlease enter the id of the Patient that you want to edit their information: ")
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
        print(f"Can't find the patient with the same id in the system")

    def display_patients_list(self):  # for this function we need to skip the first entry
        print("Patient ID\tName\tDisease\tGender\tAge")
        for patient in self.patients:
            self.display_patient_info(patient)
            print(" ")

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as f:
            for patient in self.patients:
                f.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patients.append(patient)
        with open("patients.txt", "a") as f:
            f.write(self.format_patient_info_for_file(patient))
        print(f"Patient whose ID is {patient.pid} has been added.\n")


class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            choice1 = input("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, or "
                            "select 3 to stop:\n1 -  Doctors\n2 -  Patients\n3 -  Exit Program\n")
            if choice1 == "1":
                self.display_doctor_menu()
            elif choice1 == "2":
                self.display_patient_menu()
            elif choice1 == "3":
                print("\nThanks for using the program! Bye")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_doctor_menu(self):
        while True:
            choice = input("\nDoctor Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - "
                           "Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to Main Menu\n")
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_dr_to_file()
                self.doctor_manager.write_list_of_doctors_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
                self.doctor_manager.write_list_of_doctors_to_file()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def display_patient_menu(self):
        while True:
            choice = input("\nPatient Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n"
                           "4 - Edit patient info\n5 - Back to the Main Menu\n")
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_id()
            elif choice == "3":
                self.patient_manager.add_patient_to_file()
                self.patient_manager.write_list_of_patients_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()
                self.patient_manager.write_list_of_patients_to_file()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")


run = Management()
run.display_menu()
