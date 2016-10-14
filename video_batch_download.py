#!/usr/bin/env python

import urllib2
import re
from bs4 import BeautifulSoup
import os

# visit all directories
for i in range(1, 69):
    url = 'http://media.vimcasts.org/videos/'
    url = url + str(i) + '/'

    # send url request
    req = urllib2.Request(url)
    req.add_header("User-agent", "Mozilla 5.10")
    conn = urllib2.urlopen(req)
    context = conn.read()

    # download m4v format, so match this key word
    names = re.compile(r'm4v')

    # get href value
    soup = BeautifulSoup(context, "html5lib")
    for link in soup.find_all('a'):
        name = link.get('href')

        # find the target video, wget the video
        if names.search(name):
            download_target = url + name
            cmd = 'wget ' + download_target
            os.system(cmd)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
