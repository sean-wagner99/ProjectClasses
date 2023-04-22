"""
Project: Classes
Group Members: Fabian Perez Diaz, Keith Payuran, Ghunder Tayupon, Sean Wagner

In Project document, it says we need to write to a file (idk how -sean)
Perhaps append to write to text file?

Program runs in constant loop, until 0 is entered
"""
# Classes begin here

class Doctor:  # class 1
    def __init__(self, id, name, spec, time, qual, room_num):
        self.__identity = id
        self.__name = name
        self.__specialization = spec
        self.__workingtime =time
        self.__qualification = qual
        self.__roomnum = room_num

    def formatDrIno(self):

    def readDoctorsFile(self):

    def searchDoctorByld(self):

    def searchDoctorByName(self):

    def displayDoctorInfo(self):

    def editDoctorInfo(self):

    def displayDoctorsList(self):


class Facility:  # class 2
    def __init__(self, fac_name):
        self.__facilityname = fac_name

    def addFacility(self):

    def displayFacilities(self):

    def writeListOffacilitiesToFile(self):


class Laboratory:  # class 3
    def __init__(self, lab_name, lab_cost):
        self.__labname = lab_name
        self.__labcost = lab_cost
    def addLabToFile(self):

    def writeListOFLabsToFile(self):

    def displayLabsList(self):

    def formatLabInfo(self):

    def enterLaboratoryInfo(self):

    def readLaboratoriesFile(self):


class Patient:  # class 4
    def __init__(self, pid, name, dis, gen, age):
        self.__pid = pid
        self.__pname = name
        self.__pdis = dis
        self.__pgen = gen
        self.__page = age
    def formatPatientInfo(self):

    def enterPatientInfo(self):

    def readPatientsFile(self):

    def searchPatientByld(self):

    def displayPatientInfo(self):

    def editPatientInfo(self):

    def displayPatientsList(self):

    def writeListOfPatientsToFile(self):

    def addPatientToFile(self):


class Management:  # class 5 // displays menu shown in sample run section, continues til 0 is inputted
    def DisplayMenu(self):
        print("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, "
              "or select 0 to stop:\n")
        cat_type = input(int("1 -  Doctors\n2 -  Facilities\n3 -  Laboratories\n4 -  Patients\n"))
            if cat_type == 1:  # doctors menu
                doc_type = input(int("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - "
                      "Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
                    if doc_type == 1:
                        # show doctor list here
                        print("Back to the previous menu\n")
                    if doc_type == 2:
                        # ask for doctor ID, then match to doctor
                        print("Back to the previous menu\n")
                    if doc_type == 3:
                        # search doctor by name, then match to doctor
                        print("Back to the previous menu\n")
                    if doc_type == 4:
                        # add doctor to list
                        # below needs to be moved to proper function
                        doc_id = input("Enter the doctor's ID:\n")
                        doc_name = input("Enter the doctor's name:\n")
                        doc_spec = input("Enter the doctor's speciality:\n")
                        doc_timing = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
                        doc_qual = input("Enter the doctor's qualification:")
                        doc_rm_num = input("Enter the doctor's room number:\n")
                        doc_add = doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num
                        print("Back to the previous menu\n")
                    if doc_type == 5:
                        # edit doctor info
                        # below needs to be moved to proper function
                        doc_search_ID = input("Please enter the ID of the doctor that you want to edit their information:\n")
                        doc_new_name = input("Enter new Name:\n")
                        doc_new_spec = input("Enter new Specialist in:\n")
                        doc_new_timing = input("Enter new Timing:\n")
                        doc_new_qual = input("Enter new Qualification\n")
                        doc_new_rm_num = input("Enter new Room Number:\n")
                        print("Back to the previous menu\n")
                    if doc_type == 6:
                        # redirect to start menu
                        print("Back to the previous menu\n")
                        continue
            elif cat_type == 2:  # facilities menu
                fac_type = input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n"
                                 "3 - Back to the Main Menu\n")
                    if fac_type == 1:
                        print(f"The Hospital Facilities are:\n{fac_1}\n{fac_2}\n{fac_3}\n{fac_4\n}")
                    if fac_type == 2:
                        fac_new_name = input("Enter Facility name:\n")
                    if fac_type == 3:
                        continue
            elif cat_type == 3:  # laboratories menu
                lab_type = input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n"
                                 "3 - Back to the Main Menu\n")
                    if lab_type == 1:
                        # display lab list
                    if lab_type == 2:
                        # add new lab
                    if lab_type == 3:
                        print("Back to the previous menu\n")
                        continue
            elif cat_type == 4:  # patients menu
                pat_type = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n"
                                 "3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu:\n")
                    if pat_type == 1:
                        # display patients lsit
                    if pat_type == 2:
                        # search for patient by ID
                    if pat_type == 3:
                        # add new patient
                    if pat_type == 4:
                        # edit patient info
                    if pat_type == 5:
                        print("Back to the previous menu\n")
                        continue
            elif cat_type == 0:
                break
            else:
                print("Invalid input, please try again.")


# Classes end here
