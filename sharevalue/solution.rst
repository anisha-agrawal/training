Sharevalue
----------

In this problem we write a python script which prints the latest share value of a company when its NASDAQ symbol is specified as a command line parameter.
For example, to print the share value of Google Inc. (NASDAQ symbol GOOG), we run the script like::

    $ ./sharevalue.py GOOG

The script with explanation:
----------------------------

The script checks if the command entered is in the correct format.
If true, then getvalue() function is called and the NASDAQ symbol is passed to it.
The getvalue() function fetches the share value from the url using urlopen() function of module urllib2 and stores it in a file.
It the passes the file to printvalue() function which prints the share value.

::

    #!/usr/bin/env python
    import sys
    import urllib2

    def getvalue(symbol):
        """
        This function gets the latest share value of the inputted NASDAQ symbol.
        :arg symbol: NASDAQ symbol of a company.
        """
        url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=l1' % symbol
        # url for getting share value
        value = urllib2.urlopen(url) # file containing share value
        printvalue(value) # file passed to printvalue() which prints its contents

    def printvalue(val):
        """
        This function prints the latest share value of the inputted NASDAQ symbol
        :arg val: Share value of imputted NASDAQ symbol of a company.
        """
        print "Share value: %s" % val.read()

    if __name__ == '__main__':
        if len(sys.argv) != 2: #checks if command line parameters are equal to 2 or not
            print "Wrong parameter"
            print "Enter the command in this format: ./sharevalue.py <a valid NASDAQ symbol>"
            sys.exit(1)
        getvalue(sys.argv[1])
        #NASDAQ symbol passed to getvalue() if entered command is in correct format

The script can be found `here <https://github.com/anisha-agrawal/training/blob/master/sharevalue/sharevalue.py>`_
