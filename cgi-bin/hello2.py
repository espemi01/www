#!/usr/bin/env python
import os

print "Content-type: text/html\n"

qs = os.environ['QUERY_STRING']

if 'thename' in qs:
    name = qs.split('=')[1]
    print "Set-cookie: 'thename=value'\n"
elif 'thename' not in qs:
	cookie = os.environ['HTTP_COOKIE']
	name = cookie.split('=')[1]
else:
    name = 'No Name Provided'

print "<html>"
print "<body>"
print "<h1>Hello %s</h1>" % name
print "</pre>"
print "</body>"
print "</html>"
