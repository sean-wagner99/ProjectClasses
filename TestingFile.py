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
class Test:
    def formatDrInfo(self):
        doc_file = open("doctors.txt", "r")
        doc_cont = doc_file.read()
        for category in doc_cont.split("_"):
            id = category[1]
            name = category[2]
            spec = category[3]
            wktime = category[4]
            qual = category[5]
            rmnum = category[6]
            return print(id)

