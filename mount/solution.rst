Mount
-----

In this problem we write a python script which gives the same output as the mount command

We use two functions, openfile() and printfile() in the code.
First we call the openfile() function.

 ::

     if __name__ == '__main__':
        openfile() #calling openfile() function

The openfile() function opens the /proc/mounts file and passes its contents to printfile() function line by line.

 ::

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


The printfile() function prints each line in the required format. 
The first line of thr /proc/mounts file should not be printed as it is not present in the output of mount command.
Hence, printfile() first checks if the line passed to it is not the first line, if true then it prints it in the required format otherwise not.
To print each line in the required format, we first strip the newline character form each line, split it based on whitespace and store it in a list.
Then we insert "on" at index 1 and "type" at index 3, remove the last two list items '0' and '0' and finally print the list items in the required format.

 ::

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

We run the script using:
 ::

    $ python mount.py

Or using:
 ::

    $ chmod +x mount.py
    $ ./mount.py

The link to the script can be found `here <https://github.com/anisha-agrawal/training/blob/master/mount/mount.py>`_

