#doc_file = open("doctors.txt", "r")
#doc_cont = doc_file.read()
#doc_file.close()
#doc_list = [doc_cont]
#doc_list.sort()
#print(doc_list)

'''
Trying to figure out how to format text file to table
also how to figure out appending/searching the data
'''
    def formatDrInfo():
        doc_file = open("doctors.txt", "r")
        doc_cont = doc_file.read()
        doc_cont.split("_")
        value = 0
        id = []
        name = []
        spec = []
        wktime = []
        qual = []
        rmnum = []

        for sentence in doc_cont:




x = Doctor
x.formatDrInfo()
