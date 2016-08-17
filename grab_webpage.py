import urllib2
from urllib2 import HTTPError, URLError
import math
import sys
import time
import os

from bs4 import BeautifulSoup
import re

# argv[0] is batch_down.py
# argv[1] is url links

def Usage():
    print 'Usage: python grab.py <url>'

if len(sys.argv) < 2:
    print 'argument < 2'
    Usage()
    sys.exit(-1)

url = sys.argv[1]
req = urllib2.Request(url)
req.add_header("User-agent", "Mozilla 5.10")
try:
    conn = urllib2.urlopen(req)
    # print conn.read()
except HTTPError ,e:
    print "HTTP error"
except URLError, e:
    print "The server\'s  something is wrong!"

soup = BeautifulSoup(conn)
print '============prettify==========='
print soup.prettify()
print '============prettify==========='
print '\n'
print '============title   ==========='
print soup.title
print '============title   ==========='
print '\n'
print '============head    ==========='
print soup.head
print '============head    ==========='
print '\n'
print '============soup a  ==========='
print soup.a
print '============soup a  ==========='
print '\n'
print '============soup p  ==========='
print soup.p
print '============soup p  ==========='
