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
