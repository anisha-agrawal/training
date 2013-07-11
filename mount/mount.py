#!/usr/bin/env python
def openfile():
    """
    Function which opens the /proc/mounts file.
    It then passes its contents to printfile() function line by line
    """
    f = open("/proc/mounts") #opens file mounts in read mode
    global i #i denotes line number of file, starting from 1
    i = 1 #i initialised with 1
    for line in f: #loops through the lines in file
        printfile(line) #calls printfile() and passes each line of line to it in string format
        i = i + 1 #i incremented by 1
    f.close() #closes the file mounts

def printfile(x):
    """
    Function which prints each line in the required format
    """
    if i != 1: #checking if i is not representing the first line of the file
        s = x.strip() #to remove newline character
        l = s.split(" ")
        #splits the string s based on whitespace and stores the splitted strings in list l
        l.insert(1, "on") #inserts "on" at index 1 of list l
        l.insert(3, "type") #inserts "type" at index 2 of list l
        del l[-1] #deletes last list item which is last '0' of the file
        del l[-1] #deletes last list item which is second last '0' of the file
        for y in l[0:-1]: #loop to print the  items of l except the last item
            print y,
        print "(%s)" % l[-1] #prints the last item of l in the required format

if __name__ == '__main__':
    openfile() #calling openfile() function
