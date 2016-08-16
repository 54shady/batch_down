import urllib2
from urllib2 import HTTPError, URLError
import math
import sys
import time
import os

# argv[0] is batch_down.py
# argv[1] is url links

def Usage():
    print 'Usage: python download_from_list.py <url> [save_dir]'

if len(sys.argv) < 2:
    print 'argument < 2'
    Usage()
    sys.exit(-1)

save_local_dir = ''
save_local_dir = os.getcwd() + '/'

print "The start time: "+time.ctime()
print 'Save pic to : ' + save_local_dir

i = 0
for url in open(sys.argv[1]):
    req = urllib2.Request(url)
    req.add_header("User-agent", "Mozilla 5.10")
    name = save_local_dir + str(i) + '.jpg'
    i += 1
    # print name
    try:
        conn = urllib2.urlopen(req)
        f = open(name, 'wb')
        f.write(conn.read())
        f.close()
    except HTTPError ,e:
        i = i+1
    except URLError, e:
        print "The server\'s  something is wrong!"
print "\nThe finished time: "+time.ctime()
print 'pic saved'
