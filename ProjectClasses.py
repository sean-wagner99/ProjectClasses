"""
Project: Classes
Group Members: Fabian Perez Diaz, Keith Payuran, Ghunder Tayupon, Sean Wagner
"""
# Classes begin here

class Doctor:  # class 1
    def __init__(self, a, b, c, d, e, f):
        self.__identity = a
        self.__name = b
        self.__specialization = c
        self.__workingtime =d
        self.__qualification = e
        self.__roomnum = f

    def formatDrIno(self):

    def readDoctorsFile(self):

    def searchDoctorByld(self):

    def searchDoctorByName(self):

    def displayDoctorInfo(self):

    def editDoctorInfo(self):

    def displayDoctorsList(self):


class Facility:  # class 2
    def __init__(self):

    def addFacility(self):

    def displayFacilities(self):

    def writeListOffacilitiesToFile(self):


class Laboratory:  # class 3
    def __init__(self):


class Patient:  # class 4
    def __init__(self):


class Management:  # class 5
    def __init__(self):


# Classes end here

# lines below need to be added into a loop or something
print("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, or select 0 to stop:\n")
print("1 -  Doctors\n2 -  Facilities\n3 -  Laboratories\n4 -  Patients")