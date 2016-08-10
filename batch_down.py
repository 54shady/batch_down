import urllib2  
from urllib2 import HTTPError, URLError  
import math  
import sys  
import time  
  
print "The start time: "+time.ctime()  
x = input("Start value:")  
y = input("Stop value:")  
k = y-x  
target_url_prefix = input("Enter the url prefix: ")
save_local_dir = input("Enter the save dir: ")
for i in range(x, y+1):  
    if i < 10:
        url = str(target_url_prefix) + '0' + str(i) + '.jpg'  
    else:
        url = str(target_url_prefix) + str(i) + '.jpg'  
    # print url
    req = urllib2.Request(url)  
    req.add_header("User-agent", "Mozilla 5.10")  
    name = str(save_local_dir) + str(i) + '.jpg'  
    # print name
    try:  
        conn = urllib2.urlopen(req)  
        f = open(name, 'wb')  
        f.write(conn.read())  
        f.close()  
        if k < 100:  
            sys.stdout.write("Computing: [%s%s] %.2f%%\r" % ('#' * (i-x) , '-' * (y-i), (i-x)*100/k))  
            sys.stdout.flush()  
            time.sleep(0.01)  
        else:  
            sys.stdout.write("Computing: [%s%s] %.2f%% \r" % ('#' * ((i-x)/(k/50)) , '-' * ((y-i)/(k/50)), (i-x)*100.0/k))  
            sys.stdout.flush()  
            time.sleep(0.01)  
    except HTTPError ,e:  
        i = i+1  
    except URLError, e:  
        print "The server\'s  something is wrong!"  
        break  
print "\nThe finished time: "+time.ctime()  
print 'pic saved'  
