"""
Project: Classes
Group Members: Fabian Perez Diaz, Keith Payuran, Ghunder Tayupon, Sean Wagner

Writing/Reading a file (module 3, part 2 pp)

Program runs in constant loop, until 0 is entered

We will likely need to re-add data files as we will be writing on them in our tests
"""


class Doctor:  # class 1
    def __init__(self, id, name, spec, time, qual, room_num):
        self.__id = id
        self.__name = name
        self.__spec = spec
        self.__worktime =time
        self.__qual = qual
        self.__rmnum = room_num

    def formatDrInfo(self, id, name, spec, worktime, qual, rmnum):  # this function needs to
        doc = f"{id}_{name}_{spec}_{worktime}_{qual}_{rmnum}"
        return doc

    def enterDrInfo(self):
        doc_id = input("Enter the doctor's ID:\n")
        doc_name = input("Enter the doctor's name:\n")
        doc_spec = input("Enter the doctor's speciality:\n")
        doc_timing = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
        doc_qual = input("Enter the doctor's qualification:")
        doc_rm_num = input("Enter the doctor's room number:\n")
        doc_new = doc_id, doc_name, doc_spec, doc_timing, doc_qual, doc_rm_num
        return doc_new

    def readDoctorsFile(self):  # opens doctors.txt // adds doctor objects to a list
        doc_file = open("doctors.txt", "r")
        doc_cont = doc_file.read()
        doc_file.close()
        doc_list = [doc_cont]
        return doc_list

    def searchDoctorByld(self):
        pass

    def searchDoctorByName(self):
        pass

    def displayDoctorInfo(self):
        doc_file = open("doctors.txt", "r")
        doc_cont = doc_file.read()
        doc_file.close()
        return print(doc_cont)

    def editDoctorInfo(self):
        doc_search_ID = input("Please enter the ID of the doctor that you want to edit their information:\n")
        doc_new_name = input("Enter new Name:\n")
        doc_new_spec = input("Enter new Specialist in:\n")
        doc_new_timing = input("Enter new Timing:\n")
        doc_new_qual = input("Enter new Qualification\n")
        doc_new_rm_num = input("Enter new Room Number:\n")
        doc_edit = doc_search_ID, doc_new_name, doc_new_spec, doc_new_timing, doc_new_qual, doc_new_rm_num
        doc_edit_form = self.formatDrInfo(doc_edit)
        # needs more work

    def displayDoctorsList(self):
        pass

    def writeListOfDoctorsToFile(self):
        pass

    def addDrToFile(self):
        doc_file = open("doctors.txt", "a")
        doc_file.write()  # need function name here
        doc_file.close()
        return


class Facility:  # class 2
    def __init__(self, fac_name):
        self.__facilityname = fac_name

    def addFacility(self):  # appends facility name to the file
        fac_file = open("facilities.txt", "a")
        fac_input = input("Enter Facility name:\n")
        fac_file.write(fac_input)  # needs to be written on new line
        fac_file.close()
        return

    def displayFacilities(self):  # displays the list of facilities
        fac_file = open("facilities.txt", "r")
        fac_cont = fac_file.read()
        fac_file.close()
        return print(fac_cont)  # not done yet

    def writeListOffacilitiesToFile(self):  # writes facilities list to file
        fac_file = open("facilities.txt", "w")
        fac_cont = fac_file.read()
        fac_file.close()
        return fac_file.write(fac_cont)  # this function needs to be tested


class Laboratory:  # class 3
    def __init__(self, lab_name, lab_cost):
        self.__lab_nm = lab_name
        self.__lab_cst = lab_cost

    def addLabToFile(self):
        lab_file = open("laboratories.txt", "a")
        lab_file.write()  # need to add function to be added
        lab_file.close()
        pass

    def writeListOFLabsToFile(self):
        pass

    def displayLabsList(self):
        lab_file = open("laboratories.txt", "r")
        lab_cont = lab_file.read()
        lab_file.close()
        return lab_cont

    def formatLabInfo(self, lab_name, lab_cost):
        lab_form = f"{lab_name}_{lab_cost}"
        return lab_form

    def enterLaboratoryInfo(self):
        lab_name = input("Enter Laboratory facility:\n")
        lab_cost = input("Enter Laboratory cost:\n")
        return lab_name, lab_cost

    def readLaboratoriesFile(self):
        lab_file = open("laboratories.txt", "r")
        lab_cont = lab_file.read()
        lab_file.close()
        # need to add lab contents to list
        pass


class Patient:  # class 4
    def __init__(self, pid, name, dis, gen, age):
        self.__pid = pid
        self.__pname = name
        self.__pdis = dis
        self.__pgen = gen
        self.__page = age

    def formatPatientInfo(self, id, name, disease, gender, age):
        patient = f"{id}_{name}_{disease}_{gender}_{age}"
        return patient


    def enterPatientInfo(self):
        patient_ID = input("Please enter your ID:\n")
        patient_name = input("Please enter your Name:\n")
        patient_disease = input("Please enter the disease:\n")
        patient_gender = input("Please enter your gender:\n")
        patient_age = input("Please enter your age:\n")

    def readPatientsFile(self): # opens patients.txt // adds patient objects to a list
        pat_file = open("patients.txt", "r")
        pat_cont = pat_file.read()
        pat_file.close()
        pat_list = [doc_cont]
        return pat_list
    

    def searchPatientByld(self):
        pass

    def displayPatientInfo(self):
        pass

    def editPatientInfo(self):
        pass

    def displayPatientsList(self):
        pat_file = open("patients.txt", "r")
        pat_cont = pat_file.read()
        pat_file.close()
        return print(pat_cont)

    def writeListOfPatientsToFile(self):
        pass

    def addPatientToFile(self):
        pat_file = open("patients.txt", "a")
        #pat_file.write(INSERTHERE)
        #pat_file.close())
        return


class Management:  # class 5 // displays menu shown in sample run section, continues til 0 is inputted
    def DisplayMenu(self):
        print("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, "
              "or select 0 to stop:")
        cat_type = input("1 -  Doctors\n2 -  Facilities\n3 -  Laboratories\n4 -  Patients\n\n")
        cat_type = int(cat_type)
        print(" ")
        while cat_type != 0:
            if cat_type == 1:  # doctors menu
                doc_type = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - "
                    "Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
                if doc_type == 1:
                    # show doctor list here
                    pass
                if doc_type == 2:
                    # ask for doctor ID, then match to doctor
                    pass
                if doc_type == 3:
                    # search doctor by name, then match to doctor
                    pass
                if doc_type == 4:
                    # add doctor to list
                    #enterDrInfo()
                    pass
                if doc_type == 5:
                    # edit doctor info
                    pass
                if doc_type == 6:
                    # redirect to start menu
                    pass
            if cat_type == 2:  # facilities menu
                fac_type = input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n"
                                 "3 - Back to the Main Menu\n")
                if fac_type == 1:
                    print(f"The Hospital Facilities are:")
                if fac_type == 2:
                    fac_new_name = input("Enter Facility name:\n")
                if fac_type == 3:
                    pass
            if cat_type == 3:  # laboratories menu
                lab_type = input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n"
                                 "3 - Back to the Main Menu\n")
                if lab_type == 1:
                    # display lab list
                    pass
                if lab_type == 2:
                    # add new lab
                    pass
                if lab_type == 3:
                    print("Back to the previous menu\n")
            if cat_type == 4:  # patients menu
                pat_type = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n"
                                 "3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n")
                if pat_type == 1:
                    # display patients list
                    pass
                if pat_type == 2:
                    # search for patient by ID
                    pass
                if pat_type == 3:
                    # add new patient
                    pass
                if pat_type == 4:
                    # edit patient info
                    pass
                if pat_type == 5:
                    print("Back to the previous menu\n")
                    continue
            if cat_type == 4:
                print('Test')


run = Management()
run.DisplayMenu()
