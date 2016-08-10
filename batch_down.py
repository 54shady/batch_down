import urllib2
from urllib2 import HTTPError, URLError
import math
import sys
import time
import os

# argv[0] is batch_down.py
# argv[1] is start index
# argv[2] is end index
# argv[3] is target url
# argv[4] is save directory[option]
def Usage():
    print 'Usage: python xxoo.py <start_pic_index> <end_pic_index> <url> [save_dir]'

if len(sys.argv) < 4:
    print 'argument < 4'
    Usage()
    sys.exit(-1)

startIndex = int(sys.argv[1])
endIndex = int(sys.argv[2]) + 1

save_local_dir = ''

if len(sys.argv) == 4:
    save_local_dir = os.getcwd() + '/'
else:
    save_local_dir = sys.argv[4] + '/'

print "The start time: "+time.ctime()
print 'Save pic to : ' + save_local_dir

k = endIndex - startIndex

for i in range(startIndex, endIndex):
    if i < 10:
        url = sys.argv[3] + '0' + str(i) + '.jpg'
    else:
        url = sys.argv[3] + str(i) + '.jpg'
    # print url
    req = urllib2.Request(url)
    req.add_header("User-agent", "Mozilla 5.10")
    name = save_local_dir + str(i) + '.jpg'
    # print name
    try:
        conn = urllib2.urlopen(req)
        f = open(name, 'wb')
        f.write(conn.read())
        f.close()
        if k < 100:
            sys.stdout.write("Computing: [%s%s] %.2f%%\r" % ('#' * (i-startIndex) , '-' * (endIndex-i), (i-startIndex)*100/k))
            sys.stdout.flush()
            time.sleep(0.01)
        else:
            sys.stdout.write("Computing: [%s%s] %.2f%% \r" % ('#' * ((i-startIndex)/(k/50)) , '-' * ((endIndex-i)/(k/50)), (i-startIndex)*100.0/k))
            sys.stdout.flush()
            time.sleep(0.01)
    except HTTPError ,e:
        i = i+1
    except URLError, e:
        print "The server\'s  something is wrong!"
        break
print "\nThe finished time: "+time.ctime()
print 'pic saved'
