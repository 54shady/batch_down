import urllib2
from urllib2 import HTTPError, URLError
import math
import sys
import time
import os
import random

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
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]

    #headers = {'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #           'Accept-Encoding': 'none',
    #           'Accept-Language': 'en-US,en;q=0.8',
    #           'Connection': 'keep-alive'}
    print url
    req = urllib2.Request(url)
    #req = urllib2.Request(url, headers=headers)
    browser = random.choice(user_agents)
    req.add_header("User-agent", browser)

    #req.add_header("User-agent", "Mozilla 5.10")
    name = save_local_dir + str(i) + '.jpg'
    #print name
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
        print e
        i = i+1
    except URLError, e:
        print "The server\'s  something is wrong!"
        break
print "\nThe finished time: "+time.ctime()
print 'pic saved'
