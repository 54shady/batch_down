#!/usr/bin/python

import urllib
from bs4 import BeautifulSoup

# target url
url = 'http://www.pythonscraping.com/exercises/exercise1.html'

# get url request
req = urllib.request.Request(url)

# add agent(option)
req.add_header("User-agent", "Mozilla 5.10")

# open url
conn = urllib.request.urlopen(req)

# get context
context = conn.read()

# get href value
soup = BeautifulSoup(context, "html5lib");

# print out the header
print(soup.head)
print(soup.title)
print(soup.h1)
print(soup.div)
