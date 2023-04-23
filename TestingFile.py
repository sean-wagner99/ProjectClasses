#doc_file = open("doctors.txt", "r")
#doc_cont = doc_file.read()
#doc_file.close()
#doc_list = [doc_cont]
#doc_list.sort()
#print(doc_list)

class Management:  # class 5 // displays menu shown in sample run section, continues til 0 is inputted
    def DisplayMenu(self):
        flag = True
        while flag == True:
            print("Welcome to Alberta Hospital (AH) Management System\nSelect from the following options, "
                  "or select 0 to stop:")
            cat_type = input("1 -  Doctors\n2 -  Facilities\n3 -  Laboratories\n4 -  Patients\n\n")
            cat_type = int(cat_type)
            print(" ")
            if cat_type == 1:  # doctors menu
                doc_type = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - "
                    "Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n")
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
                    #enterDrInfo()
                    print("Back to the previous menu\n")
                if doc_type == 5:
                    # edit doctor info
                    pass
                if doc_type == 6:
                    # redirect to start menu
                    print("Back to the previous menu\n")
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
                                 "3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu:\n")
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
            if cat_type == 4:
                print('Test')


run = Management()
run.DisplayMenu()